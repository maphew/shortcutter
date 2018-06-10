(
echo cd /d %cd%
echo python setup.py sdist
echo twine upload dist/* --skip-existing
) | clip
