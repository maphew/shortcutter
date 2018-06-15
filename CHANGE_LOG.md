Change log
==========

## 0.1.3 - 2018-06-15

* Forked shortcut > shortcutter,
* Renamed CLI app to `shortcutter`,
* Added support for virtual environments, Anaconda/Miniconda, conda environments: shortcuts activate env before starting the target,
* Special command/method can create shortcut to the terminal at activated environment (plus terminal shortcut at conda root),
* Shortcut name now can be set,
* Better support for setup.py use-cases:
  * Folder shortcuts,
  * Shortcuts can be created to yet non-existing targets,
  * Added 'silent' and log mode when errors are not raised,
  * Added folder creation method that nicely plays with 'silent' and log mode.
* Documentation moved to GitHub,
* Added versioneer (auto version based on GitHub commit),
* Only one dependence on Windows: pywin32 (available on conda-forge),
* Changed docstrings style to NumPy style,
* Removed some unpythonic code. 


## 0.0.2 - 2018-02-25

* added desktop_directory and menu_directory properties
* documentation updates


## 0.0.1 - 2018-02-25

* initial alpha release
* support for Windows, macOS & Linux
* `shortcut` app and `ShortCutter` API
