python setup.py sdist
chcp 1251 > NUL
twine upload dist/* --skip-existing
chcp 65001 > NUL
