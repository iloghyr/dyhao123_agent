#!/bin/env python
#encoding: utf-8
# vim: set tw=0 shiftwidth=4 tabstop=4 expandtab number:
'''
Created on 2015-01-24

@author: iloghyr
'''

# import bs4
import urlparse

class WebParser(object):
    """html content WebParser"""
    def __init__(self, parser=None):
        super(WebParser, self).__init__()
        if parser:
            self.parser = parser
        else:
            self.parser = None

    def set_parser(self, parser):
        """
        set parser
        """
        self.parser = parser

    def parse(self, content):
        """
        """
        if not self.parser:
            raise Exception("parser is not set")
        method = 'self._parse_%s' % self.parser
        eval(method)(content)

    def _parse_douyu(self, content):
        """
        douyu tv parser
        """
        print 'douyu'
        pass

    def _parse_huomao(self, content):
        """
        huomao tv parser
        """
        pass

    def _parse_zhanqi(self, content):
        """
        zhanqi tv parser
        """
        pass

    def _parse_panda(self, content):
        """
        panda tv parser
        """
        pass

    def _parse_huya(self, content):
        """
        huya tv parser
        """
        pass

if __name__ == '__main__':
    w = WebParser('douyu')
    w.parse('')



