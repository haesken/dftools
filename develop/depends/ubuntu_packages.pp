$lxml = [
    "libxslt1-dev",
    "libxml2-dev",
]
package { $lxml: ensure => "latest" }

$upx = [
    "upx-ucl",
]
package { $upx: ensure => "latest" }
