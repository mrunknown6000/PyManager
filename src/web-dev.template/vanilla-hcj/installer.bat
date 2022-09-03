@echo off
@REM REMEMBER TO MAKE EVERY COMMAND > NUL 

cd "src"
set homedir="%cd%"

cd %1 > NUL
mkdir %2 > NUL
robocopy %homedir% %2 /e > NUL

cd %2 > NUL
npm init -y > NUL
exit