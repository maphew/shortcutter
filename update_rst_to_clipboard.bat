(
echo chcp 65001
echo cd /d %cd%
echo pandoc README.md -o README.rst
echo sphinx-build -b rst docs api shortcutter/base.py
) | clip
