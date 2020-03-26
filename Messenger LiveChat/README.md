# Messenger "Live Chat"

<img src="https://github.com/ElizaLo/Practice-Python/blob/master/Messenger%20LiveChat/MainWindow.png" width="440" height="575">

## Requirements

- Qt Designer
    - [Qt Designer Manual](https://doc-snapshots.qt.io/qt5-dev/qtdesigner-manual.html)
- `PyQt5`
    - [PyQt5 Reference Guide](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- `Flask`
- `datetime`
- `requests`

## Errors:
- **socket.error: [Errno 48] Address already in use**
    1. `sudo lsof -i:5000`
    
    This will give you a list of processes using the port if any. Once the list of processes is given, use the id on the PID column to terminate the process use
    
    2. `kill PID` use the provided PID
