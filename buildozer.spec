[app]
title = 抖音手机号提取器
package.name = douyinphoneextractor
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
# 关键：主程序文件是mina.py
source.main.py = mina.py
version = 1.0
# 补充依赖：android（处理手机权限）、openpyxl（已加）、plyer（已加）
requirements = python3,kivy==2.3.1,plyer,openpyxl,android
orientation = portrait
fullscreen = 0

[android]
android.permissions = INTERNET,VIBRATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 23c
android.archs = arm64-v8a, armeabi-v7a
android.add_android_manifest_uses_permission = android.permission.WRITE_EXTERNAL_STORAGE
android.build_tools = 30.0.3
# 强制指定SDK下载源，避开预览版
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r23c
