# Qt #

![Torizon Version](https://img.shields.io/badge/Torizon_OS-7.1.0-blue?logo=torizon)
&nbsp;
![Torizon Container](https://img.shields.io/badge//allanktoradex/cppqmltemplate--upstream-torizon--7-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//allanktoradex/cppqmltemplate--imx8-torizon--7-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//allanktoradex/cppqmltemplate--am62-torizon--7-blue?logo=docker)

Deploy a simple Qt QML application (in C++) in a Weston environment. It creates a window and displays an animation with the Torizon icon using the Weston container as the Wayland compositor.

![Screenshot](https://docs1.toradex.com/116544-demogalleryqt.png?v=2)

## About

Qt is a popular cross-platform framework for developing (GUIs). It provides a rich set of libraries and tools to help developing high-performance applications.

The source code of this application is available on the [Torizon Samples](https://github.com/toradex/vscode-torizon-templates/tree/dev/cppQML) repository.

## Requirements
To run this demo, you need:s

- A supported Toradex SoM;
- Display;
- Torizon OS installed;
- Internet Connectivity.


## Deploy from the Torizon Cloud

- [Qt Demo Applications](https://www.torizon.io/qt-demo-applications).

## More Resources

- [Qt on Torizon OS](https://developer.toradex.com/torizon/application-development/use-cases/gui/qt-on-torizon-os);
- [Getting Started with Qt](https://developer.toradex.com/linux-bsp/application-development/gui/getting-started-with-qt/);
- [Qt 6 QML Template](https://github.com/torizon/vscode-torizon-templates/blob/dev/cppQML/.doc/README.md);
- [Qt PySide2 Tempĺate](https://github.com/torizon/vscode-torizon-templates/tree/bookworm/python3Pyside2QML/.doc).

## Tested Devices
### **Verdin iMX8M Plus**

<details>
<summary>✅ 0058 - Verdin iMX8M Plus Quad 4GB WB IT </summary>

**Job ID**: `716736`

**Date**: `Wed Apr  9 12:59:11 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/500611918e07c8fe1cf9b3cc8f76327936d80d93ad461d3fe0da9c30624ff84b/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mp-14772913
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Plus WB on Verdin Development Board
Toradex version:          0058 V1.1A
Serial number:            14772913
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
e7160ab73b62   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
6b4e12341d0b   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0063 - Verdin iMX8M Plus Quad 4GB IT </summary>

**Job ID**: `716733`

**Date**: `Wed Apr  9 13:06:52 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/500611918e07c8fe1cf9b3cc8f76327936d80d93ad461d3fe0da9c30624ff84b/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mp-07107042
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Plus on Verdin Development Board
Toradex version:          0063 V1.1A
Serial number:            07107042
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
addf07f3e252   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
e982b160352a   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0064 - Verdin iMX8M Plus Quad 2GB WB IT </summary>

**Job ID**: `716743`

**Date**: `Wed Apr  9 12:58:30 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/500611918e07c8fe1cf9b3cc8f76327936d80d93ad461d3fe0da9c30624ff84b/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mp-15128279
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Plus WB on Verdin Development Board
Toradex version:          0064 V1.1A
Serial number:            15128279
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
77866cc99148   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
776489b2a91d   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0065 - Verdin iMX8M Plus QuadLite 1GB IT </summary>

**Job ID**: `716740`

**Date**: `Wed Apr  9 13:07:02 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/500611918e07c8fe1cf9b3cc8f76327936d80d93ad461d3fe0da9c30624ff84b/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mp-15314927
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Plus on Verdin Development Board
Toradex version:          0065 V1.1A
Serial number:            15314927
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
8202de38b1a6   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
9e04e584f018   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0066 - Verdin iMX8M Plus Quad 8GB WB </summary>

**Job ID**: `716757`

**Date**: `Wed Apr  9 12:57:32 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/500611918e07c8fe1cf9b3cc8f76327936d80d93ad461d3fe0da9c30624ff84b/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mp-07203684
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Plus WB on Verdin Development Board
Toradex version:          0066 V1.0A
Serial number:            07203684
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
cc4f25de5438   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
9e72edff79a6   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0070 - Verdin iMX8M Plus Quad 8GB WB IT </summary>

**Job ID**: `716731`

**Date**: `Wed Apr  9 12:53:18 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/500611918e07c8fe1cf9b3cc8f76327936d80d93ad461d3fe0da9c30624ff84b/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mp-15128129
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Plus WB on Verdin Development Board
Toradex version:          0070 V1.1A
Serial number:            15128129
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
081fc6a384a5   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
e7a17cec1bf0   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>

### **Verdin iMX8M Mini**

<details>
<summary>✅ 0055 - Verdin iMX8M Mini Quad 2GB WB IT </summary>

**Job ID**: `716747`

**Date**: `Wed Apr  9 12:58:20 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/28c6117959abbf7185a98daaa9ef3bef7020fdd7ea6dbaa0701fc0e45f2a38a2/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mm-15005793
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Mini WB on Verdin Development Board
Toradex version:          0055 V1.1F
Serial number:            15005793
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
915e59e279ba   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
db78432565ae   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0057 - Verdin iMX8M Mini DualLite 1GB </summary>

**Job ID**: `716745`

**Date**: `Wed Apr  9 13:00:23 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/28c6117959abbf7185a98daaa9ef3bef7020fdd7ea6dbaa0701fc0e45f2a38a2/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mm-15176665
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Mini on Verdin Development Board
Toradex version:          0057 V1.1C
Serial number:            15176665
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
71ae3ae8df44   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
6e52ca3ef70d   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0059 - Verdin iMX8M Mini Quad 2GB IT </summary>

**Job ID**: `716760`

**Date**: `Wed Apr  9 13:03:59 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/28c6117959abbf7185a98daaa9ef3bef7020fdd7ea6dbaa0701fc0e45f2a38a2/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mm-15038814
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Mini on Verdin Development Board
Toradex version:          0059 V1.1D
Serial number:            15038814
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
41e02a391356   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
1b8efe109e49   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0060 - Verdin iMX8M Mini DualLite 1GB WB IT </summary>

**Job ID**: `716737`

**Date**: `Wed Apr  9 13:02:08 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/28c6117959abbf7185a98daaa9ef3bef7020fdd7ea6dbaa0701fc0e45f2a38a2/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mm-07174100
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Mini WB on Verdin Development Board
Toradex version:          0060 V1.1C
Serial number:            07174100
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
6e16950fb41b   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
a4661eb98135   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0068 - Verdin iMX8M Mini Quad 2GB WB IT (No CAN) </summary>

**Job ID**: `716732`

**Date**: `Wed Apr  9 12:53:33 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/28c6117959abbf7185a98daaa9ef3bef7020fdd7ea6dbaa0701fc0e45f2a38a2/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mm-07334924
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Mini WB on Verdin Development Board
Toradex version:          0068 V1.1#26
Serial number:            07334924
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
681da79b30c8   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
9dcd4bdc7657   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0086 - Verdin iMX8M Mini DualLite 2GB IT </summary>

**Job ID**: `716754`

**Date**: `Wed Apr  9 13:05:16 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/28c6117959abbf7185a98daaa9ef3bef7020fdd7ea6dbaa0701fc0e45f2a38a2/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mm-15306892
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Mini on Verdin Development Board
Toradex version:          0086 V1.1#26
Serial number:            15306892
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
3e379cd224db   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
c200806ee54a   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0087 - Verdin iMX8M Mini Quad 2GB IT </summary>

**Job ID**: `716746`

**Date**: `Wed Apr  9 13:04:06 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/28c6117959abbf7185a98daaa9ef3bef7020fdd7ea6dbaa0701fc0e45f2a38a2/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mm-15366980
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Mini on Verdin Development Board
Toradex version:          0087 V1.1#26
Serial number:            15366980
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
ef5cd01488a3   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
ce8b8bf117dc   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0090 - Verdin iMX8M Mini Quad 4GB WB ET </summary>

**Job ID**: `716761`

**Date**: `Wed Apr  9 13:07:49 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/28c6117959abbf7185a98daaa9ef3bef7020fdd7ea6dbaa0701fc0e45f2a38a2/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-imx8mm-15421145
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin iMX8M Mini WB on Verdin Development Board
Toradex version:          0090 V1.1#26
Serial number:            15421145
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
35a0cf826b5a   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
99fc5724c4a4   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>

### **Verdin AM62**

<details>
<summary>✅ 0071 - Verdin AM62 Solo 512MB </summary>

**Job ID**: `716762`

**Date**: `Wed Apr  9 13:01:12 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.58-7.1.0-gf874412b7190 #1-Torizon SMP PREEMPT Fri Dec  6 14:07:48 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/f3e8eace2362cfd69fe527293cf3f705d48ce1c6781b1052c56459592e6a30dc/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-am62-15412814
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin AM62 on Verdin Development Board
Toradex version:          0071 V1.2A
Serial number:            15412814
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED         STATUS         PORTS      NAMES
4174e1972471   allanktoradex/cppqmltemplate-am62:torizon-7   "./cppqmltemplate"       2 minutes ago   Up 2 minutes   2231/tcp   1_custom-tests-app-1
a70c525e407d   torizon/weston-am62:4.4.0                     "/bin/sh -c '/usr/bi…"   2 minutes ago   Up 2 minutes              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0072 - Verdin AM62 Solo 512MB WB IT </summary>

**Job ID**: `716749`

**Date**: `Wed Apr  9 13:06:27 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.58-7.1.0-gf874412b7190 #1-Torizon SMP PREEMPT Fri Dec  6 14:07:48 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/f3e8eace2362cfd69fe527293cf3f705d48ce1c6781b1052c56459592e6a30dc/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-am62-15412792
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin AM62 WB on Verdin Development Board
Toradex version:          0072 V1.2A
Serial number:            15412792
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED         STATUS              PORTS      NAMES
869a8524fd94   allanktoradex/cppqmltemplate-am62:torizon-7   "./cppqmltemplate"       2 minutes ago   Up About a minute   2231/tcp   1_custom-tests-app-1
a4e3647d7b1c   torizon/weston-am62:4.4.0                     "/bin/sh -c '/usr/bi…"   2 minutes ago   Up 2 minutes                   1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0073 - Verdin AM62 Dual 1GB ET </summary>

**Job ID**: `716940`

**Date**: `Wed Apr  9 16:04:40 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.58-7.1.0-gf874412b7190 #1-Torizon SMP PREEMPT Fri Dec  6 14:07:48 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/f3e8eace2362cfd69fe527293cf3f705d48ce1c6781b1052c56459592e6a30dc/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-am62-15412849
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin AM62 on Verdin Development Board
Toradex version:          0073 V1.2A
Serial number:            15412849
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
2e10017efb82   allanktoradex/cppqmltemplate-am62:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
182e105f2922   torizon/weston-am62:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0074 - Verdin AM62 Dual 1GB IT </summary>

**Job ID**: `716741`

**Date**: `Wed Apr  9 13:09:45 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.58-7.1.0-gf874412b7190 #1-Torizon SMP PREEMPT Fri Dec  6 14:07:48 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/f3e8eace2362cfd69fe527293cf3f705d48ce1c6781b1052c56459592e6a30dc/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-am62-15412866
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin AM62 on Verdin Development Board
Toradex version:          0074 V1.2A
Serial number:            15412866
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
f38e39844c9c   allanktoradex/cppqmltemplate-am62:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
44f47cb2c673   torizon/weston-am62:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0075 - Verdin AM62 Dual 1GB WB IT </summary>

**Job ID**: `716939`

**Date**: `Wed Apr  9 16:06:56 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.58-7.1.0-gf874412b7190 #1-Torizon SMP PREEMPT Fri Dec  6 14:07:48 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/f3e8eace2362cfd69fe527293cf3f705d48ce1c6781b1052c56459592e6a30dc/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-am62-15412801
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin AM62 WB on Verdin Development Board
Toradex version:          0075 V1.2A
Serial number:            15412801
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
6f80e3a5c7be   allanktoradex/cppqmltemplate-am62:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
ee1b4280f6ec   torizon/weston-am62:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0076 - Verdin AM62 Quad 2GB WB IT </summary>

**Job ID**: `716756`

**Date**: `Wed Apr  9 12:56:07 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.58-7.1.0-gf874412b7190 #1-Torizon SMP PREEMPT Fri Dec  6 14:07:48 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/f3e8eace2362cfd69fe527293cf3f705d48ce1c6781b1052c56459592e6a30dc/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 verdin-am62-15412840
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Verdin AM62 WB on Verdin Development Board
Toradex version:          0076 V1.2A
Serial number:            15412840
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
1bbce6c24d2a   allanktoradex/cppqmltemplate-am62:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
356e3f0c222a   torizon/weston-am62:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>

### **Apalis iMX8**

<details>
<summary>✅ 0037 - Apalis iMX8QM 4GB WB IT </summary>

**Job ID**: `716758`

**Date**: `Wed Apr  9 13:04:55 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15445071
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QM V1.1 on Apalis Evaluation Board
Toradex version:          0037 V1.1F
Serial number:            15445071
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
cd339ebb5c13   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
2975bd517f2a   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0047 - Apalis iMX8QM 4GB IT </summary>

**Job ID**: `716755`

**Date**: `Wed Apr  9 13:09:49 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15444755
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QM V1.1 on Apalis Evaluation Board
Toradex version:          0047 V1.1E
Serial number:            15444755
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
54228db14cb0   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
0cbdc93da1cc   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0048 - Apalis iMX8QP 2GB WB </summary>

**Job ID**: `716742`

**Date**: `Wed Apr  9 12:57:01 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15444819
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QP V1.1 on Apalis Evaluation Board
Toradex version:          0048 V1.1E
Serial number:            15444819
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
b8eb0a8f9cd7   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
2a03ed5c5858   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0049 - Apalis iMX8QP 2GB </summary>

**Job ID**: `716938`

**Date**: `Wed Apr  9 15:49:23 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15304827
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QP V1.1 on Apalis Evaluation Board
Toradex version:          0049 V1.1E
Serial number:            15304827
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
e5405ab46fd0   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
34852237834d   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0067 - Apalis iMX8QM 8GB WB IT </summary>

**Job ID**: `716753`

**Date**: `Wed Apr  9 12:58:03 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15543176
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QM V1.1 on Apalis Evaluation Board
Toradex version:          0067 V1.1B
Serial number:            15543176
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
12f9aa76ae85   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
b3dfc989b197   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0091 - Apalis iMX8QM 4GB Wi-Fi BT IT </summary>

**Job ID**: `716752`

**Date**: `Wed Apr  9 13:04:20 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15556459
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QM V1.1 on Apalis Evaluation Board
Toradex version:          0091 V1.1A
Serial number:            15556459
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
e4f36446143a   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
2fa32062e17d   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0092 - Apalis iMX8QM 4GB IT </summary>

**Job ID**: `716734`

**Date**: `Wed Apr  9 13:08:42 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15556423
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QM V1.1 on Apalis Evaluation Board
Toradex version:          0092 V1.1A
Serial number:            15556423
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
08f76c41490c   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
337142da7102   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0093 - Apalis iMX8QP 2GB Wi-Fi BT </summary>

**Job ID**: `716759`

**Date**: `Wed Apr  9 12:53:31 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15556408
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QP V1.1 on Apalis Evaluation Board
Toradex version:          0093 V1.1A
Serial number:            15556408
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
404f351bdd85   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
e9535f2d7a5e   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0094 - Apalis iMX8QP 2GB </summary>

**Job ID**: `716739`

**Date**: `Wed Apr  9 13:05:01 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15556434
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QP V1.1 on Apalis Evaluation Board
Toradex version:          0094 V1.1A
Serial number:            15556434
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
ed8a51e2a1c2   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
43cb8d9f8c40   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0095 - Apalis iMX8QM 8GB Wi-Fi BT IT </summary>

**Job ID**: `716738`

**Date**: `Wed Apr  9 12:55:21 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/0eaef1f3b0f7eb2c759082d2ee270acca372e00b5de7c4e25895228855a35acf/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx8-15556476
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX8QM V1.1 on Apalis Evaluation Board
Toradex version:          0095 V1.1A
Serial number:            15556476
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
53e7c227e12a   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
a34bf3b9c064   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>

### **Apalis iMX6**

<details>
<summary>✅ 0027 - Apalis iMX6Q 1GB (WinEC) </summary>

**Job ID**: `716728`

**Date**: `Wed Apr  9 13:05:12 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.69-7.1.0-00039-g0f10503b36ba #1-Torizon SMP PREEMPT Wed Dec 11 07:36:24 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/78b61bf62f38ea12c032a3898494990c188f5fe6cd6443f768338823e976c6f6/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS Upstream"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx6-10927870
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX6Q/D Module on Apalis Evaluation Board
Toradex version:          0027 V1.1D
Serial number:            10927870
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                             COMMAND                  CREATED              STATUS              PORTS      NAMES
a336c7c46004   allanktoradex/cppqmltemplate-upstream:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
28d3602dfa82   torizon/weston:4.4.0                              "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0028 - Apalis iMX6Q 2GB IT (WinEC) </summary>

**Job ID**: `716744`

**Date**: `Wed Apr  9 12:58:15 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.69-7.1.0-00039-g0f10503b36ba #1-Torizon SMP PREEMPT Wed Dec 11 07:36:24 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/78b61bf62f38ea12c032a3898494990c188f5fe6cd6443f768338823e976c6f6/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS Upstream"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx6-10867499
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX6Q/D Module on Apalis Evaluation Board
Toradex version:          0028 V1.1D
Serial number:            10867499
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                             COMMAND                  CREATED              STATUS              PORTS      NAMES
eb53d651d94c   allanktoradex/cppqmltemplate-upstream:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
7e44ba318e00   torizon/weston:4.4.0                              "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0029 - Apalis iMX6D 512MB (WinEC) </summary>

**Job ID**: `716724`

**Date**: `Wed Apr  9 13:03:38 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.69-7.1.0-00039-g0f10503b36ba #1-Torizon SMP PREEMPT Wed Dec 11 07:36:24 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/78b61bf62f38ea12c032a3898494990c188f5fe6cd6443f768338823e976c6f6/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS Upstream"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx6-05054713
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX6Q/D Module on Apalis Evaluation Board
Toradex version:          0029 V1.1A
Serial number:            05054713
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                             COMMAND                  CREATED              STATUS              PORTS      NAMES
4f7392873c31   allanktoradex/cppqmltemplate-upstream:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
9c2c86cce95a   torizon/weston:4.4.0                              "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0035 - Apalis iMX6D 1GB IT (WinEC) </summary>

**Job ID**: `716729`

**Date**: `Wed Apr  9 13:06:50 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.69-7.1.0-00039-g0f10503b36ba #1-Torizon SMP PREEMPT Wed Dec 11 07:36:24 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/78b61bf62f38ea12c032a3898494990c188f5fe6cd6443f768338823e976c6f6/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS Upstream"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 apalis-imx6-10922891
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX6Q/D Module on Apalis Evaluation Board
Toradex version:          0035 V1.1C
Serial number:            10922891
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                             COMMAND                  CREATED              STATUS              PORTS      NAMES
cefe05c3c463   allanktoradex/cppqmltemplate-upstream:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
494e76c2a419   torizon/weston:4.4.0                              "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>

### **Colibri iMX8X**

<details>
<summary>✅ 0038 - Colibri iMX8QXP 2GB WB IT </summary>

**Job ID**: `716730`

**Date**: `Wed Apr  9 13:05:37 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/73741213d16339fd40639896f377654090019de0802df51ff67e7c55e2ef3b44/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 colibri-imx8x-14985749
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Colibri iMX8QXP on Colibri Evaluation Board V3
Toradex version:          0038 V1.0E
Serial number:            14985749
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
28ae082db8ea   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
3e5f137c97ae   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0050 - Colibri iMX8QXP 2GB IT </summary>

**Job ID**: `716721`

**Date**: `Wed Apr  9 13:07:14 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/73741213d16339fd40639896f377654090019de0802df51ff67e7c55e2ef3b44/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 colibri-imx8x-14986935
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Colibri iMX8QXP on Colibri Evaluation Board V3
Toradex version:          0050 V1.0E
Serial number:            14986935
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
e5dfcae26cec   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
4457238f2cc9   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0051 - Colibri iMX8DX 1GB WB </summary>

**Job ID**: `716723`

**Date**: `Wed Apr  9 13:02:54 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/73741213d16339fd40639896f377654090019de0802df51ff67e7c55e2ef3b44/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 colibri-imx8x-06760738
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Colibri iMX8DX on Colibri Evaluation Board V3
Toradex version:          0051 V1.0D
Serial number:            06760738
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                         COMMAND                  CREATED              STATUS              PORTS      NAMES
b8b9cf90b823   allanktoradex/cppqmltemplate-imx8:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
47b2aad2397a   torizon/weston-imx8:4.4.0                     "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0052 - Colibri iMX8DX 1GB </summary>

**Job ID**: `716726`

**Date**: `Wed Apr  9 13:10:30 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.54-7.1.0-g3493ccd66900 #1-Torizon SMP PREEMPT Tue Dec 17 21:04:41 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/73741213d16339fd40639896f377654090019de0802df51ff67e7c55e2ef3b44/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 colibri-imx8x-06843662
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Colibri iMX8DX on Colibri Evaluation Board V3
Toradex version:          0052 V1.0D
Serial number:            06843662
Processor arch:           aarch64
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
</details>

### **Colibri iMX7**

<details>
<summary>✅ 0039 - Colibri iMX7D 1GB </summary>

**Job ID**: `716735`

**Date**: `Wed Apr  9 13:01:53 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.69-7.1.0-00039-g0f10503b36ba #1-Torizon SMP PREEMPT Wed Dec 11 07:36:24 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/4d56f8a19850a28a66627fd6170052d64c008e66e560649733d4b93008cf22e3/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS Upstream"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 colibri-imx7-emmc-07006449
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Colibri iMX7D 1GB (eMMC) on Colibri Evaluation Board V3
Toradex version:          0039 V1.1C
Serial number:            07006449
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                             COMMAND                  CREATED              STATUS              PORTS      NAMES
c752f0ee3259   allanktoradex/cppqmltemplate-upstream:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
2eb449751627   torizon/weston:4.4.0                              "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>

### **Colibri iMX6ULL**

<details>
<summary>✅ 0062 - Colibri iMX6ULL 1GB IT </summary>

**Job ID**: `716725`

**Date**: `Wed Apr  9 13:11:59 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.69-7.1.0-00039-g0f10503b36ba #1-Torizon PREEMPT Wed Dec 11 07:36:24 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/1b8fcb554bfefb0bc7dbb00ac4bcc4501dd7d953a04843253584ec59a16539de/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS Upstream"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 colibri-imx6ull-emmc-15416030
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Colibri iMX6ULL 1GB (eMMC) on Colibri Evaluation Board V3
Toradex version:          0062 V1.1D
Serial number:            15416030
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                             COMMAND                  CREATED              STATUS              PORTS      NAMES
d030af6cb367   allanktoradex/cppqmltemplate-upstream:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
9b323180fbd2   torizon/weston:4.4.0                              "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>

### **Colibri iMX6**

<details>
<summary>✅ 0015 - Colibri iMX6DL 512MB (WinEC) </summary>

**Job ID**: `716722`

**Date**: `Wed Apr  9 13:02:48 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.69-7.1.0-00039-g0f10503b36ba #1-Torizon SMP PREEMPT Wed Dec 11 07:36:24 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/3a9e776bfdd2a102519af12fe88948023839b9ce6478dea1ccd3d153c8e419d9/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS Upstream"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 colibri-imx6-10866276
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Colibri iMX6DL/S on Colibri Evaluation Board V3
Toradex version:          0015 V1.1B
Serial number:            10866276
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                             COMMAND                  CREATED              STATUS              PORTS      NAMES
95e9cfa22bd7   allanktoradex/cppqmltemplate-upstream:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
9d4d01d39457   torizon/weston:4.4.0                              "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0017 - Colibri iMX6DL 512MB IT (WinEC) </summary>

**Job ID**: `716727`

**Date**: `Wed Apr  9 13:05:49 UTC 2025`

**Device Information**:
```
> tdx-info

Software summary
------------------------------------------------------------
Bootloader:               U-Boot
Kernel version:           6.6.69-7.1.0-00039-g0f10503b36ba #1-Torizon SMP PREEMPT Wed Dec 11 07:36:24 UTC 2024
Kernel command line:      root=LABEL=otaroot rootfstype=ext4 quiet logo.nologo vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fbcon=map:3 ostree=/ostree/boot.1/torizon/3a9e776bfdd2a102519af12fe88948023839b9ce6478dea1ccd3d153c8e419d9/0 systemd.log_color=false loglevel=0 tep_sup_out
Distro name:              NAME="Torizon OS Upstream"
Distro version:           VERSION_ID=7.1.0-build.4
Distro variant:           VARIANT="Docker"
Hostname:                 colibri-imx6-10866302
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Colibri iMX6DL/S on Colibri Evaluation Board V3
Toradex version:          0017 V1.1B
Serial number:            10866302
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE                                             COMMAND                  CREATED              STATUS              PORTS      NAMES
86629e655f98   allanktoradex/cppqmltemplate-upstream:torizon-7   "./cppqmltemplate"       About a minute ago   Up About a minute   2231/tcp   1_custom-tests-app-1
c2d6e5b03299   torizon/weston:4.4.0                              "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute              1_custom-tests-weston-1
```
</details>

