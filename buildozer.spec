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
# 补充必要权限：存储+振动+网络（模拟接口调用）
android.permissions = INTERNET,VIBRATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
# 必须加NDK版本，否则打包失败
android.ndk = 25b
# 支持主流手机架构
android.archs = arm64-v8a, armeabi-v7a
# 允许写入外部存储
android.add_android_manifest_uses_permission = android.permission.WRITE_EXTERNAL_STORAGE
android.build_tools = 31.0.0
