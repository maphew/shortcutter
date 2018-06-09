import os
from os import path as p
import sys
import site
import stat
from .base import ShortCutter

ACTIVATE = """#!/bin/sh
source "{activate}"
"{executable}" "$@"
"{deactivate}"

"""


class ShortCutterLinux(ShortCutter):
    @staticmethod
    def _get_desktop_folder():
        import subprocess
        try:
            return subprocess.check_output(['xdg-user-dir',
                                            'DESKTOP']).decode('utf-8').strip()
        except subprocess.CalledProcessError:
            return p.join(p.expanduser('~'), 'Desktop')

    @staticmethod
    def _get_menu_folder():
        return p.join(p.expanduser('~'), '.local', 'share', 'applications')

    @staticmethod
    def _get_bin_folder():
        return p.dirname(sys.executable)

    @staticmethod
    def _get_local_root():
        return p.dirname(p.dirname(sys.executable))

    @staticmethod
    def _get_site_packages():
        return site.getsitepackages()[0]

    @staticmethod
    def _get_activate_wrapper_template():
        return ACTIVATE

    @staticmethod
    def _create_shortcut_to_dir(shortcut_name, target_path, shortcut_directory):
        """
        Creates a Unix shortcut to a directory via symbolic link.

        Returns tuple (shortcut_name, target_path, shortcut_file_path)
        """
        shortcut_file_path = p.join(shortcut_directory, shortcut_name)
        if p.islink(shortcut_file_path):
            os.remove(shortcut_file_path)
        os.symlink(target_path, shortcut_file_path)
        return shortcut_name, target_path, shortcut_file_path

    @staticmethod
    def _create_shortcut_file(shortcut_name, target_path, shortcut_directory):
        """
        Creates a Linux shortcut file.

        Returns tuple (shortcut_name, target_path, shortcut_file_path)
        """
        shortcut_file_path = p.join(shortcut_directory, "launch_" + shortcut_name + ".desktop")
        with open(shortcut_file_path, "w") as shortcut:
            shortcut.write("[Desktop Entry]\n")
            shortcut.write("Name={}\n".format(shortcut_name))
            shortcut.write("Exec={} %F\n".format(target_path))
            shortcut.write("Terminal=true\n")
            shortcut.write("Type=Application\n")

            # make the launch file executable
            st = os.stat(shortcut_file_path)
            os.chmod(shortcut_file_path, st.st_mode | stat.S_IEXEC)

        return shortcut_name, target_path, shortcut_file_path

    def _is_file_the_target(self, target, file_name, file_path):
        match = False
        if file_name == target:
            # is the file executable
            if os.access(file_path, os.X_OK):
                match = True
            else:
                match = False
        return match

    @staticmethod
    def _get_paths():
        """
        Gets paths from the PATH environment variable and
        prepends the `<Python>/bin` directory.

        Returns a list of paths.
        """
        return [p.dirname(sys.executable)] + os.environ['PATH'].split(os.pathsep)
