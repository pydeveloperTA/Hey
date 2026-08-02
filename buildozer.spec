[app]

# --- Basic app info ---
title = Travel Assistant
package.name = travelassistant
package.domain = com.example
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf
# Buildozer's default entry point is a file named main.py in source.dir

# --- Python / Android dependencies ---
# Derived from this script's imports. Heavy stack (mapview + plyer + pyjnius +
# yt-dlp) - expect to tweak this line once or twice based on build log errors.
requirements = python3,kivy==2.3.1,kivy_garden.mapview,pillow,requests,certifi,charset-normalizer,idna,urllib3,openssl,plyer,pyjnius,yt-dlp,mutagen,pycryptodomex,brotli,websockets

orientation = portrait
fullscreen = 0

# icon.filename = %(source.dir)s/icon.png

# --- Permissions (matches what the app requests at runtime) ---
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,ACCESS_NETWORK_STATE,POST_NOTIFICATIONS,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 35
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

# If a build fails with a Gradle/Android-Gradle-Plugin version mismatch,
# uncomment the line below to use the development branch of python-for-android:
# p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
