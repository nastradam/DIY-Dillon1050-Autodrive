# DIY-Dillon1050-Autodrive

Open-source automation stack for a Dillon 1050 using a **Ponsness Warren autodrive base**, a **motor upgrade**, and a **Raspberry Pi** controller with sensors and vision.

**Safety & Liability**  
Modifying reloading presses and automating them introduces serious risk of injury or property damage. You are responsible for design, assembly, testing, and safe operation. Use physical guards, hardwired E-Stops, and conservative speeds during commissioning. Manufacturer warranties may be void.

## Highlights
- Re-use Ponsness Warren autodrive frame + linkage.
- Upgrade to AC servo for smoother control and reliable torque.
- Raspberry Pi control with isolated I/O.
- Sensors for primer/powder/brass/bullet runout and binding detection via load cell.
- Vision (OpenCV) for bullet orientation and optional OAL checks.
- Round counting, batch limits, alarms, and auto-stop.

## Structure
```
/BOM
  BOM.csv
/docs
  wiring-diagram-v1.png
  README-BOM.md
  mechanical-mounts.md
/code
  pi-control.py
  vision-inspection.py
  round-counter.py
/hardware
  motor-mount-plate.stl
  camera-bracket.stl
```
