import os
import subprocess
import sys

# আপনার নতুন Fancode 720p m3u8 লিংক
m3u8_url = "https://bd-mc-flive.fancode.com/mumbai/143400_english_hls_a55273fc7252729_1ta-di_h264/720p.m3u8?hdntl=Expires=1783407904~_GO=Generated~acl=/mumbai/143400_english_hls_a55273fc7252729_1ta-di_h264/*~Signature=Ac2BFelVHfaT_lKZtydXvHRuVlMgi6ZH4bq7Tuabat5_RfJabYq3YTIhFzYwHBXt8_HCvOHQYxOmz4hBBbRDYCcZSB4H"

# GitHub Secrets থেকে ফেসবুক স্ট্রিম কি সংগ্রহ
stream_key = os.getenv("FB_STREAM_KEY")

if not stream_key:
    print("Error: FB_STREAM_KEY পাওয়া যায়নি!")
    sys.exit(1)

rtmp_url = f"rtmps://live-api-s.facebook.com:443/rtmp/{stream_key}"

# ffmpeg কমান্ড (User-Agent যুক্ত করা হয়েছে ব্লক এড়ানোর জন্য)
command = [
    "ffmpeg",
    "-user_agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "-i", m3u8_url,
    "-c", "copy",
    "-f", "flv",
    rtmp_url
]

print("নতুন লিংক দিয়ে ফেসবুকে লাইভ শুরু হচ্ছে...")

# check=True দেওয়া হয়েছে যাতে কোনো এরর হলে গিটহাব লগে লাল কালিতে ধরা পড়ে
try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"ffmpeg Error: লাইভ স্ট্রিম কোনো কারণে বন্ধ হয়ে গেছে বা লিংক কাজ করছে না।")
    sys.exit(1)
