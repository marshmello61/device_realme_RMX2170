#
# Copyright (C) 2020 The AOSP Project
#
# SPDX-License-Identifier: Apache-2.0
#

LOCAL_PATH := $(call my-dir)

ifeq ($(TARGET_DEVICE),RMX2170)
$(call add-radio-file,dynamic-remove-oppo)

include $(call all-makefiles-under,$(LOCAL_PATH))

endif
