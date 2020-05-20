import os
import subprocess
import json

from i_str_l import i_str_l

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from usms.file_system_utils import file_system_utils as fsu



PY_TEST_DIR_PATH = os.path.abspath('i_test_dir')
PY_TEST_FILE_NAME = 'i_test.py'
PY_TEST_PATH = PY_TEST_DIR_PATH + '//' + PY_TEST_FILE_NAME
SORTED_STR_L_DELIM = '  :  '
SORTED_STR_L_JSON_PATH = 'sorted_import_sizes.json'
ADJ_SORTED_STR_L_JSON_PATH = 'adj_sorted_import_sizes.json'
NUM_DECIMAL_DIGITS = 1

OVERWRITE_MASTER_SIZES = False


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

    return round(bytes_to_megabytes(total_size), NUM_DECIMAL_DIGITS)



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
    
    sorted_key_l = reversed(sorted(size_d, key=lambda i: float(size_d[i])))
    
    for key in sorted_key_l:
        size_str = key + SORTED_STR_L_DELIM + str(size_d[key])
        sorted_str_l.append(size_str)
    return sorted_str_l



def size_d_to_adjusted_size_d(size_d, master_size_d = None):
    if master_size_d == None:
        sorted_key_l = sorted(size_d, key=lambda i: float(size_d[i]))
        lowest_key = sorted_key_l[0]
        smallest_size = size_d[lowest_key]
    else:
        sorted_key_l = sorted(master_size_d, key=lambda i: float(master_size_d[i]))
        lowest_key = sorted_key_l[0]
        smallest_size = master_size_d[lowest_key]
        
    adjusted_size_d = {}
    for k, v in size_d.items():
        adjusted_size_d[k] = round(v - smallest_size, NUM_DECIMAL_DIGITS)
        
    return adjusted_size_d
    


def sorted_str_l_to_size_d(sorted_str_l):
    size_d = {}
    
    for size_str in sorted_str_l:
        kv = size_str.split(SORTED_STR_L_DELIM)
        size_d[kv[0]] = float(kv[1])
    return size_d
    
    
 
def l_print(in_l):
    for e in in_l:
        print('  ', e)
        
        
        
        
try:        
    master_size_d = sorted_str_l_to_size_d(json_read(SORTED_STR_L_JSON_PATH, return_if_file_not_found = []))
except json.decoder.JSONDecodeError:
    master_size_d = {}
 
local_size_d = {}
   
og_script_dir_path = os.path.abspath(os.path.dirname(__file__))
   
for i_str in i_str_l:
    i_str = i_str.strip()
        
    if not OVERWRITE_MASTER_SIZES and i_str in master_size_d.keys():
        print('\nSkipping import because size already known:  {} : {}'.format(i_str, master_size_d[i_str]))
        
    else:
        fsu.delete_if_exists(PY_TEST_DIR_PATH)
        write([i_str], PY_TEST_PATH)
        os.chdir(PY_TEST_DIR_PATH)
           
        cmd = 'pyinstaller ' + PY_TEST_FILE_NAME
        subprocess.call(cmd, shell = True)
       
        app_size = get_size(PY_TEST_DIR_PATH)
        print(i_str, ': ', app_size)
        
        local_size_d[i_str] = app_size
        master_size_d[i_str] = app_size
           
        os.chdir(og_script_dir_path)
        
        # so you stop committing apps
        fsu.delete_if_exists(PY_TEST_DIR_PATH)
    
    

# result print
print('-------------------------------------------------------')
master_sorted_size_l = size_d_to_sorted_str_l(master_size_d)
print('\nmaster_sorted_size_l')
l_print(master_sorted_size_l)


print('-------------------------------------------------------')
adj_master_size_d = size_d_to_adjusted_size_d(master_size_d)
adj_master_size_str_l = size_d_to_sorted_str_l(adj_master_size_d)
print('\nadj_master_size_str_l:')
l_print(adj_master_size_str_l)

print('-------------------------------------------------------')
local_sorted_size_str_l = size_d_to_sorted_str_l(local_size_d)
print('\nlocal_sorted_size_str_l:')
l_print(local_sorted_size_str_l)



json_write(master_sorted_size_l, SORTED_STR_L_JSON_PATH)
json_write(adj_master_size_str_l, ADJ_SORTED_STR_L_JSON_PATH)


# td = sorted_str_l_to_size_d(local_sorted_size_str_l)
# print(td)


    
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

























