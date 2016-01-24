#!/bin/env python
#encoding: utf-8
# vim: set tw=0 shiftwidth=4 tabstop=4 expandtab number:
"""
Created on 2015-01-24

@author: iloghyr
"""

import httpclient
import logging


class Worker(object):
    """agent  Worker"""

    def __init__(self, url_list):
        super(Worker, self).__init__()
        self.url_list = url_list
        self._http = httpclient.HttpClient()

    def get_content_iterator(self, target, page=1):
        """
        web content iterator
        """
        for i in xrange(page):
            param_page = i + 1
            url = target % param_page
            yield self._http.get(url)

    def start(self):
        """
        start to run
        """
        print self.url_list

if __name__ == '__main__':
    w = Worker([])
    w.get_web_content('', 5)


