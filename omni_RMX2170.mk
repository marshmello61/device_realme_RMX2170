#
# Copyright 2021 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

# Release name
PRODUCT_RELEASE_NAME := RMX2170

# Inherit from hardware-specific part of the product configuration
$(call inherit-product, $(SRC_TARGET_DIR)/product/base.mk)

# Inherit from our custom product configuration
$(call inherit-product, vendor/omni/config/common.mk)

## Device identifier. This must come after all inclusions
PRODUCT_DEVICE := RMX2170
PRODUCT_NAME := omni_RMX2170
PRODUCT_BRAND := realme
PRODUCT_MODEL := realme 7 pro
PRODUCT_MANUFACTURER := realme

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRODUCT_NAME=RMX2170 \
    BUILD_PRODUCT=RMX2170 \
    TARGET_DEVICE=RMX2170

# Inherit device-specific stuffs
$(call inherit-product, device/realme/RMX2170/device.mk)
