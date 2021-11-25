@ECHO OFF
set arg1=%1
set arg2=%2
set arg3=%3
rmdir /q /s __pycache__
git add .
git commit -m %arg1%
git push -u %arg2% %arg3%
