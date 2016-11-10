# ghost
Webkit based scriptable web browser for python.

# requirements

- python2.7
- pyside

# install

- install pyside
```
osx:
  brew install cartr/qt4/qt
  brew install pyside
ubuntu:
  sudo apt-get install cmake qt4-dev-tools qtmobility-dev python2.7-dev libphonon-dev
  sudo pip install pyside
centos:
  yum install qtwebkit qtwebkit-devel
  pip install pyside
```    

- use ghost

  copy the ghost.py file to your project

# usage

see [test.py](https://github.com/gf0842wf/ghost/blob/master/test.py)

# if you want run in no x window server

- install xvfb
```
ubuntu: 
  sudo apt-get install xvfb
centos: 
  yum install xorg-X11-server-Xvfb
```
- run

`xvfb-run --auto-servernum --server-args="-screen 0 1280x760x24"  python test.py`
