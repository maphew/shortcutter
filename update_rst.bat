chcp 65001 > NUL
pandoc README.md -o README.rst
sphinx-build -b rst docs api shortcutter/base.py
