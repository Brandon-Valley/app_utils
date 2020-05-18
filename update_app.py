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


        
# # works for single path str or list of paths
# def delete_if_exists(path_str_or_l):
#     def delete_single_fs_obj_fast(path):
#         def onerror(func, path, exc_info):
#             """
#             Error handler for ``shutil.rmtree``.
#         
#             If the error is due to an access error (read only file)
#             it attempts to add write permission and then retries.
#         
#             If the error is for another reason it re-raises the error.
#         
#             Usage : ``shutil.rmtree(path, onerror=onerror)``
#             """
#             import stat
#             if not os.access(path, os.W_OK):
#                 # Is the error an access error ?
#                 os.chmod(path, stat.S_IWUSR)
#                 func(path)
#             else:
#                 raise
#             
#         if os.path.exists(path):
#             if   os.path.isdir(path):
#                 shutil.rmtree(path, ignore_errors=False, onerror=onerror)
#             elif os.path.isfile(path):
#                 os.remove(path)
#             else:
#                 raise Exception('ERROR:  Gave something that is not a file or a dir, bad path: ', path)    
#     
#     
#     if isinstance(path_str_or_l, str):
#         path_str_or_l = [path_str_or_l]
#     
#     for path in path_str_or_l:
#         delete_single_fs_obj_fast(path)
        
        

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
    main()       
