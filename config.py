__author__ = "javad salary"


import os


class Config:
    def __init__(self):
        self.applications_root = os.path.join(os.path.dirname(__file__), "")
        self.web = {
            'port': 8090,
            'server_ip': '127.0.0.1',
        }
