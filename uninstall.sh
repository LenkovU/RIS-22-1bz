#!/bin/bash

sudo systemctl disable display_control.service
sudo systemctl stop display_control.service
sudo rm -rf /etc/systemd/system/motion-display-control.service
sudo rm -rf /usr/local/bin/display_control.py

echo "done."
