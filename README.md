# DIY Dillon 1050 Autodrive

Open-source, DIY-friendly autodrive system for the Dillon Super 1050/1100 platform with optional vision, powder safety, production/QC logging, and networked touchscreen UI.

**Current Release:** v0.1.0 — August 21, 2025

## Highlights
- Motorized press stroke with safety interlocks and hard-stop logic
- Integrated **Error Logging** and **Maintenance Logging** modules
- **Data & Production Logging**: batches, lots, load data, QC, chronograph velocities
- **Vision Module (optional)**: bullet orientation verification; OAL tolerance + finished-round counter
- **Optical Powder Check (optional)**: camera-based powder charge verification
- **Low Powder Alarm (optional)**: hopper level sensors with round-count estimates per fill
- **Powder Check & Low Primer Integration**: tie into Dillon switches for automatic stops
- **Touch UI** on a Raspberry Pi with local web app (LAN-accessible)
- Open data model (SQLite) and REST API (FastAPI) for analytics/apps

> This repo is part of the larger Dillon Autoloader project. See **docs/Traceability_Matrix.md** for chat-to-feature mapping and **docs/Roadmap.md** for next steps.

## Repository Layout
```
/
├─ README.md
├─ VERSION
├─ CHANGELOG.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ .gitignore
├─ bom/
│  ├─ BOM.xlsx
│  ├─ BOM.csv
│  └─ BOM.pdf
├─ docs/
│  ├─ System_Overview.md
│  ├─ Architecture.mmd
│  ├─ Wiring_Diagram.mmd
│  ├─ GUI_Spec.md
│  ├─ GUI_Wireframes.mmd
│  ├─ Logging_Modules.md
│  ├─ Data_Production_Logging.md
│  ├─ Vision_Module.md
│  ├─ Optical_Powder_Check.md
│  ├─ Low_Powder_Alarm.md
│  ├─ Low_Primer_Stop.md
│  ├─ Powder_Check_Integration.md
│  ├─ Controller_Comparison.md
│  ├─ Reverse_Engineering_Mark7.md
│  ├─ Sensors_Integration.md
│  ├─ Safety.md
│  ├─ BOM_Notes.md
│  ├─ Versioning.md
│  ├─ Repo_Update_Instructions.md
│  ├─ Roadmap.md
│  └─ Traceability_Matrix.md
├─ software/
│  └─ pi/
│     ├─ main.py
│     ├─ config.yaml
│     ├─ motor_control.py
│     ├─ sensors.py
│     ├─ powder_check.py
│     ├─ vision/
│     │  ├─ __init__.py
│     │  ├─ orientation.py
│     │  └─ oal_counter.py
│     ├─ logging/
│     │  ├─ __init__.py
│     │  ├─ error_log.py
│     │  ├─ maintenance_log.py
│     │  └─ production_log.py
│     └─ ui_server/
│        ├─ app.py
│        ├─ static/
│        └─ templates/
├─ hardware/
│  ├─ wiring_diagram.md
│  └─ parts_mounts.md
├─ diagrams/
│  └─ architecture.mmd
└─ db/
   └─ schema.sql
```

## Quick Start (Dev)
1. **Clone** and open repo.
2. Flash Raspberry Pi OS (Lite or Full). Enable SSH + camera interfaces.
3. `python3 -m venv .venv && source .venv/bin/activate`
4. `pip install -r docs/Versioning.md` (placeholder for dependency list; see `software/pi/ui_server/app.py` requirements header)
5. `python software/pi/ui_server/app.py` to run the API + UI locally.
6. Open the UI from the Pi touchscreen or any browser on the LAN.

> Safety first: See **docs/Safety.md**. Always dry-run without primers/powder before live testing.
