chcp 65001 > NUL
pandoc README.md -o README.rst
sphinx-build -b rst docs docs\_build
::sphinx-apidoc -f -o docs\_build docs
copy docs\_build\api.rst api.rst
@echo replace '         *' -^> '          *' manually
