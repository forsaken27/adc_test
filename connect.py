import serial
import argparse
import csv

###################              Initializing              ##################################

parser = argparse.ArgumentParser()
parser.add_argument('--serialPort', default='COM7', type=str, help='Please type the serial port path')
parser.add_argument('--timeDuration', default='1000', type=int, help='Please input time duration in milliseconds')
args = parser.parse_args()
ser = serial.Serial(args.serialPort, 9600)
sampling_frequency = 10
csv_data = []
duration = args.timeDuration

###################              Reading from Serial              ###########################

current_time = 0
while current_time < duration:
    if ser.in_waiting:
        raw_data = ser.readline()
        current_voltage = raw_data.decode("utf-8").strip()
        csv_data.append((current_voltage))
        current_time += sampling_frequency
ser.close()    

###################              Converting into float              #########################

current_time = 0
for i in range(len(csv_data)):
    try:
        csv_data[i] = [current_time, float(csv_data[i])]
    except ValueError:
        csv_data[i] = [current_time, 0.0]
    current_time += sampling_frequency

###################              Creating CSV file              #############################

with open("result.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
print()
print("..... Process finished .....")
print()





