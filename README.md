Shortcutter
===========

[![Latest Version](https://badge.fury.io/py/shortcut.svg)](https://badge.fury.io/py/bluedot)
[![Docs](https://readthedocs.org/projects/shortcut/badge/)](https://readthedocs.org/projects/shortcut/)

Shortcutter is a cross platform API for creating shortcuts for python applications meant to be used in setup.py script or as a command line application (fork of the Shortcut).

Shortcutter creates shortcucts that activate python environment prior launching the app. It supports virtual environments, Anaconda/Miniconda, conda environments, `sudo pip install`, `pip install --user`. Shortcutter will do its best to find your app, searching for the usual suspects in the usual places (i.e. those in the PATH), or you can give it a full path.

To create desktop and menu shortcuts for `python`:

-   Using the app:

        shortcutter python

-   Using the Python API:
    ```py
    from shortcutter import ShortCutter
    s = ShortCutter()
    s.create_desktop_shortcut("python")
    s.create_menu_shortcut("python")
    ```

It was created to solve a simple problem - if you install a python
package using `pip` there is no simple way of creating a shortcut to the
program it installs.


Documentation
=============

There is comprehensive documentation at [shortcut.readthedocs.io](https://shortcut.readthedocs.io).


Install
=======

Shortcut is available on
[pypi](https://pypi.python.org/pypi/shortcutter) and can be installed using `pip`:

- Windows :

        pip install shortcutter

- MacOS or Linux :

        pip3 install shortcutter


Command line interface
======================

The `-h` or `--help` option will display the help:
```
shortcutter --help
```

```
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
```


Status
======

Alpha - tested and works but
[issues](https://github.com/kiwi0fruit/shortcutter/issues) maybe
experienced and API changes are possible.

It should work with Windows, MacOS and Linux operating systems.


[Change log](CHANGE_LOG.md)
==========
