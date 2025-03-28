from flask import Flask, jsonify
import cv2
import base64

app = Flask(__name__)

camera = cv2.VideoCapture(0) 
if not camera.isOpened():
    print("Ne morem odpreti kamere!")
    exit()

def capture_and_encode():
    ret, frame = camera.read()
    if not ret:
        print("Ne morem zajeti slike!")
        return None

    ret, buffer = cv2.imencode('.jpg', frame)
    if not ret:
        print("Ne morem kodirati slike!")
        return None

    img_str = base64.b64encode(buffer).decode('utf-8')
    return img_str

@app.route('/image')
def image():
    img_data = capture_and_encode()
    if img_data:
        return jsonify({'image': img_data})
    else:
        return "Ni slike na voljo", 500

@app.route('/is_camera_working')
def is_camera_working():
    if camera.isOpened():
        return jsonify({'status': 'OK'})
    else:
        return jsonify({'status': 'ERROR'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)