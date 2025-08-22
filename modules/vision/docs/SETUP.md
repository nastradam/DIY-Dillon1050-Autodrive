# Vision Module – Setup

## 1) System packages (RPi OS/Debian)
```bash
sudo apt-get update
sudo apt-get install -y python3-opencv python3-venv python3-pip libatlas-base-dev libgpiod2 gpiod
```

## 2) Python env
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r modules/vision/requirements.txt
```

## 3) Hardware & lighting
- Cam A (Orientation): backlit case‑mouth region + ring fill.
- Cam B (OAL/Counter): strong backlight (panel or line light) forming a silhouette.
- Fix focus, disable auto‑exposure; set short exposure to freeze motion (1/2000–1/4000s equivalent).

## 4) Configuration
- Global settings: `modules/vision/config/common.yaml`
- Orientation pipeline: `modules/vision/config/orientation.yaml`
- OAL/Counter pipeline: `modules/vision/config/oal_counter.yaml`

Set:
- ROI for each camera
- Phase windows (degrees)
- OAL target/tolerances (inches)
- GPIO pins for hall sensor, break‑beam, reject solenoid

## 5) Calibration
- **OAL px/mm:** Place a scale (or calibration target) in the same plane as the cartridge path; run the UI to compute px/mm and save to `oal_counter.yaml`.
- **Perspective:** If camera isn’t perfectly orthogonal, compute & save homography; the web UI offers a guided procedure.
- **Thresholds:** Run ~50 rounds, compute mean±σ and set soft/hard tolerances accordingly.

## 6) Safety interlocks
- Hard‑fail → stop press, sound buzzer, log image.
- Soft‑fail → configurable: warn, auto‑reject, or stop.
