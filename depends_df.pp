$libs = [
    "ncurses-base",
    "libncurses5",
    "libncurses5-dev",
    "libsdl1.2debian-all",
    "libsdl1.2-dev",
    "libsdl-image1.2",
    "libsdl-image1.2-dev",
    "libglu1-mesa",
    "libglu1-mesa-dev",
    "libgtk2.0-0",
    "libgtk2.0-dev",
    "libopenal1",
    "libopenal-dev",
    "ia32-libs",
]
package { $libs: ensure => "latest" }

$download = [
    "wget",
]
package { $download: ensure => "latest" }
