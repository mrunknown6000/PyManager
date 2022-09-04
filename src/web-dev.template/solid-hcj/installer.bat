@echo off
@REM REMEMBER TO MAKE EVERY COMMAND > NUL 

cd %1 
npx degit solidjs/templates/js %2 > NUL

exit