python setup.py sdist
chcp 1252 && set "PYTHONIOENCODING="
twine upload dist/*
chcp 65001 && set "PYTHONIOENCODING=utf-8"
rmdir /s /q dist
