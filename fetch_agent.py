#!/bin/env python
#encoding: utf-8
# vim: set tw=0 shiftwidth=4 tabstop=4 expandtab number:
'''
Created on 2015-01-24

@author: iloghyr
'''

import sys
import ast
import logging
import lib.logger
import lib.configmgr
import lib.worker


class FetchAgent(object):
    """
    fetch online live agent
    """
    def __init__(self):
        """
        init
        """
        self.cm = lib.configmgr.ConfigMgr.instance()
        self.cm.init()
        lib.logger.setup_logger()

    def run(self):
        """
        main runner
        """
        config = self.cm.get_section_items('main')
        url_list = config.get('url_list')
        url_list = ast.literal_eval(url_list)
        worker = lib.worker.Worker(url_list)
        worker.start()







if __name__ == '__main__':
    fetchAgent = FetchAgent()
    fetchAgent.run()