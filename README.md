# Orange Fox Recovery Project Device Tree for Realme X3/ X3 Superzoom.

## Features

Works:

- OZIP Installation
- Fastbootd
- Almost EveryThing

OrangeFox Recovery Project (OFRP) R11 for realme X3 (RMX2081/5)

How to build
Check OFRP official guide https://wiki.orangefox.tech/en/dev/building

Fix decryption on Android 11 (RUI2.0) thanks @logotoy73 and @Ctapchuk

To provide decryption /data on Android 11 with keymaster@4.0 you need to fix some things like: mounting binderfs
--Apply these commits to the required repositories to fix the binderfs mount error (now the recovery will not get stuck on the splash screen):
https://github.com/omnirom/android_system_sepolicy/commit/50c5d731e0aa4098aac293e4024b213b5c445b99
https://github.com/omnirom/android_system_sepolicy/commit/74affd140396b74840e5dd8018b423ffcbe25a18
https://github.com/TeamWin/android_bootable_recovery/commit/cd79c90d27941edbda6a92593835aec2a99c2ee9

Next, you need to fully enable decryption in your device tree.
In order for the decryption /data to work, you need to use the AVB from the stock recovery (TWRP/OFRP cannot provide the required AVB at the moment). To do this, you need to disable the AVB flags in your tree. After compiling the recovery image, you need to flash the stock recovery first and then the custom recovery.
