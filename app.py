from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "DaddyLive API is Running Perfectly! 🔥 Use /stream?id=YOUR_CHANNEL_ID"

@app.route('/stream')
def get_stream():
    channel_id = request.args.get('id')
    if not channel_id:
        return Response("#EXTM3U\n# Error: No ID provided", mimetype='text/plain')

    # ডাইনামিক URL তৈরি (id অনুযায়ী premium91, premium65 ইত্যাদি হবে)
    target_url = f"https://zotos.voglempanis.online/premium{channel_id}/tracks-v1a1/mono.css"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://donis.jimpenopisonline.online/",
        "Origin": "https://donis.jimpenopisonline.online"
    }

    try:
        r = requests.get(target_url, headers=headers, timeout=10)
        
        if r.status_code == 200:
            # প্লেয়ারকে ধোঁকা দেওয়ার জন্য Content-Type পরিবর্তন
            return Response(r.text, mimetype='application/x-mpegURL')
        else:
            return Response(f"#EXTM3U\n# Error: HTTP {r.status_code}", mimetype='text/plain')
            
    except Exception as e:
        return Response(f"#EXTM3U\n# Error: {str(e)}", mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
