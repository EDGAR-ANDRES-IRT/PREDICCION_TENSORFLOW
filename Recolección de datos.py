import pandas
import serial
import csv
import time

arduino = serial.Serial('COM8', 9600)
time.sleep(2)

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Temperatura", "Humedad"])

    try:
        while True:
            line = arduino.readline().decode('utf-8').strip()
            if line:
                try:
                    temp, hum = map(float, line.split(","))
                    writer.writerow([temp, hum])
                    print(f"Temp: {temp}°C, Hum: {hum}%")
                except ValueError:
                    print("Formato inválido:", line)
    except KeyboardInterrupt:
        print("Finalizando lectura...")

#Viernes 4 de julio, 5:03 pm
#Sabado 5 de julio, 6:01 pm