
# NoirBird's IDM Trial Reset

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

A simple Python script to reset trial in Internet Download Manager.

**Note: I do NOT condone using cracked software. Please buy [a licence](https://secure.internetdownloadmanager.com/buy_idm.html).**
## Usage

**PowerShell Command (Recommended):**

(Always up to date, Run PowerShell as Administrator)

```ps
iwr -useb https://raw.githubusercontent.com/NoirBird/IDM-Trial-Reset/main/powershell-install.ps1 | iex
```

**Python Script:**

```bat
  py NoirBird-IDM-Reset.py
```

**EXE File:**

```bat
Just open the file LoL
```


## Building

To convert Python file to Executable binary you may use 2 different options:

**Nuitka:**

```bat
  pip install nuitka
  nuitka --mingw64 --onefile --assume-yes-for-downloads --remove-output --output-filename=NBIBMRPatcher "NoirBird-IDM-Reset.py"
```

**PyInstaller:**

```bat
  pip install pyinstaller
  pyinstaller -F --uac-admin NoirBird-IDM-Reset.py
```
