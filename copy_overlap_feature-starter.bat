@echo off
SET PYCHARM="C:\Program Files\JetBrains\PyCharm Community Edition 2017.3\bin\pycharm64.exe"
SET OSGEO4W_ROOT="C:\OSGEO4W"
call %OSGEO4W_ROOT%\bin\o4w_env.bat
call %OSGEO4W_ROOT%\bin\qt5_env.bat
call %OSGEO4W_ROOT%\bin\py3_env.bat
@echo off
path %OSGEO4W_ROOT%\apps\qgis\bin;%PATH%
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis
set GDAL_FILENAME_IS_UTF8=YES
rem Set VSI cache to be used as buffer, see #6448
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python;%PYTHONPATH%

start python 
"O:\Script\copy_overlap_feature.py"

rem "\\gaf.de\nz\irsproj\EM3D\Script\EM3D-p5bdemedit-CopyTileToQC\QGIS3-Script\copy_tile_to_qc.py"