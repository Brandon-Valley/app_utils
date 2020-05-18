# this file is ignored by the .gitignore to allow for param changes without repo update

import os

# define everything as an abs path based on a relative path to this file so
# this file can move in relation to update_app.py
# NOT TESTED IF THIS GIVES PATH RELATIVE TO THIS FILE OR __main__
def abs_path(in_path):
    return os.path.abspath(in_path)

# path to top level file relative to this file
TOP_LEVEL_FILE__REL_PATH = abs_path('..//main.py') 

# None for default python icon, must be .ico
ICON__REL_PATH           = None             

# None for pwd      
APP_DIR__REL_PATH        = abs_path('..//app')                  
             
# can be paths to dirs or individual files
# leave list empty to not copy anything extra into the dist dir
COPY_INTO_DIST__INCLUDE_PATHS_L = [abs_path('..')] 


# to exclude from any dir in COPY_INTO_DIST__INCLUDE_PATHS_L
#    possible remove modes:  
#                            'basename_equals'
#                            'in_basename'      -- NOT IMPLEMENTED
#                            'paths_equal'
#                            'in_path'          -- NOT IMPLEMENTED
#
#        see path_l_remove() in file_system_utils for implemented / not implemented
#
# if COPY_INTO_DIST__INCLUDE_PATHS_L == [], this will be ignored 
COPY_INTO_DIST__EXCLUDE_PATHS_LD = {
                                        'basename_equals' : ['.git', '__pycache__'],
                                        'paths_equal'     : [abs_path(APP_DIR__REL_PATH)]
                                    }


# set to True to see what cmd will be executed
DRY_RUN = False 

# delete the PYCACHE that pyinstaller creates
DELETE_PYCACHE = True






if __name__ == '__main__':
    import update_app
    update_app.main()