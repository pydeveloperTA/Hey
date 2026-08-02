[app]

# --- Basic app info ---
title = Travel Assistant
package.name = travelassistant
package.domain = com.example
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

# --- Python / Android dependencies ---
requirements = python3,kivy==2.3.1,kivy_garden.mapview,pillow,requests,certifi,charset-normalizer,idna,urllib3,plyer,pyjnius,yt-dlp,mutagen,websockets

orientation = portrait
fullscreen = 0

# --- Permissions ---
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,ACCESS_NETWORK_STATE,POST_NOTIFICATIONS,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# --- Target Android SDK / NDK Configuration ---
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

# --- Use develop branch for modern p4a compatibility ---
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
