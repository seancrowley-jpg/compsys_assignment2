#!/bin/sh
. ./eddy.conf
echo "Disabling virtual Eddystone Beacon..."
sudo hciconfig $BLUETOOTH_DEVICE noleadv
echo "Complete"
