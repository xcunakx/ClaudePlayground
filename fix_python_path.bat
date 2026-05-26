@echo off
for /d %%i in ("%LOCALAPPDATA%\Programs\Python\Python3*") do (
    setx PATH "%PATH%;%%i;%%i\Scripts"
    echo Python path added: %%i
    goto done
)
echo Python installation not found. Make sure Python is installed.
:done
pause
