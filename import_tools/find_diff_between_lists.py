# how to use:
#    list_all_imports > get list > save as list_all_imports_l
#    paste list into empty py file
#    try to run
#        if run fails, delete import responsible
#        repeat until run succeeds
#    paste remaining imports into working_import_str_l
#    paste result into i_str_l to list_all_imports_l to not deal with it in the future

list_all_imports_l = [
    "import tkinter                                   ",
    "import ntpath                                    ",
    "from pynput.keyboard import Controller           ",
    "import simplejson                                ",
    "from operator import methodcaller                ",
    "import tkinter.ttk                               ",
    "from pynput.keyboard import Listener             ",
    "import _tkinter                                  ",
    "from datetime import datetime                    ",
    "from moneyed import get_currency                 ",
    "from subprocess import PIPE                      ",
    "from tkinter import filedialog                   ",
    "import uuid                                      ",
    "import ctypes                                    ",
    "import json                                      ",
    "import pyperclip                                 ",
    "from dateutil.parser import parse                ",
    "import unittest                                  ",
    "from tkinter import *                            ",
    "import check_call                                ",
    "from django.apps import AppConfig                ",
    "from tests.models import TestModel               ",
    "import Currency                                  ",
    "from flask_jsonplus import FlaskJSONPlus         ",
    "from setuptools import setup                     ",
    "from sortedcontainers import SortedList          ",
    "import jsonplus                                  ",
    "import six                                       ",
    "import shutil                                    ",
    "from django.test import TestCase                 ",
    "from  custom_widgets import File_System_Browse_WG",
    "import date                                      ",
    "from django.shortcuts import render              ",
    "from os import listdir                           ",
    "import django                                    ",
    "import traceback                                 ",
    "import jsonify                                   ",
    "import glob                                      ",
    "import sys                                       ",
    "from fractions import Fraction                   ",
    "import subprocess                                ",
    "from tkinter.ttk import *                        ",
    "from ctypes import windll                        ",
    "from pynput.keyboard import Key                  ",
    "import partial                                   ",
    "from django.db import models                     ",
    "from PIC_transfer import PIC_transfer            ",
    "import keyboard                                  ",
    "import stat                                      ",
    "from functools import wraps                      ",
    "from django.test.utils import get_runner         ",
    "import time                                      ",
    "import math                                      ",
    "from pynput import keyboard                      ",
    "from moneyed import Money                        ",
    "import csv                                       ",
    "from django.contrib import admin                 ",
    "import threading                                 ",
    "import GUI                                       ",
    "import print_function                            ",
    "from func_timeout import func_timeout            ",
    "from decimal import Decimal                      ",
    "import argparse                                  ",
    "from operator import attrgetter                  ",
    "import jsonplus__non_merged                      ",
    "import os                                        ",
    "import timedelta                                 ",
    "import CurrencyDoesNotExist                      ",
    "from collections import namedtuple               ",
    "import textwrap                                  ",
    "from django.db import connection                 ",
    "import string                                    ",
    "from flask import Flask                          ",
    "import django_jsonplus.coders                    "  
    ]


working_import_str_l = [
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




s__working_import_str_l = [s.strip() for s in working_import_str_l]
s__list_all_imports_l   = [s.strip() for s in list_all_imports_l]
# print(s__working_import_str_l)

diff_l = []

for s in s__list_all_imports_l:
    if s not in s__working_import_str_l:
        diff_l.append(s)

for s in diff_l:
    print('"{}",'.format(s))














