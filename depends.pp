$depends = [
    "python-lxml",
    "python2.7",
    "wget",
]
package { $depends: ensure => "installed" }
