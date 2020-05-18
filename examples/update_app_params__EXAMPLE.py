# this file is ignored by the .gitignore to allow for param changes without repo update

TOP_LEVEL_FILE__REL_PATH = '..//main.py' 
ICON__REL_PATH           = None                   # None for default python icon, must be .ico
APP_DIR__REL_PATH        = 'app'                  # None for pwd
             
DRY_RUN = False # set to True to see what cmd will be executed
DELETE_PYCACHE = True


if __name__ == '__main__':
    import update_app
    update_app.main()