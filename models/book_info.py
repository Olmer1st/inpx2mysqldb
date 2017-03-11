#!/usr/bin/env python
# coding=utf-8

"""AUTHOR','GENRE','TITLE;SERIES;SERNO;FILE;SIZE;LIBID;DEL;EXT;DATE;LANG;LIBRATE;KEYWORDS;"""


class BookInfo(object):
    fields = ['AUTHOR', 'GENRE', 'TITLE', 'SERIES', 'SERNO', 'FILE', 'SIZE', 'LIBID', 'DEL', 'EXT', 'DATE', 'LANG',
              'LIBRATE', 'KEYWORDS']

    def __init__(self):
        self._params = None

    @property
    def author(self):
        if self._params is None:
            return None
        return self._params["AUTHOR"]

    @property
    def genre(self):
        if self._params is None:
            return None
        return self._params["GENRE"]

    @property
    def title(self):
        if self._params is None:
            return None
        return self._params["TITLE"]

    @property
    def series(self):
        if self._params is None:
            return None
        return self._params["SERIES"]

    @property
    def serno(self):
        if self._params is None:
            return None
        return self._params["SERNO"]

    @property
    def file(self):
        if self._params is None:
            return None
        return self._params["FILE"]

    @property
    def size(self):
        if self._params is None:
            return None
        return self._params["SIZE"]

    @property
    def libid(self):
        if self._params is None:
            return None
        return self._params["LIBID"]

    @property
    def deleted(self):
        if self._params is None:
            return None
        return self._params["DEL"]

    @property
    def ext(self):
        if self._params is None:
            return None
        return self._params["EXT"]

    @property
    def date(self):
        if self._params is None:
            return None
        return self._params["DATE"]

    @property
    def lang(self):
        if self._params is None:
            return None
        return self._params["LANG"]

    @property
    def librate(self):
        if self._params is None:
            return None
        return self._params["LIBRATE"]

    @property
    def keywords(self):
        if self._params is None:
            return None
        return self._params["KEYWORDS"]

    def load_from_line(self, line):
        if line is None or len(line) == 0:
            return
        tmp_arr = [field.decode('utf8') if len(field) > 0 else None for field in line.split(chr(0x04))]
        self._params = dict(zip(self.fields, tmp_arr))

    def load_from_row(self, row):
        if row is None:
            return
        self._params = row

    @property
    def path(self):
        if self._params is None:
            return None
        return self._params["PATH"]

    @path.setter
    def path(self, path):
        if self._params is None:
            return
        self._params["PATH"] = path

    @property
    def bid(self):
        if self._params is None:
            return None
        return self._params["BID"]

    @bid.setter
    def bid(self, bid):
        if self._params is None:
            return
        self._params["BID"] = bid

    @property
    def file_name(self):
        if self.file is None or self.ext is None:
            return ""
        return "{0}.{1}".format(self.file, self.ext)

    @property
    def zip_file_name(self):
        if len(self.file_name) == 0:
            return ""
        return "{0}.{1}".format(self.file_name, "zip")

    @property
    def params(self):
        if self._params is None:
            return None
        return (
        self.author, self.genre, self.title, self.series, self.serno, self.file, self.size, self.libid, self.deleted,
        self.ext, self.date, self.lang, self.librate, self.keywords, self.path)
