# this file is ignored by the .gitignore to allow for param changes without repo update

import os

def abs_path(in_path):
    return os.path.abspath(in_path)

# if true, print error to console instead of raising exception
#    this is preferable in production because a raised exception will close the terminal if the script was run from a double click
IS_PRODUCTION = True


#################################################
# App Params
#################################################

# path to top level file relative to this file
# if this file is not a .pyw, it will bring up a terminal when run
TOP_LEVEL_FILE__PATH = abs_path('..//..//src//main.pyw') 

# None for default python icon, must be .ico
ICON__PATH           = abs_path('..//imgs//icon.ico')             

# None for pwd      
APP_DIR__PATH        = abs_path('..//..//app')                  
             
# can be paths to dirs or individual files
# leave list empty to not copy anything extra into the dist dir
COPY_INTO_DIST__INCLUDE_PATHS_L = [abs_path('..//..//src'),
                                   abs_path('..//..//app_update')] 


# to exclude from any dir in COPY_INTO_DIST__INCLUDE_PATHS_L
#    possible remove modes:  
#                            'basename_equals'
#                            'in_basename'      -- NOT IMPLEMENTED
#                            'paths_equal'
#                            'in_path'          -- NOT IMPLEMENTED
#                            'starts_with'
#                            'is_component_name'
#
#        see path_l_remove() in file_system_utils for implemented / not implemented
#
# if COPY_INTO_DIST__INCLUDE_PATHS_L == [], this will be ignored 
COPY_INTO_DIST__EXCLUDE_PATHS_LD = {
                                        'is_component_name' : ['.git', '__pycache__'],
                                        'starts_with'     : [abs_path(APP_DIR__PATH)]
                                    }


#################################################
# Shortcut Params
#################################################

ADD_SHORTCUT = True

# must end in .lnk but will not show
# can contain spaces
SHORTCUT_DEST_PATH = abs_path('..//..//Sourcetree_Add_Remote_Name_To_Clone_Path.lnk')

SHORTCUT_WORKING_DIR_PATH = None


#################################################
#  Probably Shouldn't Change
#################################################

# set to True to see what cmd will be executed
DRY_RUN = False 

# delete the PYCACHE that pyinstaller creates
DELETE_PYCACHE = True

DIST_DIR_PATH  = APP_DIR__PATH + '\\dist'
BUILD_DIR_PATH = APP_DIR__PATH + '\\build'





if __name__ == '__main__':
    import update_app
    update_app.main()