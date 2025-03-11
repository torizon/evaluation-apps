# Chromium Kiosk Mode #

![Torizon Version](https://img.shields.io/badge/Torizon_OS-6.8.1-blue?logo=torizon)
&nbsp;
![Torizon Container](https://img.shields.io/badge//torizon/chromium-3-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//torizon/chromium--vivante-3-blue?logo=docker)
&nbsp;
![Torizon Container](https://img.shields.io/badge//torizon/chromium--am62-3-blue?logo=docker)

This application runs the Chromium web browser in **kiosk** mode.

![Screenshot](./screenshot.png)

## About

Chromium is an open-source browser project that aims to build a safer, faster, and more stable way for all users to experience the web.

In kiosk mode, the browser:

- Opens in fullscreen an URL defined under the "command" tag in the **docker-compose.yml**;
- Does not show error messages/popups;
- Does not allow the user to navigate to different websites using the browser's navigation bar.

## Requirements
To run this demo, you need:

- A supported Toradex SoM;
- Display;
- Torizon OS installed;
- Internet Connectivity.


## Deploy from the Torizon Cloud

- [Chromium Kiosk Mode Demo](https://www.torizon.io/chromium-kiosk-mode);

## More Resources

- [Web Browser in kiosk mode](https://developer.toradex.com/torizon/application-development/use-cases/gui/web-browser-kiosk-mode-with-torizoncore/);
- [Torizon Containers Github](https://github.com/torizon/torizon-containers/tree/oldstable/debian-docker-images/imx/chromium).