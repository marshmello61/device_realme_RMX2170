# Orange Fox Recovery Project Device Tree for Realme X3/ X3 Superzoom.

## Features

Works:

- OZIP Installation
- Fastbootd
- Almost EveryThing

## Compile

First Download OFox Sources:

```
mkdir ~/OrangeFox_10
cd ~/OrangeFox_10
rsync rsync://sources.orangefox.download/sources/fox_10.0 . --progress -a
cd ~/OrangeFox_10/fox_10.0
```

Clone this device repository:

```
git clone https://github.com/nishant6342/device_realme_X3_ofox -b fox_11.0 device/realme/RMX2081
```

Finally execute these:

```
. build/envsetup.sh
lunch omni_RMX2081-userdebug
mka recoveryimage
```

To test it:

```
fastboot boot out/target/product/RMX2081/recovery.img
```

Thanks to @imjyotiraditya and @siddharthbhardwaj , Tree is possible cause of them 
