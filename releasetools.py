# Copyright (C) 2009 The Android Open Source Project
# Copyright (C) 2019 The Mokee Open Source Project
# Copyright (C) 2019 The LineageOS Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

def FullOTA_InstallBegin(info):
  data = info.input_zip.read("RADIO/dynamic-remove-oppo")
  common.ZipWriteStr(info.output_zip, "dynamic-remove-oppo", data)
  info.script.AppendExtra('update_dynamic_partitions(package_extract_file("dynamic-remove-oppo"));')

def FullOTA_InstallEnd(info):
  OTA_InstallEnd(info, False)

def IncrementalOTA_InstallEnd(info):
  OTA_InstallEnd(info, True)

def AddImageOnly(info, basename, incremental, firmware):
  if incremental:
    input_zip = info.source_zip
  else:
    input_zip = info.input_zip
  if firmware:
    data = input_zip.read("RADIO/" + basename)
  else:
    data = input_zip.read("IMAGES/" + basename)
  common.ZipWriteStr(info.output_zip, basename, data)

def AddImage(info, basename, dest, incremental):
  AddImageOnly(info, basename, incremental, False)
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (basename, dest))

def OTA_InstallEnd(info, incremental):
  info.script.Print("Patching dtbo and vbmeta images...")
  AddImage(info, "dtbo.img", "/dev/block/bootdevice/by-name/dtbo", incremental)
  AddImage(info, "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta", incremental)
  AddImage(info, "vbmeta_system.img", "/dev/block/bootdevice/by-name/vbmeta_system", incremental)
  Firmware_Images(info, incremental)

def Firmware_Images(info, incremental):
  img_map = {
      'abl': ['abl'],
      'aop': ['aop'],
      'BTFM': ['bluetooth'],
      'cdt_engineering': ['cdt_engineering'],
      'cmnlib': ['cmnlib'],
      'cmnlib64': ['cmnlib64'],
      'devcfg': ['devcfg'],
      'dpAP': ['apdp'],
      'DRIVER': ['DRIVER'],
      'dspso': ['dsp'],
      'hyp': ['hyp'],
      'imagefv': ['imagefv'],
      'keymaster64': ['keymaster'],
      'modem': ['modem'],
      'oppo_sec': ['oppo_sec'],
      'qupv3fw': ['qupfw'],
      'splash': ['splash'],
      'static_nvbk': ['oppostanvbk'],
      'storsec': ['storsec'],
      'tz': ['tz'],
      'uefisecapp': ['uefisecapp'],
      'xbl': ['xbl'],
      'xbl_config': ['xbl_config']
      }

  fw_cmd = '\n(\n'
  fw_cmd += 'ui_print("Flashing device specific firmware...");\n'

  # Flash Device Specific Firmware
  for img in img_map.keys():
    AddImageOnly(info, '{}.img'.format(img), incremental, True)
    for part in img_map[img]:
      fw_cmd += 'package_extract_file("{}.img", "/dev/block/bootdevice/by-name/{}");\n'.format(img, part)
  # END Flash Device Specific Firmware

  fw_cmd += ')\n);'
  info.script.AppendExtra(fw_cmd)
