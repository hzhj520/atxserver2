# coding: utf-8
#
from concurrent.futures import ThreadPoolExecutor
from .base import BaseRequestHandler, AuthRequestHandler
from .login import OpenIdLoginHandler, SimpleLoginHandler, GithubLoginHandler, CASLoginHandler

from ..settings import CAS_SETTINGS
from urllib.parse import quote

class LogoutHandler(BaseRequestHandler):
    def get(self):
        self.clear_all_cookies()
        # self.redirect("/login")
        redirect_url = CAS_SETTINGS['cas_server'] + \
            '/logout?service=' + quote(CAS_SETTINGS['service_url'])
        self.redirect(redirect_url)

class MainHandler(AuthRequestHandler):
    def get(self):
        self.redirect("/devices")
