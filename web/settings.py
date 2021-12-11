# coding: utf-8
#

import os

RDB_HOST = os.getenv("RDB_HOST") or "localhost"
RDB_PORT = int(os.getenv("RDB_PORT") or "28015")
RDB_USER = os.getenv("RDB_USER") or "admin"
RDB_PASSWD = os.getenv("RDB_PASSWD") or None
RDB_DBNAME = os.getenv("RDB_DBNAME") or "atxserver2"

AUTH_BACKENDS = {
    "openid": {
        "endpoint": "https://login.netease.com/openid/"
    }
}

GITHUB = {
    "client_id": "12f69b6ce758ad8cba97",
    "client_secret": "8237514344c77842b9c35962f65be433d8df49c1",
    "redirect_uri": "http://localhost:4000/login"
}



# CAS setting
CAS_SETTINGS = {
    # replace this with your cas server url
    'cas_server': 'http://test-sso.iqiyi.com/cas',
    # replace this with your website url
    'service_url': 'http://127.0.0.1:4000/login',
    # CAS protocol version, 1.0 or 2.0? default is 2.0.
    'version': 2
}