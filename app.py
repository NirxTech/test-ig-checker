from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_followers():
    followers_file = request.files['followers_file']
    following_file = request.files['following_file']

    try:
        followers_data = json.load(followers_file)
        following_data = json.load(following_file)
    except Exception:
        return render_template('index.html', error="File JSON tidak valid!")

    try:
        followers_usernames = {
            item['string_list_data'][0]['value']
            for item in followers_data
            if 'string_list_data' in item and item['string_list_data']
        }
    except Exception as e:
        return render_template('result.html', error=f"Format followers.json salah: {e}")

    try:
        following_usernames = {
            item['string_list_data'][0]['value']
            for item in following_data.get('relationships_following', [])
            if 'string_list_data' in item and item['string_list_data']
        }
    except Exception as e:
        return render_template('index.html', error=f"Format following.json salah: {e}")

    not_following_back = following_usernames - followers_usernames
    not_followed_back = followers_usernames - following_usernames

    return render_template('result.html', not_following_back=sorted(not_following_back), not_followed_back=sorted(not_followed_back))

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)