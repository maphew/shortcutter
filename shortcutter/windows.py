import sys
import os
from os import path as p
# import win32com
# this often fails due to unable to find DLLs
# so dynamically change the path if required
try:
    import win32com
except ImportError as e:
    if "DLL load failed:" in str(e):
        path = p.join(p.split(sys.executable)[0], "Lib", "site-packages", "pywin32_system32")
        os.environ["PATH"] = os.environ["PATH"] + ";" + path
        try:
            import win32com
        except ImportError as ee:
            dll = os.listdir(path)
            dll = [p.join(path, _) for _ in dll if "dll" in _]
            # TODO: Python version 2.7 does not support this syntax:
            raise ImportError("Failed to import win32com, due to missing DLL:\n" + "\n".join(dll)) from e
    else:
        raise e

from win32com.client import Dispatch
from .base import ShortCutter

shell = Dispatch('WScript.Shell')

ACTIVATE = r"""@echo off
call "{activate}"
chcp 65001 > NUL
set "PYTHONIOENCODING=utf-8"
"{executable}" %*
call "{bin}\deactivate.bat"
"""

ACTIVATE_PROMPT = """@echo off
set "PATH={bin};%PATH%"
call "{activate}"
chcp 65001 > NUL
set "PYTHONIOENCODING=utf-8"
cd %USERPROFILE%
cmd /k
"""

FOLDER_SHORTCUT = """@echo off
cd /d "{path}"
start .
"""


class ShortCutterWindows(ShortCutter):
    def _set_win_vars(self):
        self._executable_file_extensions = [ext.upper() for ext in os.environ['PATHEXT'].split(os.pathsep)]
        cmd = self.find_target('cmd')
        self._exe_icon_app_path = cmd if cmd else sys.executable
        explorer = self.find_target('explorer')
        self._dir_icon_app_path = explorer if explorer else sys.executable

    @staticmethod
    def _get_desktop_folder():
        return shell.SpecialFolders("Desktop")

    @staticmethod
    def _get_menu_folder():
        return shell.SpecialFolders("Programs")

    @staticmethod
    def _get_bin_folder():
        return p.join(p.dirname(sys.executable), "Scripts")

    @staticmethod
    def _get_local_root():
        return p.dirname(sys.executable)

    @staticmethod
    def _get_site_packages():
        return p.join(p.dirname(sys.executable), 'Lib', 'site-packages')

    @staticmethod
    def _get_activate_wrapper_templates():
        return ACTIVATE, ACTIVATE_PROMPT

    @staticmethod
    def _make_executable(file_path):
        pass

    def _create_shortcut_to_dir(self, shortcut_name, target_path, shortcut_directory):
        return self._create_shortcut_win(shortcut_name, target_path, shortcut_directory, True)

    def _create_shortcut_file(self, shortcut_name, target_path, shortcut_directory):
        return self._create_shortcut_win(shortcut_name, target_path, shortcut_directory)

    def _create_shortcut_win(self, shortcut_name, target_path, shortcut_directory, dir_=False):
        """
        Creates a Windows shortcut file.

        Returns tuple (shortcut_name, target_path, shortcut_file_path)
        """
        working_directory = target_path if dir_ else p.dirname(target_path)
        dir_bat = False
        if dir_ and not p.exists(target_path):
            # create bat that opens dir:
            wrapper_path = p.join(self.bin_folder, self.sh('shortcutter__' + shortcut_name + '__folder'))
            with open(wrapper_path, 'w') as f:
                f.write(FOLDER_SHORTCUT.format(path=target_path))
            dir_bat = True 

        shortcut_file_path = p.join(shortcut_directory, shortcut_name + ".lnk")

        shortcut = shell.CreateShortCut(shortcut_file_path)
        shortcut.Targetpath = target_path
        shortcut.WorkingDirectory = working_directory
        shortcut.Description = "Shortcut to" + p.basename(target_path)
        if not dir_:
            ext = p.splitext(target_path)[1].upper()
            # is the file executable?
            if ext in self._executable_file_extensions:
                shortcut.IconLocation = "{},0".format(self._exe_icon_app_path)
        elif dir_bat:
            shortcut.IconLocation = "{},0".format(self._dir_icon_app_path)
        shortcut.save()

        return shortcut_name, target_path, shortcut_file_path

    def _is_file_the_target(self, target, file_name, file_path):
        match = False
        # does the target have an extension?
        target_ext = p.splitext(target)[1]
        # if so, do a direct match
        if target_ext:
            if file_name.lower() == target.lower():
                match = True
        # no extension, compare the target to the file_name for each executable file extension
        else:
            for extension in self._executable_file_extensions:
                if file_name.lower() == (target + extension).lower():
                    match = True
        return match

    @staticmethod
    def _get_paths():
        """
        Gets paths from the PATH environment variable and 
        prepends `<Python>`, `<Python>\Scripts`, `<Python>\Library\bin` directories.

        Returns a list of paths.
        """
        root = p.dirname(sys.executable)
        return [root,
                p.join(root, 'Scripts'),
                p.join(root, 'Library', 'bin')] + os.environ['PATH'].split(os.pathsep)
