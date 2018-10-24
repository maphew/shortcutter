cd /d "%~dp0"

pandoc README.md -o README.rst
sphinx-build -b rst docs docs\_build
chcp 65001
type docs\_build\api.rst | python docs/rst_fix.py > api.rst
chcp 1252
rmdir /s /q docs\_build
