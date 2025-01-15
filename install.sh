#!/bin/bash

curl -O https://github.com/LenkovU/RIS-22-1bz/blob/main/display_control.py
curl -O https://github.com/LenkovU/RIS-22-1bz/blob/main/display_control.service

if [ ! -d "/usr/local/bin" ]; then
  sudo mkdir -p /usr/local/bin
fi

sudo chmod +x display_control.py
sudo mv display_control.py /usr/local/bin
sudo mv display_control.service /etc/systemd/system
sudo systemctl start display_control.service
sudo systemctl enable display_control.service

echo "done."
