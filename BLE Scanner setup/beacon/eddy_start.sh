#!/bin/sh
. ./eddy.conf
echo "Launching eddystone virtual beacon..."
sudo hciconfig $BLUETOOTH_DEVICE up
sudo hciconfig $BLUETOOTH_DEVICE noleadv
sudo hciconfig $BLUETOOTH_DEVICE leadv 3
sudo hcitool -i hci0 cmd 0x08 0x0008 $PAYLOAD
echo "Complete"
