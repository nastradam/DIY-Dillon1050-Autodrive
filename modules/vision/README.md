# Vision Module (Add‑On)

This module adds **two machine‑vision functions** to the Dillon Autoloader project:

- **Orientation Camera (Cam A):** Confirms projectile is base‑down/tip‑up and aligned to the case mouth before seating.
- **OAL + Finished‑Round Counter (Cam B):** Measures **overall length (OAL)** after seating/crimp, enforces tolerances, and **counts finished rounds**, optionally actuating a reject gate.

**Controller:** Raspberry Pi 5 recommended (Pi 4 supported with reduced throughput).  
**Approach:** Classical OpenCV pipelines with deterministic, phase‑triggered single‑frame capture per cycle. Optional Coral TPU / DepthAI upgrades.

Quick links:
- Setup: `docs/SETUP.md`
- Wiring: `docs/WIRING.md`
- BOM additions: `docs/BOM.md`

## Running (per submodule)
```bash
# Orientation only
python -m modules.vision.orientation.run_orientation --config modules/vision/config/orientation.yaml

# OAL + Counter only
python -m modules.vision.oal_counter.run_oal_counter --config modules/vision/config/oal_counter.yaml

# Web UI (both, mock or live per config)
./modules/vision/scripts/run_webui.sh
```
