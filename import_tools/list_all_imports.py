from usms.file_system_utils import file_system_utils as fsu

import os
import re



def read(filePath):
    with open(filePath) as textFile:  # can throw FileNotFoundError
        out =  list(l.rstrip() for l in textFile.readlines())
    textFile.close()
    return out
        
 
my_stuff_l = [ 'logger', '_utils', 'Main_Tab', '_tools', 'os.', 'sys.', "'",
                'Git_Commit',
                'Tool_Tip',
                'custom_exceptions',
                'from . ',
                'import setup_new_repo',
                'common_vars',
                'commit_log_format_strings       ',
                'RGB_Display_Entry',
                'custom_widgets',
                'jsonplus__non_merged',
                'print_function',
                'absolute_import',

                'from moneyed import USD',
                'from flask import current_app',
                'from djmoney.money import Money',
                'import FunctionTimedOut',
                'import Popen',
                'from django.conf import settings',
                'import CalledProcessError',
                'from django_jsonplus.models import JSONPlusField',
                'import join',
                
                "from moneyed import get_currency",
                "import check_call",
                "from django.apps import AppConfig",
                "from tests.models import TestModel",
                "import Currency",
                "from flask_jsonplus import FlaskJSONPlus",
                "from sortedcontainers import SortedList",
                "import jsonplus",
                "from django.test import TestCase",
                "from  custom_widgets import File_System_Browse_WG",
                "import date",
                "from django.shortcuts import render",
                "import django",
                "import jsonify",
                "import partial",
                "from django.db import models",
                "from PIC_transfer import PIC_transfer",
                "from django.test.utils import get_runner",
                "from moneyed import Money",
                "from django.contrib import admin",
                "import GUI",
                "import print_function",
                "import jsonplus__non_merged",
                "import timedelta",
                "import CurrencyDoesNotExist",
                "from django.db import connection",
                "from flask import Flask",
                "import django_jsonplus.coders"                           
            ] 
 
proj_path = "C:\\projects\\version_control_scripts\\CE\\setup_new_repo\\src"
 
all_files_abs_path_l = fsu.get_dir_content_l(proj_path, object_type = 'file', content_type = 'abs_path', recurs_dirs = True)
 
print(all_files_abs_path_l)
 
i_str_set = set()
fi_d = {}
 
for abs_file_path in all_files_abs_path_l:
    ext = fsu.get_extention(abs_file_path)
#     print(ext)
     
    
     
    if ext in ['.py', '.pyw']:
        py_basename = os.path.basename(abs_file_path)
        fi_d[py_basename] = set()
        
        lines = read(abs_file_path)
         
        for line in lines:
            if 'import' in line:
#                 ss_l = re.split(', |, |\*|\n',text)
#                 split_str_l = []
                split_srt_l = line.split(',')
                
#                 ss_str_l = []
                for s_str in split_srt_l:
                    ss_str = s_str.strip().replace('sms.', '').replace('usms.', '')
                    
                    ss_str = ss_str.split(' as ')[0]
                    
                    
                    if ss_str[0] == '.':
                        ss_str = ss_str[1:]
                    
                    non_comment_ss_str = ss_str.split('#')[0].strip()#.strip('/n')
                    
#                     while('  ' in non_comment_ss_str):
                    non_comment_ss_str = non_comment_ss_str.replace('  ', ' ')
                    
                    
#                     print('non_comment_ss_str: ', non_comment_ss_str)
#                     ss_str_l.append(non_comment_ss_str)

                    if not any(m_str in non_comment_ss_str for m_str in my_stuff_l):
                        
                        if 'import' not in non_comment_ss_str:
                            non_comment_ss_str = 'import ' + non_comment_ss_str
                                                    
                        fi_d[py_basename].add(non_comment_ss_str)
                        i_str_set.add(non_comment_ss_str)
                    

                    
                
                
for k, v in fi_d.items():
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('\n {}    {}'.format(k,v))
                    
                    
                    
                
print('-----------------------------------------------')                    
for i_str in i_str_set:
    print(i_str)
                    
print(len(i_str_set))
                        
 
 
 
 
 
# 


