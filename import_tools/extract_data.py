#!/usr/bin/env python
# coding=utf-8

import config as cfg
import zipfile
import os
import models.book_info as book_info
import models.books as books
# import pcloudservice
from tqdm import trange

books_manager = None


def parse_multiple_value(value):
    tmp_arr = [field.replace(",", " ").rstrip() if len(field) > 0 else None for field in
               value.split(":")]
    return tmp_arr


def extract_file(zip, path, filename):
    # print "extract file from zip and create new archive"
    try:
        newpath = zip.extract(filename, path)
        zipfile_path = "{0}{1}".format(newpath, ".zip")
        with zipfile.ZipFile(zipfile_path, 'w', zipfile.ZIP_DEFLATED) as myzip:
            myzip.write(newpath, filename)
        os.remove(newpath)
    except Exception as error:
        print(error)


def create_folder(filename):
    # print "create new library folder"
    newpath = "{0}/{1}".format(cfg.LIBRARY["library_files"], filename.replace(".inp", ""))
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


def find_zip(filename):
    # print "find and open zip file"
    filename = filename.replace(".inp", ".zip")
    zip_filepath = "{0}/{1}".format(cfg.LIBRARY["archives_path"], filename)
    if not os.path.exists(zip_filepath):
        return None
    return zipfile.ZipFile(zip_filepath, 'r')


def parse_inpx(inpx):
    global books_manager
    if inpx is None:
        return
    # print "parse inpx file"
    infolist = inpx.infolist()
    for i in trange(len(infolist), desc='parse inpx file'):
        inp = infolist[i]
        if inp.filename.startswith("fb2"):
            doc = inpx.read(inp.filename)
            zip = find_zip(inp.filename)
            if doc is not None and zip is not None and not books_manager.is_inp_exist(inp.filename):
                inp_id = books_manager.add_inp(inp.filename)
                path = create_folder(inp.filename)
                lines = doc.splitlines()
                for j in trange(len(lines)):
                    line = lines[j]
                    info = book_info.BookInfo()
                    info.load_from_line(line)
                    info.path = inp.filename.replace(".inp", "")
                    fnd_info = books_manager.find_by_file(info.libid, info.file)
                    if fnd_info is None or fnd_info.bid is None:
                        bid = books_manager.save_book(info)
                        if bid is not None:
                            info.bid = bid
                            extract_file(zip, path, "{0}.{1}".format(info.file, info.ext))
                            # pcloud_fi = pcloudservice.PCloudService.get_file_info(info.path, info.zip_file_name)
                            # if "error" in pcloud_fi and "result" in pcloud_fi and pcloud_fi["result"] == 2009:
                            #     extract_file(zip, path, "{0}.{1}".format(info.file, info.ext))
                            # elif "error" in pcloud_fi and "result" not in pcloud_fi:
                            #     raise Exception("Error in pCloud service")
                            # else:
                            #     pass

                    #     books_manager.update_book(info, fnd_info._bid)
                books_manager.update_inp(inp_id)
            zip.close()


def open_inpx():
    print "open inpx file"
    zip_inpx = None
    try:
        zip_inpx = zipfile.ZipFile(cfg.LIBRARY["inpx_file"], 'r')
    except:
        pass
    return zip_inpx


def start_process():
    global books_manager
    with books.Books() as books_manager:
        inpx = open_inpx()
        parse_inpx(inpx)
        if inpx:
            inpx.close()
        #   create_all_tables()
        print "end of process"


def stop_process():
    global books_manager
    books_manager.close()


if __name__ == "__main__":
    start_process()
