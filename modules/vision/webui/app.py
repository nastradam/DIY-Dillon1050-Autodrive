import os, json, yaml
from flask import Flask, request, jsonify
import numpy as np, cv2

from ..orientation.pipeline import analyze_orientation
from ..oal_counter.pipeline import measure_oal

app = Flask(__name__)
CFG_COMMON = {}
CFG_O = {}
CFG_B = {}

def load_cfg():
    global CFG_COMMON, CFG_O, CFG_B
    with open('modules/vision/config/common.yaml') as f: CFG_COMMON = yaml.safe_load(f)
    with open('modules/vision/config/orientation.yaml') as f: CFG_O = yaml.safe_load(f)
    with open('modules/vision/config/oal_counter.yaml') as f: CFG_B = yaml.safe_load(f)

@app.route('/api/orientation', methods=['POST'])
def api_orientation():
    file = request.files.get('frame')
    if not file: return jsonify({'error':'no frame'}), 400
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    x,y,w,h = CFG_O['camera']['roi']
    roi = img[y:y+h, x:x+w]
    res = analyze_orientation(roi)
    return jsonify(res)

@app.route('/api/oal', methods=['POST'])
def api_oal():
    file = request.files.get('frame')
    if not file: return jsonify({'error':'no frame'}), 400
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    x,y,w,h = CFG_B['camera']['roi']
    roi = img[y:y+h, x:x+w]
    ppm = CFG_B['oal']['px_per_mm']
    res = measure_oal(roi, ppm)
    return jsonify(res)

@app.route('/api/health')
def health():
    return jsonify({'status':'ok'})

if __name__ == '__main__':
    load_cfg()
    app.run(host='0.0.0.0', port=8080)
