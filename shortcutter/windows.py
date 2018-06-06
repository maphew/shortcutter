# import win32com
# this often fails due to unable to find DLLs
# so dynamically change the path if required
try:
    import win32com
except ImportError as e:
    if "DLL load failed:" in str(e):
        import os
        import sys
        path = os.path.join(os.path.split(sys.executable)[0], "Lib", "site-packages", "pywin32_system32")
        os.environ["PATH"] = os.environ["PATH"] + ";" + path
        try:
            import win32com
        except ImportError as ee:
            dll = os.listdir(path)
            dll = [os.path.join(path, _) for _ in dll if "dll" in _]
            # TODO: Python version 2.7 does not support this syntax:
            raise ImportError("Failed to import win32com, due to missing DLL:\n" + "\n".join(dll)) from e
    else:
        raise e

import winshell
import sys
import os
from .base import ShortCutter


class ShortCutterWindows(ShortCutter):
    def _custom_init(self):
        self.executable_file_extensions = os.environ['PATHEXT'].split(os.pathsep)

    @staticmethod
    def _get_desktop_folder():
        return winshell.desktop()

    @staticmethod
    def _get_menu_folder():
        return winshell.folder("CSIDL_PROGRAMS")

    @staticmethod
    def _get_site_packages():
        return os.path.join(os.path.dirname(sys.executable), 'Lib', 'site-packages')

    @staticmethod
    def _get_bin_folder():
        return os.path.join(os.path.dirname(sys.executable), "Scripts")

    @staticmethod
    def _executable(app_name):
        return app_name + '.exe'

    @staticmethod
    def _create_shortcut_to_dir(shortcut_name, target_path, shortcut_directory):
        return ShortCutterWindows._create_shortcut_file(shortcut_name, target_path, shortcut_directory)

    @staticmethod
    def _create_shortcut_file(shortcut_name, target_path, shortcut_directory):
        """
        Creates a Windows shortcut file.

        Returns shortcut_file_path
        """
        shortcut_file_path = os.path.join(shortcut_directory, shortcut_name + ".lnk")

        winshell.CreateShortcut(
            Path=shortcut_file_path,
            Target=target_path,
            Icon=(target_path, 0),
            Description="Shortcut to" + os.path.basename(target_path),
            StartIn=target_path)

        return shortcut_file_path

    def _is_file_the_target(self, target, file_name, file_path):
        match = False
        # does the target have an extension?
        target_ext = os.path.splitext(target)[1]
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
        root = os.path.dirname(sys.executable)
        return [root,
                os.path.join(root, 'Scripts'),
                os.path.join(root, 'Library', 'bin')] + os.environ['PATH'].split(os.pathsep)
