#!/usr/bin/env python3
"""Entry point for the Pi controller.

- Loads config
- Starts UI/API server
- Initializes IO and sensors
- Provides main run loop hooks
"""
from ui_server.app import create_app, run_dev
from logging.production_log import ProductionLogger

def main():
    # TODO: wire real lifecycle
    app = create_app()
    print("DIY Dillon 1050 Autodrive - UI/API ready")
    run_dev(app)

if __name__ == "__main__":
    main()
