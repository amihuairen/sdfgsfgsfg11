[app]
title = 抖音手机号提取器
package.name = douyinphoneextractor
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
# 补充主程序文件（必须写！否则打包找不到入口）
source.main.py = main.py  # 替换成你实际的 py 文件名，比如 mina.py
version = 1.0
requirements = python3,kivy==2.3.1,plyer,openpyxl
orientation = portrait
fullscreen = 0

# 注意：[android.permissions] 这个节是无效的，权限要写在 [android] 节里
[android]
# 权限合并到这里，格式正确
android.permissions = INTERNET,VIBRATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
# 补充关键配置（避免打包兼容问题）
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
