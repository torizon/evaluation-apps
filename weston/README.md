# Weston Desktop Environment #

![Torizon Version](https://img.shields.io/badge/Torizon_OS-6.8.1-blue?logo=torizon) 
&nbsp;
![Torizon Container](https://img.shields.io/badge//torizon/weston-3-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//torizon/weston--vivante-3-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//torizon/weston--am62-3-blue?logo=docker)

This app starts a standalone instance of Weston from where you can launch other applications like the weston-terminal Terminal Emulator.

![Screenshot](./screenshot.png)

A blank dark-blue screen.

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

- [Weston on Torizon OS](https://developer.toradex.com/torizon/application-development/working-with-containers/working-with-weston-on-torizoncore/);
- [Torizon Containers Github](https://github.com/torizon/torizon-containers/tree/oldstable/debian-docker-images/imx/weston);