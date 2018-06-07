import os
from os import path as p
from .exception import ShortcutError
from .linux import ShortCutterLinux
from tempfile import NamedTemporaryFile
import subprocess


class ShortCutterMacOS(ShortCutterLinux):
    @staticmethod
    def _get_desktop_folder():
        return p.join(p.expanduser('~'), 'Desktop')

    @staticmethod
    def _get_menu_folder():
        return p.join('/', 'Applications') 

    @staticmethod
    def _create_shortcut_file(shortcut_name, target_path, shortcut_directory):
        """
        Creates a MacOS app which opens an executable via the terminal

        Returns the file path of the shortcut created
        """
        shortcut_file_path = p.join(shortcut_directory, shortcut_name + ".app")

        # create the AppleScript script
        sf = NamedTemporaryFile(mode="w")
        sf.write('tell application "Terminal"\n')
        sf.write('activate\n')
        sf.write('do script "{}"\n'.format(target_path))
        sf.write('end tell\n')
        sf.flush()

        # compile the script into an application
        result = subprocess.run(["osacompile", "-o", shortcut_file_path, sf.name], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        if len(result.stderr):
            raise ShortcutError("Error occured creating app - {}".format(str(result.stderr)))

        sf.close()

        return shortcut_file_path
