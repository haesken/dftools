$basics = [
    "mercurial",
    "build-essential",
    "libglib2.0-dev",
    "libSM-dev",
    "libxrender-dev",
    "libfontconfig1-dev",
    "libxext-dev",
]
package { $basics: ensure => "latest" }

$qt_tools = [
    "qt4-qmake",
    "qt4-dev-tools",
]
package { $qt_tools: ensure => "latest" }
