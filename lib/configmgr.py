#!/bin/env python
# encoding: utf-8
# vim: set tw=0 shiftwidth=4 tabstop=4 expandtab number:
"""
Created on 2016-01-01

@author: iloghyr
"""
import ConfigParser
import datetime
import logging
import os

  


class ConfigMgr(object):
    """
    conf manage instance class
    """

    def __init__(self):
        """
        """
        self._initialized = False
        self._configer = None

        self.lib_dir = os.path.dirname(os.path.realpath(__file__))
        self.work_dir = os.path.dirname(self.lib_dir)
        self.conf_dir = os.path.join(self.work_dir, "conf")

    def _load_config_file(self, config_file):
        """
        load config file
        """
        if config_file is None:
            config_file = os.path.join(self.conf_dir, "main.conf")

        self._configer = ConfigParser.ConfigParser()
        readok = self._configer.read(config_file)

        if config_file not in readok:
            raise Exception("load config file %s failed" % config_file)

        self.logger.info("load config from %s", config_file)

    @classmethod
    def instance(cls):
        """
        get instance of this module
        """
        key = "__instance__"
        if hasattr(cls, key):
            return getattr(cls, key)
        else:
            cm = ConfigMgr()
            setattr(cls, key, cm)
            return cm

    def init(self, config_file=None):
        """
        init configMgr, must be called after first call of instance()
        """
        if self._initialized:
            return
        
        self.logger = logging.getLogger(__name__)
        # load config file
        self._load_config_file(config_file)
        self._initialized = True

    def get_section_items(self, section):
        """
        get sepcific section configs in config file as dict
        """
        if self._configer is not None:
            configs = self._configer.items(section)
            return dict(configs)

        raise Exception("config file not loaded")

