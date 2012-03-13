$depends = [
    "python-lxml",
    "python-pip",
    "python2.7",
    "wget",
]
package { $depends: ensure => "installed" }
