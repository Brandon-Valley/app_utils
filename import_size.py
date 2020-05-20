import os
from usms.file_system_utils import file_system_utils as fsu
import subprocess


i_str_l =     [
        "import tkinter                        ",
        "import ntpath                         ",
        "from pynput.keyboard import Controller",
#         "import simplejson                     ",
#         "from operator import methodcaller     ",
#         "import tkinter.ttk                    ",
#         "from pynput.keyboard import Listener  ",
#         "import _tkinter                       ",
#         "from datetime import datetime         ",
#         "from subprocess import PIPE           ",
#         "from tkinter import filedialog        ",
#         "import uuid                           ",
#         "import ctypes                         ",
#         "import json                           ",
#         "import pyperclip                      ",
#         "from dateutil.parser import parse     ",
#         "import unittest                       ",
#         "from tkinter import *                 ",
#         "from setuptools import setup          ",
#         "import six                            ",
#         "import shutil                         ",
#         "from os import listdir                ",
#         "import traceback                      ",
#         "import glob                           ",
#         "import sys                            ",
#         "from fractions import Fraction        ",
#         "import subprocess                     ",
#         "from tkinter.ttk import *             ",
#         "from ctypes import windll             ",
#         "from pynput.keyboard import Key       ",
#         "import keyboard                       ",
#         "import stat                           ",
#         "from functools import wraps           ",
#         "import time                           ",
#         "import math                           ",
#         "from pynput import keyboard           ",
#         "import csv                            ",
#         "import threading                      ",
#         "from func_timeout import func_timeout ",
#         "from decimal import Decimal           ",
#         "import argparse                       ",
#         "from operator import attrgetter       ",
#         "import os                             ",
#         "from collections import namedtuple    ",
#         "import textwrap                       ",
#         "import string                         "
    ]


PY_TEST_DIR_PATH = os.path.abspath('i_test_dir')
PY_TEST_FILE_NAME = 'i_test.py'
PY_TEST_PATH = PY_TEST_DIR_PATH + '//' + PY_TEST_FILE_NAME
SORTED_STR_L_DELIM = '  :  '




def get_size(start_path = '.'):
    def bytes_to_megabytes(i):
        return i / 1000000
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return bytes_to_megabytes(total_size)


# print(bytes_to_megabytes(get_size("C:\\Users\\mt204e\\Documents\\test\\pyinstaller_tests\\size_test_1")))


def write(lines, filePath, write_mode = 'overwrite'):
    fsu.make_file_if_not_exist(filePath)
    
    # convert to str
    if type(lines) == list or type(lines) == tuple:
        str_converted_lines = []
        for line in lines:
            str_converted_lines.append(str(line))
    else:
        str_converted_lines = [str(lines)]
    
    # write lines to file
    if   write_mode == 'overwrite':
        writeFile = open(filePath, "w") 
    elif write_mode == 'append':
        writeFile = open(filePath, "a")

    for line_num, line in enumerate(str_converted_lines):
        writeFile.write(line)
        
        # do not write newline if you just wrote the last line
        if line_num != len(str_converted_lines) - 1:
            writeFile.write('\n')
 
    writeFile.close() #to change file access modes 
    
    
    
def json_write(data, output_file_path, indent = 4):
    fsu.make_file_if_not_exist(output_file_path)
     
    with open(output_file_path, 'w') as outfile:  
        json.dump(data, outfile, indent = indent)
        outfile.close()
 
 
 
def json_read(json_file_path, return_if_file_not_found = "raise_exception"):
    try:
        with open(json_file_path, "r") as read_file:
            data = json.load(read_file)           
        read_file.close()
    except FileNotFoundError as e:
        if return_if_file_not_found != "raise_exception":
            return return_if_file_not_found
        else:
            raise e
        
    return data    
    
    


def size_d_to_sorted_str_l(size_d):
    sorted_str_l = []
    
    sorted_key_l = reversed(sorted(size_d, key=lambda i: int(size_d[i])))
    
    for key in sorted_key_l:
        size_str = key + SORTED_STR_L_DELIM + str(size_d[key])
#         print(size_str)
        sorted_str_l.append(size_str)
    return sorted_str_l
        
 
def l_print(in_l):
    for e in in_l:
        print(e)
 
 
local_size_d = {}
   
og_script_dir_path = os.path.abspath(os.path.dirname(__file__))
   
for i_str in i_str_l:
    i_str_stripped = i_str.strip()
       
       
    fsu.delete_if_exists(PY_TEST_DIR_PATH)
    write([i_str], PY_TEST_PATH)
    os.chdir(PY_TEST_DIR_PATH)
       
    cmd = 'pyinstaller ' + PY_TEST_FILE_NAME
    subprocess.call(cmd, shell = True)
   
    app_size = get_size(PY_TEST_DIR_PATH)
    print(i_str_stripped, ': ', app_size)
    local_size_d[i_str_stripped] = app_size
       
    os.chdir(og_script_dir_path)
    
    
local_sorted_size_str_l = size_d_to_sorted_str_l(local_size_d)
print(local_sorted_size_str_l)
print('local_sorted_size_str_l:')
l_print(local_sorted_size_str_l)
    
#  
# 
# 
# local_sorted_dl
#  
#  
# print(sorted(d, key=lambda i: int(d[i])))


# size_d = {'a': 50, 'b': 89, 'c': 110, '57482': 18, '57485': 82, '57484': 40}  
# 
# print(size_d_to_sorted_str_l(size_d))

























