Shortcutter
===========

Shortcutter is a cross platform API for creating shortcuts for python
applications meant to be used in setup.py script or as a command line
application (fork of the Shortcut).

Shortcutter creates shortcucts that activate python environment prior
launching the app. It supports virtual environments, Anaconda/Miniconda,
conda environments, ``sudo pip install``, ``pip install --user``.
Shortcutter will do its best to find your app, searching for the usual
suspects in the usual places (i.e. those in the PATH), or you can give
it a full path.

Additioanlly special command/method can create shortcut to the terminal
at activated environment (plus terminal shortcut at conda root).

To create desktop and menu shortcuts for ``python``:

-  Using the app:

   ::

      shortcutter python
      shortcutter --terminal

-  Using the Python API for example in ``setup.py``:

   .. code:: py

      from shortcutter import ShortCutter
      sc = ShortCutter()
      sc.create_desktop_shortcut("python")
      sc.create_menu_shortcut("python")
      sc.create_shortcut_to_env_terminal()

It was created to solve a simple problem - if you install a python
package using ``pip`` there is no simple way of creating a shortcut to
the program it installs.

Table of contents
=================

-  `Install <#install>`__
-  `Command line interface <#command-line-interface>`__
-  `Python API <#python-api>`__
-  `Operating Systems <#operating-systems>`__
-  `Status <#status>`__
-  `Change log <#change-log>`__

Install
=======

Shortcut is available on
`pypi <https://pypi.python.org/pypi/shortcutter>`__ and can be installed
using ``pip``:

-  Windows :

   ::

        pip install shortcutter

-  MacOS or Linux :

   ::

        pip3 install shortcutter

Command line interface
======================

The ``-h`` or ``--help`` option will display the help:

::

   shortcutter --help

::

   usage: shortcutter [-h] [-d] [-m] [-n [NAME]] [-s] [-t] [target]

   Automatic shortcut creator. Shortcuts auto-activate their environments by 
   default.

   positional arguments:
     target                The target executable to create Desktop and Menu
                           shortcuts.

   optional arguments:
     -h, --help            show this help message and exit
     -d, --desktop         Only create a desktop shortcut.
     -m, --menu            Only create a menu shortcut.
     -n [NAME], --name [NAME]
                           Name of the shortcut without extension (autoname
                           otherwise).
     -s, --simple          Create simple shortcut without activate wrapper.
     -t, --terminal        Create shortcut to environment with shortcutter (plus
                           shortcut to root environment in case of conda).

`Python API <https://github.com/kiwi0fruit/shortcutter/blob/master/api.rst>`__
==============================================================================

`Python
API <https://github.com/kiwi0fruit/shortcutter/blob/master/api.rst>`__.

Operating Systems
=================

Shortcut support Windows, MacOS and Linux.

The way shortcuts are provide and applications launched depends on the
operating system.

Windows
~~~~~~~

``.lnk`` files pointing directly to the application paths are created in
the User Desktop and Programs folders.

MacOS
~~~~~

MacOS applications are created which run the application via a terminal
and copied to the User Desktop (``~/Desktop``) and Launchpad
(``/Applications``).

Linux
~~~~~

``.desktop`` files are created which start the application via the shell
and created in the User Desktop and applications menu
(``~/.local/share/applications``).

Status
======

Alpha - tested and works but
`issues <https://github.com/kiwi0fruit/shortcutter/issues>`__ maybe
experienced and API changes are possible.

`Change log <https://github.com/kiwi0fruit/shortcutter/blob/master/CHANGE_LOG.md>`__
====================================================================================

`Change
log <https://github.com/kiwi0fruit/shortcutter/blob/master/CHANGE_LOG.md>`__.
