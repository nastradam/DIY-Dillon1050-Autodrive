-- SQLite schema for production/QC logging

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS calibers (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS component_lots (
  id INTEGER PRIMARY KEY,
  type TEXT NOT NULL, -- 'powder','brass','projectile','primer'
  brand TEXT,
  model TEXT,
  lot_code TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS batches (
  id INTEGER PRIMARY KEY,
  batch_code TEXT UNIQUE NOT NULL,
  caliber_id INTEGER NOT NULL,
  projectile_weight_gr REAL,
  projectile_type TEXT,
  powder_type TEXT,
  powder_charge_gr REAL,
  brass_lot_id INTEGER,
  primer_type TEXT,
  notes TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(caliber_id) REFERENCES calibers(id),
  FOREIGN KEY(brass_lot_id) REFERENCES component_lots(id)
);

CREATE TABLE IF NOT EXISTS production_runs (
  id INTEGER PRIMARY KEY,
  batch_id INTEGER NOT NULL,
  started_at TEXT DEFAULT CURRENT_TIMESTAMP,
  ended_at TEXT,
  press_rate_rpm REAL,
  total_rounds INTEGER DEFAULT 0,
  FOREIGN KEY(batch_id) REFERENCES batches(id)
);

CREATE TABLE IF NOT EXISTS run_events (
  id INTEGER PRIMARY KEY,
  run_id INTEGER NOT NULL,
  ts TEXT DEFAULT CURRENT_TIMESTAMP,
  type TEXT NOT NULL, -- 'start','stop','alarm','resume','note'
  subtype TEXT,
  message TEXT,
  cycle_position REAL,
  FOREIGN KEY(run_id) REFERENCES production_runs(id)
);

CREATE TABLE IF NOT EXISTS qc_oal_samples (
  id INTEGER PRIMARY KEY,
  run_id INTEGER NOT NULL,
  ts TEXT DEFAULT CURRENT_TIMESTAMP,
  oal_in REAL NOT NULL,
  pass INTEGER NOT NULL, -- 0/1
  FOREIGN KEY(run_id) REFERENCES production_runs(id)
);

CREATE TABLE IF NOT EXISTS qc_case_gauge (
  id INTEGER PRIMARY KEY,
  run_id INTEGER NOT NULL,
  ts TEXT DEFAULT CURRENT_TIMESTAMP,
  pass INTEGER NOT NULL, -- 0/1
  FOREIGN KEY(run_id) REFERENCES production_runs(id)
);

CREATE TABLE IF NOT EXISTS velocities (
  id INTEGER PRIMARY KEY,
  run_id INTEGER NOT NULL,
  ts TEXT DEFAULT CURRENT_TIMESTAMP,
  fps REAL NOT NULL,
  FOREIGN KEY(run_id) REFERENCES production_runs(id)
);

CREATE TABLE IF NOT EXISTS maintenance_tasks (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  interval_type TEXT NOT NULL, -- 'hours','cycles','days'
  interval_value REAL NOT NULL,
  last_completed_at TEXT
);

CREATE TABLE IF NOT EXISTS maintenance_log (
  id INTEGER PRIMARY KEY,
  task_id INTEGER,
  ts TEXT DEFAULT CURRENT_TIMESTAMP,
  technician TEXT,
  notes TEXT,
  FOREIGN KEY(task_id) REFERENCES maintenance_tasks(id)
);

CREATE TABLE IF NOT EXISTS error_log (
  id INTEGER PRIMARY KEY,
  ts TEXT DEFAULT CURRENT_TIMESTAMP,
  subsystem TEXT,
  severity TEXT,
  message TEXT,
  cycle_position REAL,
  requires_stop INTEGER DEFAULT 1
);
