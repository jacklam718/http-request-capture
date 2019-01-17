#!/usr/bin/python
# --*--coding: utf-8 --*--

from scapy.all import IP, Raw, sniff
from logger import log, writeLog

def extract_headers_from_request_payload(payload):
    try:
        return payload.split('\r\n\r\n')[0].split('\r\n')
    except ValueError:
        return payload.split('\r\n')

def find_url_from_headers(headers):
    host = ''
    uri = ''
    method = headers[0][0:headers[0].find('/')].strip()
    for line in headers:
        # find host & uri
        if 'Host: ' in line: host = line.split('Host: ')[1].strip()
        if ('%s /' % method) in line: uri = line.split('%s ' % method)[1].split(' HTTP/')[0].strip()
    return ''.join([host, uri])

def http_parser():
    payload = {'global' : ''}
    last_ack = {'global' : None}
    def parse_http_request(pkt):
        if not pkt.haslayer(Raw):
            return
        # if latest ack number same as last_ack means: it's segmented
        #nonlocal payload, last_ack

        if pkt[IP].ack == last_ack['global']:
            payload['global'] = payload['global'] + pkt[Raw].load.decode('utf-8', 'ignore')
        else:
            payload['global'] = pkt[Raw].load.decode('utf-8', 'ignore')
            last_ack['global'] = pkt[IP].ack
        # find request url and log it if found
        url = find_url_from_headers(extract_headers_from_request_payload(payload['global']))
        if url:
            log(url)
            writeLog(url)
    return parse_http_request

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    # get args from cli
    parser.add_argument('--iface', default='eth0', type=str)
    parser.add_argument('--port', default=80, type=int)
    args = parser.parse_args()
    log(
        'sniffing http requests on port {port} using network interface {iface}'
        .format(port=args.port, iface=args.iface)
    )
    sniff(
        prn=http_parser(),
        iface=args.iface,
        filter='tcp and port {port}'.format(port=args.port),
    )