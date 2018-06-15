Change log
==========

## 0.1.1 - 2018-06-15

* Forked shortcut > shortcutter,
* Added support for virtual environments, Anaconda/Miniconda, conda environments: shortcuts activate env before starting the target,
* Shortcut name now can be set,
* Better support for setup.py use-cases:
  * Folder shortcuts,
  * Shortcuts can be created to yet non-existing targets,
  * Added 'silent' and log mode when errors are not raised, 
* Documentation moved to GitHub,
* Added versioneer (auto version based on GitHub commit),
* Only one dependence on Windows: pywin32 (available on conda-forge).


## 0.0.2 - 2018-02-25

* added desktop_directory and menu_directory properties
* documentation updates


## 0.0.1 - 2018-02-25

* initial alpha release
* support for Windows, MacOS & Linux
* `shortcutter` app and `ShortCutter` API
