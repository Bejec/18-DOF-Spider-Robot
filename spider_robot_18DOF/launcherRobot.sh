#!/bin/sh
# launcherRobot.sh
# navigate to home directory, then to this directory, then execute python script, then back home
# https://medium.com/@arslion/starting-python-gui-program-on-raspberry-pi-startup-56fb4e451cc1
# Need to create launcher.desktop file in ~/.config/autostart and fill it with:
# [Desktop Entry]
# Name=spiderController
# Type=Application
# Comment=runs spider Controller
# Exec=/usr/bin/python /home/pi/Projects/spider-robot-18DOF/spider_robot_18DOF/spiderController.py
# then to make it executable
# chmod +x /home/pi/.config/autostart/launcher.desktop
touch /dev/tmp/ctr
touch /dev/tmp/rtc
touch /dev/tmp/vid
cd /
cd home/pi/Projects/spider-robot-18DOF/spider_robot_18DOF
sudo python3 spiderRobot.py
cd /
