@echo off

@REM ! WARNING RUN THIS FILE AT THE TOP DIRECTORY AKA THE OG DIR 
@REM COMMAND PRE-PROMPTED TEMPLATE INSTALLER FOR PyP v0.1

@REM Variables
cd "src"
set homedir="%cd%"

@REM param: Change to The Installation Directory
cd %1
mkdir %2
cd %2

dir %homedir%

xcopy %homedir% /E

npm init -y

exit
