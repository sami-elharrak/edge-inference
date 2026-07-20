# Edge Inference on Raspberry Pi 4

Real-time sensor fault detection using a trained Random Forest model deployed on a Raspberry Pi 4 with a live DHT22 temperature/humidity sensor.

This is Part 2 of a two-part portfolio project. Part 1 (training the model) is available at [sensor-classifier](https://github.com/sami-elharrak/sensor-classifier).

## What This Project Does

- Reads live temperature and humidity data from a DHT22 sensor wired to the Pi's GPIO pins
- Feeds each reading into a pre-trained Random Forest classifier
- Outputs a real-time NORMAL/FAULT prediction with confidence score every 3 seconds
- Logs all predictions to a CSV file with timestamps

## Hardware

| Component | Details |
|-----------|---------|
| Raspberry Pi 4 Model B | 2GB RAM |
| DHT22 Sensor (AM2302) | Temperature + humidity |
| Breadboard + jumper wires | GPIO wiring |
| 10kΩ pull-up resistor | Data line stability |

## Wiring

| DHT22 Pin | Pi GPIO Pin |
|-----------|-------------|
| VCC (Pin 1) | Pin 1 (3.3V) |
| DATA (Pin 2) | Pin 7 (GPIO4) |
| GND (Pin 4) | Pin 6 (GND) |

Resistor bridges VCC and DATA pins on the breadboard.

## Software

- Python 3.13
- scikit-learn
- joblib
- adafruit-circuitpython-dht
- Raspberry Pi OS Lite (64-bit)

## How to Run

```bash
# Clone the repo
git clone https://github.com/sami-elharrak/edge-inference.git
cd edge-inference

# Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install scikit-learn joblib adafruit-circuitpython-dht

# Run inference
python scripts/inference.py
```

## Sample Output
[2026-07-20 22:45:06] Temp: 26.3C | Humidity: 42.9% | NORMAL (72.0% confidence)
[2026-07-20 22:45:09] Temp: 25.1C | Humidity: 45.1% | NORMAL (72.0% confidence)
[2026-07-20 22:45:12] Temp: 25.1C | Humidity: 45.4% | NORMAL (72.0% confidence)

191 readings logged over ~10 minutes. Full log available in `outputs/inference_log.csv`.

## Project Structure
edge-inference/
├── scripts/
│ └── inference.py # Live inference loop
├── models/
│ └── random_forest_model.pkl # Pre-trained Random Forest
├── outputs/
│ └── inference_log.csv # Logged predictions
└── README.md

## Key Concepts

- **Edge inference** — running ML predictions directly on hardware rather than sending data to the cloud. Lower latency, no internet dependency.
- **GPIO interfacing** — reading real sensor data via the Pi's GPIO pins using the Adafruit DHT library.
- **Model deployment** — taking a model trained in a Python environment and deploying it to a constrained embedded system.

## Part 1

The Random Forest model was trained in Part 1 of this project on synthetic sensor data (temperature, vibration, pressure). See [sensor-classifier](https://github.com/sami-elharrak/sensor-classifier) for the full training pipeline.
