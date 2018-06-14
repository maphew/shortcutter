@set this=%~0
(
echo cd /d %cd%
echo call "%this:~0,-13%.bat"
) | clip
