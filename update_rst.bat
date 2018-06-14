chcp 65001 > NUL
pandoc README.md -o README.rst
sphinx-build -b rst docs docs\_build
copy docs\_build\api.rst api.rst
