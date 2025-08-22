# BOM Additions – Vision Add‑On

> Source from Adafruit / Amazon when possible; alternatives noted.

## Core
- Raspberry Pi 5 (8 GB) or Pi 4 (4–8 GB)
- Pi HQ Camera (IMX477) ×1 (Cam B – OAL)
- Pi Global Shutter Camera (IMX296) ×1 (Cam A – Orientation) — reduces motion artifacts
- C‑mount lenses: 16 mm (Cam A), 16–25 mm (Cam B) low‑distortion
- LED ring light (Cam A) + 12 V dimmer/driver
- Backlight panel or line light (Cam B) 50–100 mm
- Hall‑effect sensor + 10×3 mm magnet
- IR break‑beam pair (optional)
- N‑MOSFET driver (e.g., IRLZ44N or logic‑level MOSFET) + diode
- 12 V solenoid/servo gate for reject
- Shielded cable, connectors (M8/M12 optional), mounting brackets (2020 extrusion)

## Optional Upgrades
- Google Coral USB (Edge TPU) for orientation classifier
- Luxonis OAK‑1/‑D to offload one stream (DepthAI)
- Telecentric lens for metrology‑grade OAL accuracy
- Jetson Orin Nano (if running ML + UI at high RPM)

## Consumables/Docs
- Adhesive stainless metric scale (0.5 mm ticks)
- Printed calibration target (10 mm grid)
