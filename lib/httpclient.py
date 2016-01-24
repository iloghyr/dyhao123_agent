#!/bin/env python
#encoding: utf-8
"""
Created on 2016-01-24

@author: iloghyr
"""
import logging
import random
import requests
import time

class HttpClient(object):
    """
    Common Http Client for HTTP Interface
    """

    def __init__(self):
        """
        init
        """
        self.logger = logging.getLogger(__name__)
        self.retries = 3
        self.timeout = 3.0
        self.headers = {'Accept': 'Accept:text/html,application/xhtml+xml'
                                        ',application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Cache-Control': 'no-cache',
                        'Accept-Language': 'zh-CN,zh;q=1',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/47.0.2526.80 Safari/537.36'
                        }

    def set_timeout(self, timeout=3):
        """
        set timeout 
        """
        self.timeout = float(timeout)

    def set_retries(self, retries=3):
        """
        set retries
        """
        self.retries = int(retries)
    
    def _requests(self, method, url, json_check, **kwargs):
        for i in xrange(self.retries):
            try:
                # before retry sleep some random time (1,5)
                if i != 0:
                    time.sleep(random.randint(1, 3))

                r = requests.request(method, url, headers=self.headers, **kwargs)
                
                r.raise_for_status()
                if not json_check:
                    return r.text

                j = r.json()

                if not isinstance(j, dict) or "status" not in j:
                    raise Exception("response format wrong for %s with params:%s" % (url, 
                                                                                     str(kwargs)))
                if j["status"] == 0:
                    return j
                    
                # no matter what status is, request is ok
                break  
            except Exception as e:
                self.logger.error("#%d base_url:%s params:%s failed:%s" % (i,
                                                                           url, 
                                                                           str(kwargs),
                                                                           str(e)))
        return None

    def get(self, url, json_check=False):
        """
        request via GET
        """
        return self._requests("get", url,
                              timeout=self.timeout,
                              json_check=json_check,
                              allow_redirects=True)

    def post(self, url, data, json_check=False):
        """
        request via POST
        """
        return self._requests("post", url,
                              data=data,
                              json_check=json_check,
                              timeout=self.timeout)


