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
at activated environment (plus terminal shortcut at conda root). In case
of Windows special env vars ``%u%`` and ``%a%`` defined that switch
encodings and ``%b%`` var that sets UTF-8 encoding and starts Bash.

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

Shortcuts without entry points (for GUI)
----------------------------------------

The default use-case for Shortcutter is to create shortcuts for
entry-points executables auto created by setup.py or conda. But
sometimes such entry-points do not work (like when using pythonw on
macOS with python.app package). See example how to work-around this:
`Enaml video app <https://github.com/kiwi0fruit/enaml-video-app>`__ (the
main idea is in
`bash <https://github.com/kiwi0fruit/enaml-video-app/blob/master/enaml-video-app/scripts/enaml-video-appw>`__
script).

Table of contents
=================

-  `Shortcutter <#shortcutter>`__

   -  `Shortcuts without entry points (for
      GUI) <#shortcuts-without-entry-points-for-gui>`__

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

-  Anaconda/Miniconda on Windows:

   .. code:: bat

      conda install pywin32 "pip>=10.0.1"
      pip install shortcutter

   if pip install fails try to change codepage: ``chcp 1252``,
-  Pure pip install on Windows:

   ::

      pip install --progress-bar shortcutter

-  Anaconda/Miniconda on macOS or Linux:

   ::

      conda install "pip>=10.0.1"
      pip install shortcutter

-  System Python 3 on macOS or Linux:

   ::

      pip3 install shortcutter

-  All other cases on macOS or Linux:

   ::

      pip install shortcutter

   Note: if ``pip3 install --user`` (simply ``pip3 install`` on Ubuntu)
   then you might need to add ``%APPDATA%\Python\Python36\Scripts`` (on
   Windows) / ``~/.local/bin`` (on Linux) to the PATH.

Shortcutter should work on Python 2 or can easily be bugfixed if you
post an issue.

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

Shortcut support Windows, macOS and Linux.

The way shortcuts are provide and applications launched depends on the
operating system.

Windows
~~~~~~~

``.lnk`` files pointing directly to the application paths are created in
the User Desktop and Programs folders.

macOS
~~~~~

macOS applications are created which run the application via a terminal
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
