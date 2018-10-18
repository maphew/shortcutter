set "script_dir=%~dp0"
cd /d "%script_dir%"

chcp 65001 > NUL
pandoc README.md -o README.rst
sphinx-build -b rst docs docs\_build
type docs\_build\api.rst | python docs/rst_fix.py > api.rst
rmdir /s /q docs\_build
