chcp 65001 > NUL
pandoc README.md -o README.rst
sphinx-build -b rst docs docs\_build
::sphinx-build docs docs\_build
type docs\_build\api.rst | python docs/rst_fix.py > api.rst
