# -*- coding: utf-8 -*-
# @author: liangzhi, 2019/10/10
import re
import os
from pathlib import Path


class FilesReader(object):
    '''
    Read all files from path,every file end with end_type.
    this class can replace some str of all the files in a path.
    '''

    def __init__(self, path="defult", end_type=[".cpt"]):
        self.end_type = end_type
        if path == "defult":
            self.path = os.getcwd()
        else:
            self.path = path
        self.fileList = []
        self.fileNumber = 0
        self._CreatFileList()

    def __repr__(self):
        return 'FilesReader(path={0.path!s})'.format(self)

    def _CreatFileList(self):
        p = Path(self.path)
        for e_t in self.end_type:
            self.fileList.extend(list(p.glob("**/*" + e_t)))
        self.fileNumber = len(self.fileList)

    @property
    def files(self):
        return [os.path.relpath(f) for f in self.fileList]

    def file_replace(self, file_name, old_str, new_str, is_right_link=True):
        """
        替换文件中的字符串
        :param file:文件名
        :param old_str:old字符串
        :param new_str:新字符串
        """
        if is_right_link:
            r_str = ''
        else:
            r_str = '\s'
        file_data = ""
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.read()
            str_at = lines.find(old_str)
            reg = re.compile(re.escape(old_str) + r_str, re.IGNORECASE)
            if len(reg.findall(lines)) != 0:
                str_at = reg.findall(lines)
                new_lines = reg.sub(new_str, lines)
                file_data += new_lines
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(file_data)
            else:
                str_at = None
            return_num = str_at
        return return_num

    def replace_in_path(self, old_str, new_str, is_right_link=True):
        for file in self.fileList:
            find_str = self.file_replace(file, old_str, new_str, is_right_link=True)
            if find_str != None:
                print("replace:%(file_name)s with: %(re_str)s"
                      % {'file_name': os.path.relpath(file), 're_str': find_str})


class FoldersReader(object):
    '''
    path: the path of the folders at
    sel: the list of folders' name you want to select
    end_type: the type of files you want to replace,input a list of them
    '''

    def __init__(self, path, sel=[], end_type=[".cpt"]):
        self.path = path
        self.sel = sel
        self.end_type = end_type
        self.folders = [os.path.relpath(i) for i in os.listdir(self.path) if os.path.relpath(i) in sel]

    def replace_in_path(self, old_str, new_str):
        for folder in self.folders:
            _reaader = FilesReader(self.path + '/' + folder, self.end_type)
            _reaader.replace_in_path(old_str, new_str)
