# Powder check handling (placeholder)
def handle_powder_check(sensors, logger):
    if sensors.read_powder_check():
        logger.error("Powder check fault", subsystem="powder", requires_stop=True)
