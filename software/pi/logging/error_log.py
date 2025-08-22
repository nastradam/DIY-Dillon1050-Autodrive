# Error logger (placeholder)
class ErrorLogger:
    def error(self, msg, subsystem="core", requires_stop=True):
        print(f"ERROR[{subsystem}]: {msg} stop={requires_stop}")
