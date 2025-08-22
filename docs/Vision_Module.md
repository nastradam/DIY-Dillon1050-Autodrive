# Vision Module (Optional)

Split into two camera paths:

1. **Orientation Camera**: verifies bullet presence and orientation before seating.
2. **OAL + Finished-Round Counter Camera**: measures projected overall length (OAL) window and counts completed rounds.

### Implementation Notes
- Raspberry Pi Camera Module v3 or USB UVC cams.
- Controlled lighting (LED ring/bar) for consistent detection.
- Tunable thresholds; hard-stop on persistent failures beyond N occurrences.
- Performance: prefer ROI cropping + grayscale processing; optionally offload to USB Coral if future ML is desired.
