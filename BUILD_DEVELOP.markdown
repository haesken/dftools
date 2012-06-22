# Building & Developing Dwarf Fortress Auto

## Dependencies

Dwarf Fortress Auto has the following dependencies:
- [python 2.7](http://www.python.org/)
- [requests](http://docs.python-requests.org/en/latest/index.html) (python module)
- [lxml](http://lxml.de/installation.html) (python module)
    - [libxml](http://xmlsoft.org/)
    - [libxslt](http://xmlsoft.org/)

Building Dwarf Fortress Auto requires these additional dependencies:
- [git](http://git-scm.com/)
- [pip](http://www.pip-installer.org/)
- [virtualenv](http://www.virtualenv.org/)
- [pyinstaller](http://www.pyinstaller.org/) (installed as a submodule)

## Developing (Linux/OSX)

You should have all the dependencies installed (although
pyinstaller is only needed for building), then run

    source setup.sh

This will clone the git submodules (pyinstaller), then
create/activate the virtualenv and try to install
requests/lxml via pip. At this point you should be able to
run the scripts and start hacking. You will need to activate
the virtualenv every time you start hacking on it. (Unless
you install lxml/requests to your global packages.)

## Developing (Windows)

You probably shouldn't do this, using a Linux virtual
machine will be much easier.

## Building (Linux/OSX)

Have the virtualenv activated, then run

    ./build.sh

This will use pyinstaller to build the binaries,
copy them and the `custom` directory to the
`binaries/dwarf_fortress_auto` directory, and finally make a
tar.gz containing the `dwarf_fortress_auto` folder.

## Building (Windows)

I use a Windows 7 virtual machine dedicated to this, so
python & its modules are installed globally.

You will need to have all the dependencies installed. First
install python, then your python directory and the `scripts`
subdirectory to your path. [More info](http://stackoverflow.com/questions/6318156/adding-python-path-on-windows-7)

Install setuptools and pip.

Use pip to install requests normally.

    pip install requests

Use pip to install a static linked version of lxml

    pip install http://pypi.python.org/packages/2.7/l/lxml/lxml-2.3.win32-py2.7.exe#md5=9c02aae672870701377750121f5a6f84

Download and install [Github for Windows](http://windows.github.com/).
This will provide an installation of git/bash/tar etc.

Open a git shell and navigate to the Dwarf Fortress Auto directory.

Run this to clone pyinstaller

    git submodule update --init

Now run

    bash build_windows.sh

You should now have binaries and a tar.gz file in the binaries directory.
