import os         
import shutil
import subprocess             

from usms.file_system_utils import file_system_utils as fsu

import update_app_params as uap


# uap.TOP_LEVEL_FILE__REL_PATH = 'main.py' 
# uap.ICON__REL_PATH           = None                   # None for default python icon, must be .ico
# uap.APP_DIR__REL_PATH        = 'app'                  # None for pwd
#              
# uap.DRY_RUN = False # set to True to see what cmd will be executed
# uap.DELETE_PYCACHE = True
# COPY_INTO_DIST__INCLUDE_PATHS_L = ['..'] 
# 
# 
# # to exclude from any dir in COPY_INTO_DIST__INCLUDE_PATHS_L
# #    possible remove modes:  
# #                            'basename_equals'
# #                            'in_basename'      -- NOT IMPLEMENTED
# #                            'paths_equal'
# #                            'in_path'          -- NOT IMPLEMENTED
# #
# #        see path_l_remove() in file_system_utils for implemented / not implemented
# #
# # if COPY_INTO_DIST__INCLUDE_PATHS_L == [], this will be ignored 
# COPY_INTO_DIST__EXCLUDE_PATHS_LD = {'basename_equals' : ['.git', '__pycache__'],
#                                     'paths_equal'     : [APP_DIR__REL_PATH]}










def build_cmd():
    cmd = 'pyinstaller '
    cmd +='  {} '                        .format(uap.TOP_LEVEL_FILE__REL_PATH)
    cmd +=' --clean '
        
    
    if uap.APP_DIR__REL_PATH != None:    
        cmd +='  --specpath="{}" '       .format(uap.APP_DIR__REL_PATH)
        cmd +='  --distpath="{}//dist" ' .format(uap.APP_DIR__REL_PATH)
        cmd +='  --workpath="{}//build" '.format(uap.APP_DIR__REL_PATH)
            
    if uap.ICON__REL_PATH != None:
        icon_abs_path = os.path.dirname(os.path.abspath(__file__)) + '//' + uap.ICON__REL_PATH
        cmd +=' --icon="{}" '           .format(icon_abs_path)               
        cmd +=' --icon="{}" '           .format(uap.ICON__REL_PATH)   
        cmd +=' --add_data img//icon.png '             
        cmd +=' --one-dir '             
             
    return cmd



def copy_files_to_dist_dir():
#     root_abs_path__abs_and_rel_paths_to_copy_ld = {}
        
    print('uap.COPY_INTO_DIST__INCLUDE_PATHS_L: ', uap.COPY_INTO_DIST__INCLUDE_PATHS_L)#`````````````````````````````````````````````````````````
        
    # build init root_abs_path__rel_paths_to_copy_ld before trimming
    for root_abs_path in uap.COPY_INTO_DIST__INCLUDE_PATHS_L:        
        abs_path_l = fsu.get_dir_content_l(root_abs_path, object_type = 'all', content_type = 'abs_path', recurs_dirs = True, rel_to_path = root_abs_path)
#         root_abs_path__abs_and_rel_paths_to_copy_ld[root_abs_path] = abs_path_l
        print(abs_path_l)
        
        
#     print(root_abs_path__abs_and_rel_paths_to_copy_ld.keys(), root_abs_path__abs_and_rel_paths_to_copy_ld)#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
    
        # trim
        trimmed_abs_path_l = abs_path_l
        for removal_mode, to_remove_str_or_l in uap.COPY_INTO_DIST__EXCLUDE_PATHS_LD.items():
            trimmed_abs_path_l = fsu.path_l_remove(trimmed_abs_path_l, to_remove_str_or_l, removal_mode)
             
            print('removal_mode, to_remove_str_or_l:  ', removal_mode, to_remove_str_or_l)#`1```````````````````````````````````````````````````````
            print(trimmed_abs_path_l)#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
            
        print('done with trim !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # copy over each file / dir without contents to avoid including a trimmed path while not loosing empty dirs
        for abs_path in trimmed_abs_path_l:
            rel_to_root_path = fsu.get_rel_path_from_compare(abs_path, root_abs_path)
            print(rel_to_root_path)
        
        
        
# 
#         
#     for abs_path in paths_to_copy_l:
#         
        
        
        
        

def main(): 
    cmd = build_cmd()
    print(cmd)
    
    if not uap.DRY_RUN:
        
        if uap.APP_DIR__REL_PATH != None:
            try:
                fsu.delete_if_exists(uap.APP_DIR__REL_PATH)
            except OSError:
                fsu.delete_if_exists(uap.APP_DIR__REL_PATH) 
            
        subprocess.call(cmd, shell = True)
        
    if uap.DELETE_PYCACHE:
        fsu.delete_if_exists('__pycache__')

    i = input('\nPress any key to continue')
    




if __name__ == '__main__':
#     main()       
    copy_files_to_dist_dir()
