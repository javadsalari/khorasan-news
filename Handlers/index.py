#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import tornado.web
import tornado
import json

__author__ = "javad salary"


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        r = requests.get('http://google.com')
        response = r.text
        self.render('index.html')

    def post(self, *args, **kwargs):
        # amount = self.get_argument('amount')

        self.write('success')
