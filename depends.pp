$depends = [
    "wget",
    "python2.7",
    "python-lxml",
    "unzip",
]
package { $depends: ensure => "latest" }
