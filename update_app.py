import os         
import subprocess 
import winshell
from win32com.client import Dispatch            

from usms.file_system_utils import file_system_utils as fsu

import update_app_params as uap



def build_cmd():
    cmd = 'pyinstaller '
    cmd +='  {} '                        .format(uap.TOP_LEVEL_FILE__PATH)
    cmd +=' --clean '
        
    
    if uap.APP_DIR__PATH != None:    
        cmd +='  --specpath="{}" '       .format(uap.APP_DIR__PATH)
        cmd +='  --distpath="{}" '       .format(uap.DIST_DIR_PATH)
        cmd +='  --workpath="{}" '       .format(uap.BUILD_DIR_PATH)
            
    if uap.ICON__PATH != None:
        cmd +=' --icon="{}" '           .format(uap.ICON__PATH)   
             
    return cmd



def copy_files_to_dist_dir():
    top_lvl_file_basename_no_ext = fsu.get_basename_from_path(uap.TOP_LEVEL_FILE__PATH, include_ext = False)
                
    # build init root_abs_path__rel_paths_to_copy_ld before trimming
    for root_abs_path in uap.COPY_INTO_DIST__INCLUDE_PATHS_L:        
        abs_path_l = fsu.get_dir_content_l(root_abs_path, object_type = 'all', content_type = 'abs_path', recurs_dirs = True, rel_to_path = root_abs_path)
            
        # trim
        trimmed_abs_path_l = abs_path_l
        for removal_mode, to_remove_str_or_l in uap.COPY_INTO_DIST__EXCLUDE_PATHS_LD.items():
            trimmed_abs_path_l = fsu.path_l_remove(trimmed_abs_path_l, to_remove_str_or_l, removal_mode)
            
        # copy over each file / dir without contents to avoid including a trimmed path while not loosing empty dirs
        print('\n Copying over files...')
        for abs_path in trimmed_abs_path_l:
            rel_to_root_path = fsu.get_rel_path_from_compare(abs_path, root_abs_path)
            
            # build dest path
            rel_to_root_parent_dir_path = fsu.get_parent_dir_path_from_path(rel_to_root_path)
            dist_dest_abs_path = '{}//{}//{}'.format(uap.DIST_DIR_PATH, top_lvl_file_basename_no_ext, rel_to_root_parent_dir_path)
             
            fsu.copy_objects_to_dest(abs_path, dist_dest_abs_path, copy_dir_content = False)
            
            
            
def create_shortcut(dest_path, target_path, working_dir_path = None, icon_path = None):

    desktop = winshell.desktop()
    shell = Dispatch('WScript.Shell')
    
    shortcut = shell.CreateShortCut(dest_path)
    shortcut.Targetpath = target_path
    
    if working_dir_path != None:
        shortcut.WorkingDirectory = working_dir_path
        
    if icon_path != None:
        shortcut.IconLocation = icon_path
    
    
# #     path = os.path.abspath(dest_path)
#     target = target_path
# #     wDir = working_dir_path
#     icon = icon_path
#     
#     
#     shortcut.Targetpath = target
# #     shortcut.WorkingDirectory = wDir
#     shortcut.IconLocation = icon
    shortcut.save()            



def main(): 
    cmd = build_cmd()
    print(cmd)
    
    if not uap.DRY_RUN:
        
        if uap.APP_DIR__PATH != None:
            try:
                fsu.delete_if_exists(uap.APP_DIR__PATH)
            except OSError:
                fsu.delete_if_exists(uap.APP_DIR__PATH) 
            
        subprocess.call(cmd, shell = True)
        
    if uap.DELETE_PYCACHE:
        fsu.delete_if_exists('__pycache__')
        
    copy_files_to_dist_dir()

    i = input('\nPress Enter to continue')
    




if __name__ == '__main__':
#     main()       
    create_shortcut(dest_path = 'sc.lnk', target_path = "C:\\projects\\version_control_scripts\\CE\\app\\dist\\main\\main.exe", working_dir_path = None, icon_path = uap.ICON__PATH)