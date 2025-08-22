# GUI Spec

## Goals
- Primary machine control and diagnostics on a Pi touchscreen
- Access to **Settings**, **Production Logs**, **Batch/Lot**, **Errors**, **Maintenance**, **Vision**, and **Powder** modules
- Same UI served over LAN for phones/tablets

## Main Screens
1. **Home / Run**: Start/Stop, cycle rate, status, active alarms, cycle position
2. **Setup**: Caliber profile, stroke settings, motor tuning, sensor calibration
3. **Production Log**: Current batch run; round count; finished-round rate; OAL stats
4. **QC**: Case gauge results, velocity notebook, lot notes
5. **Vision**: Live feed thumbnails; pass/fail counts; thresholds
6. **Maintenance**: Interval counters, tasks due, acknowledgements
7. **Errors/Alarms**: History with root causes and corrective actions
8. **Settings**: Network, API keys, backups/export

## Technical
- Served by FastAPI backend; lightweight HTML/JS front-end
- Responsive layout for 7–10" touch and mobile devices
