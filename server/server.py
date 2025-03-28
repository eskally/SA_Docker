from flask import Flask, jsonify
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # Poskusi 0, 1, itd.
if not camera.isOpened():
    print("Ne morem odpreti kamere!")
    exit()

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/is_camera_working')
def is_camera_working():
    if camera.isOpened():
        return jsonify({'status': 'OK'})
    else:
        return jsonify({'status': 'ERROR'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)