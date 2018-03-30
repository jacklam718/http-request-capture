# --*--coding: utf-8 --*--

import os

REQ_URLS_FILE = open('req-urls.txt', 'a')

def log(title, message='', write=False):
    w = '\033[0m'
    g = '\033[32m'
    # write log message to log file if `write == true`
    if write:
        REQ_URLS_FILE.write(''.join([message, '\n']))
        REQ_URLS_FILE.flush()
        os.fsync(REQ_URLS_FILE.fileno())
    print(''.join([g, title, w, message]))
