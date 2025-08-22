import cv2, numpy as np, yaml, argparse, time, os

def analyze_orientation(frame_bgr):
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3,3), 0)
    edges = cv2.Canny(gray, 60, 180)
    cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        return {"ok": False, "reason": "no_bullet"}
    c = max(cnts, key=cv2.contourArea)
    rect = cv2.minAreaRect(c)
    (cx, cy), (w, h), ang = rect
    aspect = max(w,h)/max(1.0, min(w,h))
    M = cv2.moments(c)
    if M['m00']==0: return {"ok": False, "reason": "zero_moment"}
    mx, my = M['m10']/M['m00'], M['m01']/M['m00']
    h_, w_ = gray.shape
    offset_px = ((mx-w_/2)**2 + (my-h_/2)**2)**0.5
    return {"ok": aspect>1.1, "aspect": float(aspect), "centroid_offset_px": float(offset_px)}

def main(cfg_path):
    with open(cfg_path,'r') as f: cfg = yaml.safe_load(f)
    src = cfg['camera']['source']
    cap = cv2.VideoCapture(0 if src=='/dev/video0' else src if src.isdigit() else src)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cfg['camera']['width'])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cfg['camera']['height'])
    while True:
        ok, frame = cap.read()
        if not ok: break
        x,y,w,h = cfg['camera']['roi']
        roi = frame[y:y+h, x:x+w]
        res = analyze_orientation(roi)
        print(res)
        if cv2.waitKey(1)==27: break

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', required=True)
    args = ap.parse_args()
    main(args.config)
