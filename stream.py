import os
import subprocess

# আপনার m3u8 লিংক
m3u8_url = "https://cdn.jsdelivr.net/gh/srhady/Fancode-bd/raw_link/zimbabwe_vs_bangladesh_143400_english.m3u8"

# GitHub Secrets থেকে ফেসবুক স্ট্রিম কি সংগ্রহ
stream_key = os.getenv("FB_STREAM_KEY")

if not stream_key:
    print("Error: FB_STREAM_KEY পাওয়া যায়নি! দয়া করে GitHub Secrets এ এটি সেট করুন।")
    exit(1)

rtmp_url = f"rtmps://live-api-s.facebook.com:443/rtmp/{stream_key}"

# টারমাক্সে কাজ করা সেই অরিজিনাল কমান্ড
command = [
    "ffmpeg",
    "-i", m3u8_url,
    "-c", "copy",
    "-f", "flv",
    rtmp_url
]

print("গিটহাব সার্ভার থেকে ফেসবুকে লাইভ শুরু হচ্ছে...")
subprocess.run(command)
