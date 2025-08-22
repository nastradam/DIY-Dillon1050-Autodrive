# Low Powder Alarm (Optional)

Two implementation options:
1. **Dual IR Break-Beam** (High/Low levels) — simple thresholds.
2. **Top-Mounted ToF** (VL53L0X) — measures hopper surface height; estimates rounds remaining per powder density and caliber.

Raises alarm and stops the machine at low threshold; logs event with estimated remaining rounds from last calibration.
