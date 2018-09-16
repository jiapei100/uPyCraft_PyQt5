# uPyCraft_PyQt5
This is my modified version of [uPyCraft](https://github.com/DFRobot/uPyCraft) based on [PyQt5](https://sourceforge.net/projects/pyqt/files/PyQt5/). I believe it's platform independent, however, ONLY Linux has been tested so far.

## Environment
* Ubuntu 18.04.1
* Python 3.6.5
* Qt 5.11.1
* PyQt5

## Pre-Install

1. python3
```bash
$ python --version
Python 3.6.5
$ pip --version
pip 18.0 from ~/.local/lib/python3.6/site-packages/pip (python 3.6)
$ pip3 --version
pip 18.0 from ~/.local/lib/python3.6/site-packages/pip (python 3.6)

$ pip3 install -U pyinstaller --user
$ pip3 install -U pyflakes --user
$ pip3 install -U pyserial --user
```

2. QT
Download the NEWEST **qt-opensource-linux-x64-5.11.1.run** from https://www.qt.io/download, and:
```bash
    $ sudo ./qt-opensource-linux-x64-5.11.1.run
```

3. SIP
Refer to https://riverbankcomputing.com/software/sip/download
```bash
    $ pip3 install -U sip --user
```
        
4. PyQt5
Refer to https://sourceforge.net/projects/pyqt/files/PyQt5/
```bash
   $ pip3 install -U pyqt5 --user
```

5. QScintilla2
Refer to https://pypi.org/project/QScintilla/
```bash
$ pip3 install -U QScintilla --user
```


## Install uPyCraft

```bash
$ pyinstaller -F uPyCraft.py
```


## Run uPyCraft
```bash
$ cd dist
$ ./uPyCraft
```

![uPyCraft GUI](https://raw.githubusercontent.com/LongerVision/Resource/master/uPyCraft/uPyCraft.jpg)


