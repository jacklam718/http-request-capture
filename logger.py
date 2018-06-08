# --*--coding: utf-8 --*--

import os

REQ_URLS_FILE = open('req-urls.txt', 'a')

# colors
WHIYE = '\033[0m'
GREEN = '\033[32m'

def log(title, message='', write=False):
    if write:
        REQ_URLS_FILE.write(''.join([message, '\n']))
        REQ_URLS_FILE.flush()
        os.fsync(REQ_URLS_FILE.fileno())
    print(''.join([GREEN, title, WHIYE, message]))
