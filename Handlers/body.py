__author__ = 'Javad'

import tornado.web
import requests
import json


class BodyHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        id_ = args[0]
        url = "http://www.servicefarsi.com/api/news/1721693086955/7/item=" + id_
        response = requests.get(url)
        data = response.text
        data = json.loads(data)
        data_ = data[u'res']
        self.render("fullwidth.html", data=data_)

    def post(self, *args, **kwargs):
        pass
