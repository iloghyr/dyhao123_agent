#!/bin/env python
#encoding: utf-8
# vim: set tw=0 shiftwidth=4 tabstop=4 expandtab number:
'''
Created on 2015-01-24

@author: iloghyr
'''
import configmgr
import logging.handlers
import os
import sys

LOG_FORMAT = '%(asctime)s %(name)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s'

def setup_logger(logfile="runtime.log"):
    """
    setup root logger
    """
    logging.basicConfig(format=LOG_FORMAT, stream=sys.stderr, level=logging.DEBUG)
    
    root_logger = logging.getLogger()

    filename = os.path.join('./var', logfile)
    rfile_hdlr = logging.handlers.TimedRotatingFileHandler(filename, when="D",
                                                         interval=1, backupCount=30)
    formatter = logging.Formatter(LOG_FORMAT)
    rfile_hdlr.setFormatter(formatter)
    rfile_hdlr.setLevel(logging.DEBUG)
    root_logger.addHandler(rfile_hdlr)

    # hacking the requests' logger
    requests_logger = logging.getLogger("requests")
    requests_logger.setLevel(logging.WARNING)
