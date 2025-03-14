# Codesys PCL #

![Torizon Version](https://img.shields.io/badge/Torizon_OS-6.8.1-blue?logo=torizon)
&nbsp;
![Torizon Container](https://img.shields.io/badge//toradexdemos/codesys_demo_arm32-4.13.0.0-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//toradexdemos/codesyscontrol_virtuallinuxarm-4.13.0.0-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//toradexdemos/codesys_demo_arm64-4.13.0.0-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//toradexdemos/codesyscontrol_virtuallinuxarm64-4.13.0.0-blue?logo=docker)

This demo deploys a **Codesys PCL** with a Simon Game intended for evaluation. 

![Screenshot](https://docs1.toradex.com/116543-demogallerycodesys.png?v=1)

## About

CODESYS is a SoftPLC solution that can be deployed to ARM-based devices in order to enable them to work as a PLC.

This demo uses the base **Codesys Virtual Control SL** image and the **Codesys Demo app** to deploy a virtual PLC.

Also, it is built on top of the [Weston](../weston/) and [Chromium](../chromium/) containers to create an visualization app for Human Machine Interface (HMI).

The demo can also be viewed without a screen attached to the module. From the browser on your host machine (connected to the same network), access:

```
http://<hostname>:8080/webvisu.htm
```

## Requirements
To run this demo, you need:

- A supported Toradex SoM;
- Display;
- Torizon OS installed;
- Internet Connectivity.


## Deploy from the Torizon Cloud

- [CODESYS Demo Applications](https://www.torizon.io/codesys-demo).

## More Resources

- [Codesys demo](https://developer.toradex.com/torizon/application-development/partner-containers/partner-demo-container-codesys);
- [How get the Device's Hostname](https://developer.toradex.com/software/development-resources/ssh/#using-the-hostname).