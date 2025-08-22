# Production logger (placeholder)
class ProductionLogger:
    def start_run(self, batch_code: str):
        print(f"RUN START: {batch_code}")
    def stop_run(self):
        print("RUN STOP")
    def record_round(self):
        print("ROUND++")
