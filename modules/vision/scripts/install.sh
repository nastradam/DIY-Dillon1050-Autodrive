#!/usr/bin/env bash
set -e
sudo apt-get update
sudo apt-get install -y python3-opencv python3-venv python3-pip libatlas-base-dev libgpiod2 gpiod
echo "System packages installed for Vision module."
