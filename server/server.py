from flask import Flask, jsonify
import cv2
import base64
import time
from threading import Thread

app = Flask(__name__)

camera = cv2.VideoCapture(0)  
if not camera.isOpened():
    print("Ne morem odpreti kamere!")
    exit()

image_data = None

def capture_and_encode():
    global image_data
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Ne morem zajeti slike!")
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            print("Ne morem kodirati slike!")
            break

        image_data = base64.b64encode(buffer).decode('utf-8')
        time.sleep(10)  # Zajemi sliko vsakih 10 sekund

    camera.release()

@app.route('/image')
def image():
    global image_data
    if image_data:
        return jsonify({'image': image_data})
    else:
        return "Ni slike na voljo", 500

@app.route('/is_camera_working')
def is_camera_working():
    if camera.isOpened():
        return jsonify({'status': 'OK'})
    else:
        return jsonify({'status': 'ERROR'})

if __name__ == '__main__':
    # Zaženi zajemanje slik v ločeni niti
    capture_thread = Thread(target=capture_and_encode)
    capture_thread.daemon = True  # Zapri nit, ko se aplikacija zapre
    capture_thread.start()

    app.run(debug=True, host='0.0.0.0', port=5001)