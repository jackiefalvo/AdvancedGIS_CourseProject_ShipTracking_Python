@set the_env=TEST
call "C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\activate.bat" "%the_env%"
call "%localappdata%\ESRI\conda\envs\%the_env%\scripts\jupyter-notebook.exe" %cd% 
call "C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\deactivate.bat"