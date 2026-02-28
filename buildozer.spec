[app]
title = 抖音手机号提取器
package.name = douyinphoneextractor
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.1,plyer,openpyxl
orientation = portrait
fullscreen = 0

[android.permissions]
INTERNET
VIBRATE
WRITE_EXTERNAL_STORAGE
READ_EXTERNAL_STORAGE

[android]
android.permissions = INTERNET,VIBRATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
