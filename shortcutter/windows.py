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

import winshell
from .base import ShortCutter

ACTIVATE = r"""@echo off
call "{activate}"
"{executable}" %*
"{deactivate}\deactivate.bat"
"""


class ShortCutterWindows(ShortCutter):
    def _set_exec_file_exts(self):
        self.executable_file_extensions = os.environ['PATHEXT'].split(os.pathsep)

    @staticmethod
    def _get_desktop_folder():
        return winshell.desktop()

    @staticmethod
    def _get_menu_folder():
        return winshell.folder("CSIDL_PROGRAMS")

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
    def _get_activate_wrapper_template():
        return ACTIVATE

    @staticmethod
    def _create_shortcut_to_dir(shortcut_name, target_path, shortcut_directory):
        return ShortCutterWindows._create_shortcut_file(shortcut_name, target_path, shortcut_directory)

    @staticmethod
    def _create_shortcut_file(shortcut_name, target_path, shortcut_directory):
        """
        Creates a Windows shortcut file.

        Returns tuple (shortcut_name, target_path, shortcut_file_path)
        """
        shortcut_file_path = p.join(shortcut_directory, shortcut_name + ".lnk")

        winshell.CreateShortcut(
            Path=shortcut_file_path,
            Target=target_path,
            Icon=(target_path, 0),
            Description="Shortcut to" + p.basename(target_path),
            StartIn=target_path)

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
            for extension in self.executable_file_extensions:
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
