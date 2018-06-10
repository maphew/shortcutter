Shortcutter
===========

[![Latest Version](https://badge.fury.io/py/shortcut.svg)](https://badge.fury.io/py/bluedot)
[![Docs](https://readthedocs.org/projects/shortcut/badge/)](https://readthedocs.org/projects/shortcut/)

Shortcutter is a cross platform command line application and API for creating shortcuts.

`shortcutter` will do its best to find your app, searching for the usual suspects in the usual places (i.e. those in the PATH), or you can give it a full path.

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

- MacOS :

        pip3 install shortcutter

- Linux :

        sudo pip3 install shortcutter

Status
======

Alpha - tested and works but
[issues](https://github.com/kiwi0fruit/shortcutter/issues) maybe
experienced and API changes are possible.

It should work with Windows, MacOS and Linux operating systems.
