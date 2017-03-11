#!/usr/bin/env python
# coding=utf-8

DB = {
    "host": "127.0.0.1",
    "servername": "localhost",
    "port": 3306,
    "dbname": "main_portal",
    "username": "portal_admin",
    "password": "123456",
    "main_table": "lib_books",
    "inp_table": "inp_list",
    "genres_table": "lib_genres",
    "genre2group": "lib_genremeta",
    "charset": "utf8"
}

LIBRARY = {
    "archives_path": "/media/olmer/Documents-HDD41/_Lib.rus.ec - Официальная/lib.rus.ec",
    "inpx_file": "/media/olmer/Documents-HDD41/_Lib.rus.ec - Официальная/librusec_local_fb2.inpx",
    # "library_files": "/media/olmer/Documents-HDD4/lib_files"
    "library_files": "/home/olmer/pCloudDrive/lib.rus.ec"

}

PCLOUD = {
    "client_id": "R3Qp2U2jzLz",
    "client_secret": "XnuHTHSaCBQ4RJtl3vyYxm2R2rok",
    "access_token": "fAJLZR3Qp2U2jzLzZCKltq7ZqARlEFYiSmuXklWlY83PkR8Y3zgk",
    "authorize_url": "https://my.pcloud.com/oauth2/authorize",
    "api_url": "https://api.pcloud.com",
    "redirect_uri": "http://localhost:5000/getcode",
    "methods": {
        "o2token": {"name": "oauth2_token"},
        "folder": {"name": "listfolder", "params": {"path": "/"}},
        "link": {"name": "getfilelink", "params": {"path": "/%s/%s"}},
        "checksumfile": {"name": "checksumfile", "params": {"path": "/%s/%s"}},
        "publink": {"name": "getfilepublink", "params": {"path": "/%s/%s"}},
        "download": {"name": "getpublinkdownload", "params": {"code": "%s"}}
    }
}
