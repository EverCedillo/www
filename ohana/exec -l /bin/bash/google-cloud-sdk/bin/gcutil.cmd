@echo off
rem Copyright 2013 Google Inc. All Rights Reserved.

echo WARNING: 'gcutil' has been deprecated and is no longer part of default Cloud SDK distribution. >&2
echo WARNING: Please use 'gcloud compute' instead. >&2
echo WARNING: For more information see https://cloud.google.com/compute/docs/gcutil >&2
echo. >&2

SET GCUTIL_SCRIPT=%~dp0bootstrapping\gcutil.py

IF EXIST %GCUTIL_SCRIPT% GOTO GCUTIL_INSTALLED

echo WARNING: If you still must use 'gcutil', you can install it via >&2
echo WARNING: 'gcloud components update gcutil', >&2
echo WARNING: but note this option will also soon will be removed. >&2

exit /b 1

:GCUTIL_INSTALLED

SETLOCAL EnableDelayedExpansion

${CLOUDSDK_CMD_PREAMBLE}

"%COMSPEC%" /C ""%CLOUDSDK_PYTHON%" %CLOUDSDK_PYTHON_ARGS% "%GCUTIL_SCRIPT%" %*"

"%COMSPEC%" /C exit %ERRORLEVEL%
