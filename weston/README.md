# Weston Desktop Environment #

![Torizon Version](https://img.shields.io/badge/Torizon_OS-7.1.0-blue?logo=torizon) 
&nbsp;
![Torizon Container](https://img.shields.io/badge//torizon/weston-4.4.0-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//torizon/weston--vivante-4.4.0-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//torizon/weston--am62-4.4.0-blue?logo=docker)

This app starts a standalone instance of Weston from where you can launch other applications like the weston-terminal Terminal Emulator.

![Screenshot](https://docs1.toradex.com/116545-demogalleryweston.png?v=3)

## About

​Weston is the reference implementation of a Wayland display server protocol,
essentially the piece of software that makes sure that graphical application can be drawn alongside each other, superimposed and organized in windows.

To access the Weston demo apps, you can enter the running container and check for the weston commands.

```
> docker exec -it torizon-weston-1 bash
> ls /bin/weston*

weston                         weston-editor                  weston-resizor                 weston-simple-shm
weston-calibrator              weston-eventdemo               weston-scaler                  weston-simple-touch
weston-clickdot                weston-flower                  weston-screenshooter           weston-smoke
weston-cliptest                weston-fullscreen              weston-simple-damage           weston-stacking
weston-confine                 weston-image                   weston-simple-dmabuf-egl       weston-subsurfaces
weston-content_protection      weston-info                    weston-simple-dmabuf-feedback  weston-terminal
weston-debug                   weston-multi-resource          weston-simple-dmabuf-v4l       weston-touch-calibrator
weston-dnd                     weston-presentation-shm        weston-simple-egl              weston-transformed
```

# Requirements
To run this demo, you need:s

- A supported Toradex SoM;
- Display;
- Torizon OS installed;
- Internet Connectivity.

## Deploy from the Torizon Cloud

- [Weston Demo Applications](https://www.torizon.io/weston-desktop-environment).

## More Resources

- [Weston on Torizon OS](https://developer.toradex.com/torizon/6/application-development/provided-containers/working-with-weston-on-torizoncore);
- [Torizon Containers Github](https://github.com/torizon/torizon-containers/tree/oldstable/debian-docker-images/imx/weston);

## Tested Devices
### **Verdin iMX8M Plus**

<details>
<summary>✅ 0058 - Verdin iMX8M Plus Quad 4GB WB IT</summary>

**Job ID**: `701275`

**Date**: `Wed Mar 26 23:38:11 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
de1e3bf3b916   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0063 - Verdin iMX8M Plus Quad 4GB IT</summary>

**Job ID**: `701284`

**Date**: `Wed Mar 26 23:40:01 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
4e7f2bdb0f62   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0064 - Verdin iMX8M Plus Quad 2GB WB IT</summary>

**Job ID**: `701270`

**Date**: `Wed Mar 26 23:33:23 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
9ea9ab7825f5   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0065 - Verdin iMX8M Plus QuadLite 1GB IT</summary>

**Job ID**: `701281`

**Date**: `Wed Mar 26 23:34:13 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
798d60cfa06b   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0066 - Verdin iMX8M Plus Quad 8GB WB</summary>

**Job ID**: `701278`

**Date**: `Wed Mar 26 23:33:37 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
7d38a138e2be   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0070 - Verdin iMX8M Plus Quad 8GB WB IT</summary>

**Job ID**: `701276`

**Date**: `Wed Mar 26 23:34:03 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
31d51a86bd3a   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>

### **Verdin iMX8M Mini**

<details>
<summary>✅ 0055 - Verdin iMX8M Mini Quad 2GB WB IT</summary>

**Job ID**: `701273`

**Date**: `Wed Mar 26 23:37:25 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
00f3d27ff6e3   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0057 - Verdin iMX8M Mini DualLite 1GB</summary>

**Job ID**: `701292`

**Date**: `Wed Mar 26 23:38:35 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
b99e556ce094   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0059 - Verdin iMX8M Mini Quad 2GB IT</summary>

**Job ID**: `701261`

**Date**: `Wed Mar 26 23:39:41 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
abcbdb782be9   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0060 - Verdin iMX8M Mini DualLite 1GB WB IT</summary>

**Job ID**: `701285`

**Date**: `Wed Mar 26 23:41:29 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
67aabddd5071   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0068 - Verdin iMX8M Mini Quad 2GB WB IT (No CAN)</summary>

**Job ID**: `701272`

**Date**: `Wed Mar 26 23:35:02 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
c991bb154cda   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0086 - Verdin iMX8M Mini DualLite 2GB IT</summary>

**Job ID**: `701291`

**Date**: `Wed Mar 26 23:44:03 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
8d4a355ef353   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0087 - Verdin iMX8M Mini Quad 2GB IT</summary>

**Job ID**: `701289`

**Date**: `Wed Mar 26 23:46:51 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
7b1f250ea9f6   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0090 - Verdin iMX8M Mini Quad 4GB WB ET</summary>

**Job ID**: `701277`

**Date**: `Wed Mar 26 23:47:34 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
071b0be273f9   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>

### **Verdin AM62**

<details>
<summary>✅ 0071 - Verdin AM62 Solo 512MB</summary>

**Job ID**: `701286`

**Date**: `Wed Mar 26 23:41:04 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
7e33e87e2463   torizon/weston-am62   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0072 - Verdin AM62 Solo 512MB WB IT</summary>

**Job ID**: `701265`

**Date**: `Wed Mar 26 23:49:10 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
35c7ab405e83   torizon/weston-am62   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0073 - Verdin AM62 Dual 1GB ET</summary>

**Job ID**: `701287`

**Date**: `Wed Mar 26 23:45:36 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
625b09c31d70   torizon/weston-am62   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0074 - Verdin AM62 Dual 1GB IT</summary>

**Job ID**: `701274`

**Date**: `Wed Mar 26 23:45:07 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
c7e29d3cd1b0   torizon/weston-am62   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0075 - Verdin AM62 Dual 1GB WB IT</summary>

**Job ID**: `701279`

**Date**: `Wed Mar 26 23:44:40 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
833a2c780e18   torizon/weston-am62   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0076 - Verdin AM62 Quad 2GB WB IT</summary>

**Job ID**: `701268`

**Date**: `Wed Mar 26 23:35:39 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
f4dc34130b8a   torizon/weston-am62   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>

### **Apalis iMX8**

<details>
<summary>✅ 0037 - Apalis iMX8QM 4GB WB IT</summary>

**Job ID**: `701827`

**Date**: `Thu Mar 27 16:22:47 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
34f36190cc22   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0047 - Apalis iMX8QM 4GB IT</summary>

**Job ID**: `700255`

**Date**: `Wed Mar 26 09:16:20 UTC 2025`

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

CONTAINER ID   IMAGE                       COMMAND                  CREATED              STATUS              PORTS     NAMES
70e12c29cd35   torizon/weston-imx8:4.4.0   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0048 - Apalis iMX8QP 2GB WB</summary>

**Job ID**: `701823`

**Date**: `Thu Mar 27 16:23:11 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
42e60e5040bf   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0049 - Apalis iMX8QP 2GB</summary>

**Job ID**: `701821`

**Date**: `Thu Mar 27 16:22:55 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
6ad8b66e8e59   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0067 - Apalis iMX8QM 8GB WB IT</summary>

**Job ID**: `701819`

**Date**: `Thu Mar 27 16:23:14 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
de90a8b72296   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0091 - Apalis iMX8QM 4GB Wi-Fi BT IT</summary>

**Job ID**: `701822`

**Date**: `Thu Mar 27 16:27:55 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
8fbbc0d3b86f   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0092 - Apalis iMX8QM 4GB IT</summary>

**Job ID**: `701820`

**Date**: `Thu Mar 27 16:25:32 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
3dd3e8ada385   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0093 - Apalis iMX8QP 2GB Wi-Fi BT</summary>

**Job ID**: `701829`

**Date**: `Thu Mar 27 16:28:13 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
685c8c0d6374   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0094 - Apalis iMX8QP 2GB</summary>

**Job ID**: `701824`

**Date**: `Thu Mar 27 16:27:37 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
ee0b0cf46e70   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>

### **Apalis iMX6**

<details>
<summary>✅ 0027 - Apalis iMX6Q 1GB (WinEC)</summary>

**Job ID**: `701253`

**Date**: `Wed Mar 26 23:22:10 UTC 2025`

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

CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS     NAMES
9d2ccbd31a15   torizon/weston   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0028 - Apalis iMX6Q 2GB IT (WinEC)</summary>

**Job ID**: `701250`

**Date**: `Wed Mar 26 23:22:14 UTC 2025`

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
Hostname:                 apalis-imx6-10867545
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX6Q/D Module on Apalis Evaluation Board
Toradex version:          0028 V1.1D
Serial number:            10867545
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS     NAMES
c049bfabb1d6   torizon/weston   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0029 - Apalis iMX6D 512MB (WinEC)</summary>

**Job ID**: `701252`

**Date**: `Wed Mar 26 23:22:04 UTC 2025`

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

CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS     NAMES
27685d1c2bf7   torizon/weston   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0035 - Apalis iMX6D 1GB IT (WinEC)</summary>

**Job ID**: `701251`

**Date**: `Wed Mar 26 23:23:12 UTC 2025`

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
Hostname:                 apalis-imx6-10871505
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Apalis iMX6Q/D Module on Apalis Evaluation Board
Toradex version:          0035 V1.1C
Serial number:            10871505
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS     NAMES
29ecebcdb373   torizon/weston   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>

### **Colibri iMX8X**

<details>
<summary>✅ 0038 - Colibri iMX8QXP 2GB WB IT</summary>

**Job ID**: `701267`

**Date**: `Wed Mar 26 23:49:20 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
c85870307787   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0050 - Colibri iMX8QXP 2GB IT</summary>

**Job ID**: `701269`

**Date**: `Wed Mar 26 23:41:24 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
77f4a9bb10b7   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0051 - Colibri iMX8DX 1GB WB</summary>

**Job ID**: `701264`

**Date**: `Wed Mar 26 23:44:52 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
a497765d75c4   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0052 - Colibri iMX8DX 1GB</summary>

**Job ID**: `701266`

**Date**: `Wed Mar 26 23:48:50 UTC 2025`

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

CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS     NAMES
590dc1cb5c51   torizon/weston-imx8   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>

### **Colibri iMX7**

<details>
<summary>✅ 0039 - Colibri iMX7D 1GB</summary>

**Job ID**: `701259`

**Date**: `Wed Mar 26 23:39:57 UTC 2025`

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

CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS     NAMES
695dc3d0a869   torizon/weston   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>

### **Colibri iMX6ULL**

<details>
<summary>✅ 0062 - Colibri iMX6ULL 1GB IT</summary>

**Job ID**: `701260`

**Date**: `Wed Mar 26 23:45:53 UTC 2025`

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

CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS     NAMES
da38bd35109b   torizon/weston   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>

### **Colibri iMX6**

<details>
<summary>✅ 0015 - Colibri iMX6DL 512MB (WinEC)</summary>

**Job ID**: `701262`

**Date**: `Wed Mar 26 23:49:51 UTC 2025`

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
Hostname:                 colibri-imx6-10519608
------------------------------------------------------------

Hardware info
------------------------------------------------------------
HW model:                 Toradex Colibri iMX6DL/S on Colibri Evaluation Board V3
Toradex version:          0015 V1.1A
Serial number:            10519608
Processor arch:           armv7l
------------------------------------------------------------
```

**Docker Containers**:
```
> docker ps -a

CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS     NAMES
2bf23faea41f   torizon/weston   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>


<details>
<summary>✅ 0017 - Colibri iMX6DL 512MB IT (WinEC)</summary>

**Job ID**: `701263`

**Date**: `Wed Mar 26 23:41:01 UTC 2025`

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

CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS     NAMES
90fbac4abbee   torizon/weston   "/bin/sh -c '/usr/bi…"   About a minute ago   Up About a minute             1_custom-tests-weston-1
```
</details>
