#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "javad salary"

import requests
import tornado.web
import tornado
import json


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        response_iran = requests.get("http://www.servicefarsi.com/api/news/1721693086955/4/item=0,page=1/ ")
        response_ostan = requests.get("http://www.servicefarsi.com/api/news/1721693086955/4/item=19,page=1/")
        response_ostan = json.loads(response_ostan.text)
        data_ostan = response_ostan['res']
        response_iran = json.loads(response_iran.text)
        data_iran = response_iran['res']
        self.render("index.html", data_ostan=data_ostan ,data_iran=data_iran)



class NewsBodyHanler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        response = requests.get("http://www.servicefarsi.com/api/news/1721693086955/4/item=0,page=3/ ")
        id_ostan = requests.get("http://www.servicefarsi.com/api/news/1721693086955/2/")
        id_status = requests.get("http://www.servicefarsi.com/api/news/1721693086955/1/")
        id_status = json.loads(id_status.text)
        id_status = id_status['res']
        id_ostan = json.loads(id_ostan.text)
        id_ostan = id_ostan['res']
        url = "http://www.servicefarsi.com/api/news/1721693086955/7/item=" + args[0]
        response_body = requests.get(url)
        response_body = json.loads(response_body.text)
        response_body_data = response_body['res']
        response_data = json.loads(response.text)
        self.render("body_news.html", response_body_data=response_body_data, id_ostan=id_ostan,
                    id_status=id_status)

    def post(self, *args, **kwargs):
        # amount = self.get_argument('amount')

        pass
