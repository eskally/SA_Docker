from flask import Flask, render_template
import requests
import time
import base64

app = Flask(__name__)

SERVER_URL = "http://localhost:5001/image"  # Uporabi localhost za lokalno testiranje

@app.route('/')
def index():
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            img_data = response.json()['image'] # pridobi sliko iz json objekta
            return render_template('index.html', image_data=img_data)
        else:
            return f"Napaka pri pridobivanju slike: {response.status_code}", 500
    except requests.exceptions.RequestException as e:
        return f"Napaka pri povezavi s strežnikom: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)