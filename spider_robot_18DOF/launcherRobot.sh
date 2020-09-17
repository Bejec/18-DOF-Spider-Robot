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
# mkdir /home/pi/logs
# run sudo crontab -e
# add line in file and save
# @reboot sh /home/pi/Projects/spider-robot-18DOF/spider_robot_18DOF/launcherRobot.sh >/home/pi/logs/cronlog 2>&1
# sudo reboot and confirm that spiderRobot.py verbose shows up in cat /logs/cronlog

touch /dev/shm/ctr
touch /dev/shm/rtc
touch /dev/shm/vid
cd /
cd home/pi/Projects/spider-robot-18DOF/spider_robot_18DOF
sudo python3 spiderRobot.py
cd /
