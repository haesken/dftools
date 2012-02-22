$basics = [
    "build-essential",
    "libglib2.0-dev",
    "libSM-dev",
    "libxrender-dev",
    "libfontconfig1-dev",
    "libxext-dev",
]
package { $basics: ensure => "latest" }

$qt = [
    "qt4-qmake",
    "qt4-dev-tools",
]
package { $qt: ensure => "latest" }
