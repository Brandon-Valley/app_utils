import os
from usms.file_system_utils import file_system_utils as fsu



i_str_l =     [
        "import tkinter                        ",
        "import ntpath                         ",
        "from pynput.keyboard import Controller",
        "import simplejson                     ",
        "from operator import methodcaller     ",
        "import tkinter.ttk                    ",
        "from pynput.keyboard import Listener  ",
        "import _tkinter                       ",
        "from datetime import datetime         ",
        "from subprocess import PIPE           ",
        "from tkinter import filedialog        ",
        "import uuid                           ",
        "import ctypes                         ",
        "import json                           ",
        "import pyperclip                      ",
        "from dateutil.parser import parse     ",
        "import unittest                       ",
        "from tkinter import *                 ",
        "from setuptools import setup          ",
        "import six                            ",
        "import shutil                         ",
        "from os import listdir                ",
        "import traceback                      ",
        "import glob                           ",
        "import sys                            ",
        "from fractions import Fraction        ",
        "import subprocess                     ",
        "from tkinter.ttk import *             ",
        "from ctypes import windll             ",
        "from pynput.keyboard import Key       ",
        "import keyboard                       ",
        "import stat                           ",
        "from functools import wraps           ",
        "import time                           ",
        "import math                           ",
        "from pynput import keyboard           ",
        "import csv                            ",
        "import threading                      ",
        "from func_timeout import func_timeout ",
        "from decimal import Decimal           ",
        "import argparse                       ",
        "from operator import attrgetter       ",
        "import os                             ",
        "from collections import namedtuple    ",
        "import textwrap                       ",
        "import string                         "
    ]


PY_TEST_DIR_PATH = os.path.abspath('i_test_dir')
PY_TEST_FILE_NAME = 'i_test.py'
PY_TEST_PATH = PY_TEST_DIR_PATH + '//' + PY_TEST_FILE_NAME



def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

print(get_size() / 1000, 'bytes')

print(get_size("C:\\Users\\mt204e\\Documents\\test\\pyinstaller_tests\\size_test_1") / 1000000)


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





for i_str in i_str_l:
    fsu.delete_if_exists(PY_TEST_DIR_PATH)
    write([i_str], PY_TEST_PATH)
    os.chdir(PY_TEST_PATH)


































