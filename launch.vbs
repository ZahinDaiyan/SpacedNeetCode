Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & ".venv\Scripts\pythonw.exe" & chr(34) & " app.py", 0
Set WshShell = Nothing
