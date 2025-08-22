# Data & Production Logging

Records the *who/what/when* for ammunition batches and QC.

## Entities
- **Caliber Profiles**
- **Components**: projectile type/weight, powder, brass (lot), primer type
- **Batches & Lots**: unique IDs, notes, dates
- **Production Runs**: start/stop, press rate, total counts
- **QC**: case gauge pass/fail, OAL stats, measured velocities, match/range usage

See `db/schema.sql` for the full schema.
