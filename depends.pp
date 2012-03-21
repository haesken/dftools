$depends = [
    "python2.7",
    "python-lxml",
    "python-requests",
    "python-urlgrabber",
]
package { $depends: ensure => "installed" }
