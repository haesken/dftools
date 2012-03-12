$depends = [
    "python-lxml",
    "python-pip",
    "python2.7",
    "unzip",
    "wget",
]
package { $depends: ensure => "installed" }
