import joblib
import board
import adafruit_dht
import time
import csv
import os
from datetime import datetime

model = joblib.load('/home/sami/sensor-classifier/models/random_forest_model.pkl')

dht = adafruit_dht.DHT22(board.D4, use_pulseio=False)

log_path = '/home/sami/sensor-classifier/outputs/inference_log.csv'

if not os.path.exists(log_path):
    with open(log_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'temperature', 'humidity', 'prediction', 'confidence'])

print("Starting inference loop... press Ctrl+C to stop\n")

while True:
    try:
        temp = dht.temperature
        humidity = dht.humidity

        if temp is not None and humidity is not None:
            features = [[temp, 0.5, humidity]]
            prediction = model.predict(features)[0]
            confidence = max(model.predict_proba(features)[0]) * 100
            label = "FAULT" if prediction == 1 else "NORMAL"

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] Temp: {temp}C | Humidity: {humidity}% | {label} ({confidence:.1f}% confidence)")

            with open(log_path, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, temp, humidity, label, f"{confidence:.1f}"])

        time.sleep(3)

    except RuntimeError:
        time.sleep(2)
        continue
