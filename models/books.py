#!/usr/bin/env python
# coding=utf-8

import config as cfg
import book_info
from middleware.dbconnection import mysql_connection

"""books_data: AUTHOR;GENRE;TITLE;SERIES;SERNO;FILE;SIZE;LIBID;DEL;EXT;DATE;LANG;LIBRATE;KEYWORDS;ETC
   inp_list: INP_ID, INP_NAME, INSERTED
   """


class Books(object):
    def __init__(self):
        self.connection = mysql_connection()

    def is_inp_exist(self, name):
        sql = "SELECT INP_ID FROM {0} WHERE INP_NAME = '{1}' AND STATUS='1'".format(cfg.DB["inp_table"], name)
        try:
            row = self.connection.execute_fetch(sql)
            return row is not None
        except Exception as error:
            pass
            # print "Error: unable to fecth data %s" % error

        return False

    def add_inp(self, name):
        sql = "INSERT INTO {0} (INP_NAME) VALUES('{1}')".format(cfg.DB["inp_table"], name)
        return self.connection.execute_transact(sql)

    def update_inp(self, inp_id):
        if inp_id is None:
            return
        sql = "UPDATE {} SET STATUS=%s WHERE INP_ID=%s".format(cfg.DB["inp_table"])
        self.connection.execute_transact(sql, ('1', inp_id), True)

    def find_by_file(self, libid, filename):
        info = None
        sql = u"SELECT AUTHOR,GENRE,TITLE,SERIES,SERNO,FILE,SIZE,LIBID,DEL,EXT,DATE,LANG,LIBRATE,KEYWORDS, PATH, BID FROM {} WHERE LIBID = %s AND  FILE = %s".format(
            cfg.DB["main_table"])
        try:
            row = self.connection.execute_fetch(sql, True, (int(libid), int(filename)))
            info = book_info.BookInfo()
            info.load_from_row(row)

        except Exception as error:
            print "Error: unable to fecth data %s" % error
        return info

    def save_book(self, info):
        if info is None or info.params is None:
            return None
        sql = u"INSERT INTO {} (AUTHOR,GENRE,TITLE,SERIES,SERNO,FILE,SIZE,LIBID,DEL,EXT,DATE,LANG,LIBRATE,KEYWORDS,PATH) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s,%s)".format(
            cfg.DB["main_table"])
        return self.connection.execute_transact(sql, info.params)

    def update_book(self, info, bid):
        if info is None or bid is None or info.params is None:
            return
        sql = u"UPDATE {} SET AUTHOR = %s, TITLE=%s, GENRE=%s, DEL = %s, LIBRATE = %s, KEYWORDS = %s, UPDATED = CURRENT_TIMESTAMP, PATH = %s WHERE BID = %s".format(
            cfg.DB["main_table"])
        self.connection.execute_transact(sql, (
        info.author, info.title, info.genre, info.deleted, info.librate, info.keywords, info.path, bid), True)

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
