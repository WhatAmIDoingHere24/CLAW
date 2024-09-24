#!/bin/bash

if ! [ $(id -u) = 0 ]; then
    echo "run this in root"
exit 1
fi

echo "script begins..."
if ( ! sudo ufw status); then
    sudo apt install ufw
fi
sudo systemctl enable ufw --now
sudo ufw enable
sudo ufw logging on
sudo ufw deny 20:9999/tcp
echo "done securing ufw, bye bye"
