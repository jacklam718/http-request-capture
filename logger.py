# --*--coding: utf-8 --*--

from os import fsync
from time import strftime

REQ_URLS_FILE = open('req-urls.txt', 'a')

# colors
WHIYE = '\033[0m'
GREEN = '\033[32m'

def log(message=''):
    loggedTime = strftime('%a, %d %b %Y %H:%M:%S %z: ')
    print(''.join([GREEN, loggedTime, WHIYE, message]))

def writeLog(message):
    REQ_URLS_FILE.write(''.join([message, '\n']))
    REQ_URLS_FILE.flush()
    fsync(REQ_URLS_FILE.fileno())
