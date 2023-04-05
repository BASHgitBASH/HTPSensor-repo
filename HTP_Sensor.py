import bme280
import smbus2
from time import sleep
import csv
from pathlib import Path
from datetime import datetime

port = 1
address = 0x77
bus = smbus2.SMBus(port)
bme280_data = bme280.sample(bus,address) 

file_name = "Data.csv"
i = 1

while Path(file_name).exists():
    file_name = f"Data{i}.csv"
    i += 1

headers = ['Time Stamp', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (C)']

with open (file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    while True:
        bme280_data = bme280.sample(bus,address)
        timestamp = f"{datetime.now():%d/%m/%y %H:%M}"
        humidity = str(round(bme280_data.humidity, 2))
        pressure = str(round(bme280_data.pressure, 2))
        temperature = str(round(bme280_data.temperature, 2))
        writer.writerow([timestamp, humidity, temperature, pressure])
        print("Timestamp =", timestamp,"Humidity(%) =", humidity, " Pressure(hPa) =", pressure, " Temperature(C) =", temperature)   
        sleep(1)


# ATTENTION THONNY STOP BUTTON CRASHES DATA CALL PRESS CTRL+C TO END
