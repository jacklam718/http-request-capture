## Http Request Capture written in Python

### Usage
python3:
`sudo python3 http_request_capture.py --iface en0 --port 80`

python2:
`sudo python http_request_capture.py --iface en0 --port 80`
#### arguments
- `--iface` - default `en0`
- `--port` - default `80`

#### Requirements:
* Python3
* [kamene](https://github.com/phaethon/kamene)


Or


* Python2
* [scapy](https://github.com/secdev/scapy)

##### http made from browser
<img src="https://raw.githubusercontent.com/jacklam718/http-request-capture/master/.github/request-made-from-browser.png" width="300" />

##### capture http request
<img src="https://raw.githubusercontent.com/jacklam718/http-request-capture/master/.github/capture-http-request.png" width="300" />
