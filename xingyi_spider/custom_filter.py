#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by gaohuaguang
from __future__ import unicode_literals
from scrapy.dupefilter import RFPDupeFilter


class FlytrapURLFilter(RFPDupeFilter):
    """A dupe filter that considers the URL"""

    def __init__(self, path=None, debug=False):
        self._urls = set()
        super(FlytrapURLFilter, self).__init__(path, debug)

    def request_seen(self, request):
        if '#' in request.url:
            return True
        if request.url in self._urls:
            return True
        else:
            self._urls.add(request.url)
        super(FlytrapURLFilter, self).request_seen(request)
