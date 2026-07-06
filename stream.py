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

# FFmpeg কমান্ড আপডেট করা হয়েছে (Map যুক্ত করে)
command = [
    "ffmpeg",
    "-i", m3u8_url,
    "-map", "0:v:0",  # লিংক থেকে শুধুমাত্র প্রথম/প্রধান ভিডিও স্ট্রিমটি নেবে
    "-map", "0:a:0",  # লিংক থেকে শুধুমাত্র প্রথম/প্রধান অডিও স্ট্রিমটি নেবে
    "-c", "copy",
    "-f", "flv",
    rtmp_url
]

print("গিটহাব সার্ভার থেকে ফেসবুকে লাইভ শুরু হচ্ছে...")
subprocess.run(command)
