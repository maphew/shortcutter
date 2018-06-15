
Python API
******
======


ShortCutter
===========

class shortcutter.base.ShortCutter(raise_errors=False, error_log=None, activate=True, exists=True)
==================================================================================================

   Creates applicaton shortcuts for Windows, MacOS and Linux operating
   systems.

   To create desktop and menu shortcuts to ``python``:

   ::

      from shortcut import ShortCutter
      s = ShortCutter()
      s.create_desktop_shortcut("python")
      s.create_menu_shortcut("python")

   raise_errors : bool=False
      Whether to raise exceptions or skip errors and continue.

   error_log : object=None
      File object where to write errors when ``raise_errors=False``.
      Default is None - do not write errors. Can also be
      ``sys.stderr`` or ``io.StringIO()``.

   desktop_folder : str
      Directory used when creating desktop shortcuts.

   menu_folder : str
      Directory used when creating menu shortcuts.

   bin_folder_pyexe : str
      ``Scripts`` or ``bin`` dir path. Simply closest to python
      executable path.

   bin_folder_shcut : str or None
      ``Scripts`` or ``bin`` dir path where shortcutter executable was
      installed.

   local_root : str
      Root directory path of the current python environment /
      installation. Derived from python executable path.

   activate : bool=True
      Whether to create shortcuts that automatically activate conda
      environment / virtual environment.

   exists : bool=True
      Whether the target should exist or not. If not then add ``/``
      (``\`` on Windows) at the end of the path to get dir shortcut.

   activate_args : tuple (str or None, str or None)
      First is the activate script full path (or None if it’s wasn’t
      found) - conda’s or venv’s. Second is the env argument of the
      activate script (or None if not needed).

ba(script_name)
~~~~~~~~~~~~~~~

      Returns platform independent shell script (bash/batch) name:

      * run > run (on Unix)

      * run > run.bat (on Windows)

create_desktop_shortcut(target, shortcut_name=None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Creates a desktop shortcut to a target.

      :Parameters:
          * **target** (*str*) – The target to create a shortcut for,
            it can be a fully qualified file path
            ``/path/to/my_program`` or a simple application name
            ``my_program``.

          * **shortcut_name** (*str=None*) – Name of the shortcut
            without extension (``.lnk`` would be appended if needed).
            If None uses the target filename.

      :Returns:
         (shortcut_name, target_path, shortcut_file_path)

      :Return type:
         tuple (str, str, str or None)

create_menu_shortcut(target, shortcut_name=None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Creates a menu shortcut to a target.

      :Parameters:
          * **target** (*str*) – The target to create a shortcut for,
            it can be a fully qualified file path
            ``/path/to/my_program`` or a simple application name
            ``my_program``.

          * **shortcut_name** (*str=None*) – Name of the shortcut
            without extension (``.lnk`` would be appended if needed).
            If None uses the target filename.

      :Returns:
         (shortcut_name, target_path, shortcut_file_path)

      :Return type:
         tuple (str, str, str or None)

create_shortcut(target, shortcut_directory, shortcut_name=None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Creates a shortcut to a target.

      :Parameters:
          * **target** (*str*) – The target to create a shortcut for,
            it can be a fully qualified file path
            ``/path/to/my_program`` or a simple application name
            ``my_program``.

          * **shortcut_directory** (*str*) – The directory path where
            the shortcut should be created.

          * **shortcut_name** (*str=None*) – Name of the shortcut
            without extension (``.lnk`` would be appended if needed).
            If None uses the target filename.

      :Returns:
         (shortcut_name, target_path, shortcut_file_path)

      :Return type:
         tuple (str, str, str or None)

create_shortcut_to_env_terminal(shortcut_name=None, shortcut_directory=None, desktop=True, menu=True)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Creates shortcuts for console (terminal) that has already
      activated the environment we are installing to (plus shortcut to
      root environment in case of conda).

      :Parameters:
          * **shortcut_name** (*str=None*) – Name of the shortcut
            without extension (``.lnk`` would be appended if needed).
            If None uses the target filename.

          * **shortcut_directory** (*str=None*) – The directory path
            where the shortcuts should be created.

          * **desktop** (*bool=True*) – Whether to create shortcuts on
            the desktop.

          * **menu** (*bool=True*) – Whether to create shortcuts in
            the menu.

      :Returns:
         True if all operations were successful, False otherwise.

      :Return type:
         bool

exe(app_name)
~~~~~~~~~~~~~

      Returns platform independent executable name:

      * app > app (on Unix)

      * app > app.exe (on Windows)

find_target(target)
~~~~~~~~~~~~~~~~~~~

      Finds a file path for a target application. Single-worded
      targets like ``'app'`` are always searched in the PATH. You
      should prepend ``./app`` to tell that the file is in the CWD.

      :Parameters:
         **target** (*str*) – The target to find, it can be a fully
         qualified file path ``/path/to/my_program`` or a simple
         application name ``my_program``.

      :Returns:
         Returns a single target file path or ``None`` if a path can’t
         be found.

      :Return type:
         str or None

makedirs(*args)
~~~~~~~~~~~~~~~

      Recursively creates dirs if they don’t exist. Utilizes
      ``self.raise_errors`` and ``self.error_log``.

      :Parameters:
         ***args** (*str*) – Multiple paths (str) for folders to
         create.

      :Returns:
         True on success False of failure.

      :Return type:
         bool

search_for_target(target)
~~~~~~~~~~~~~~~~~~~~~~~~~

      Searches for a target application.

      :Parameters:
         **target** (*str*) – The target to find.

      :Returns:
         Returns a list of potential target file paths, it no paths
         are found an empty list is returned.

      :Return type:
         list(str)
