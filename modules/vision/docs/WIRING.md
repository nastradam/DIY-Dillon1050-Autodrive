# Wiring (RPi 5)

**Common ground** between 12 V and Pi 0 V is required.

- **Hall‑effect (cycle index):**
  - OUT → GPIO17 (BCM) with pull‑up
  - VCC → 3V3, GND → GND

- **IR Break‑beam (optional counter assist):**
  - OUT → GPIO22 (BCM) (level shift if 5 V logic)

- **Reject Solenoid (12 V):**
  - Solenoid + → 12 V
  - Solenoid − → MOSFET Drain; MOSFET Source → GND
  - Gate → GPIO27 via 220 Ω; flyback diode across coil

- **Cameras:**
  - Cam A → CSI0 (or USB UVC)
  - Cam B → CSI1 (or USB UVC)
  - Use strain relief; avoid motor wiring for EMI.

**Recommended:** Shielded sensor cable, TVS on 12 V, separate lighting supply if flicker observed.
