import cv2, numpy as np, yaml, argparse, time

def measure_oal(frame_bgr, px_per_mm=10.0, H=None):
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3,3), 0)
    if H is not None:
        h, w = gray.shape
        gray = cv2.warpPerspective(gray, H, (w, h))
    edges = cv2.Canny(gray, 60, 180)
    proj = edges.sum(axis=0)
    xs = np.where(proj>0)[0]
    if xs.size<2:
        return {"ok": False, "reason": "edges_not_found"}
    left, right = int(xs.min()), int(xs.max())
    oal_px = right-left
    mm = oal_px/max(1e-6, px_per_mm)
    return {"ok": True, "oal_mm": float(mm), "oal_in": float(mm/25.4)}

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
        res = measure_oal(roi, cfg['oal']['px_per_mm'])
        print(res)
        if cv2.waitKey(1)==27: break

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', required=True)
    args = ap.parse_args()
    main(args.config)
