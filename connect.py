import serial
import argparse
import csv
import time
###################              Initializing              ##########################################

parser = argparse.ArgumentParser()
parser.add_argument('--serialPort', default='COM8', type=str, help='Please type the serial port path')
parser.add_argument('--timeDuration', default='1', type=int, help='Please input time duration in seconds')
args = parser.parse_args()
ser = serial.Serial(args.serialPort, 1000000)
csv_row = []
#csv_row_2 = []
duration = args.timeDuration

###################              Reading from Serial              ###################################

start = time.time()
buffer = b''

while time.time() - start < duration:
    if ser.in_waiting:
        buffer += ser.read(ser.in_waiting)
        while b'\n' in buffer:
            line, buffer = buffer.split(b'\n', 1)
            try:
                parts = line.decode("utf-8").strip().split()
                csv_row.append(parts)
            except UnicodeDecodeError:
                continue
ser.close()    

###################              Preprocess the received data              #########################

csv_data = []
current_time = 0.0
sampling_frequency = duration/len(csv_row)
for i in range(len(csv_row)):
    if len(csv_row[i])==12:
        try:
            csv_data.append([current_time,  float(csv_row[i][0])*3.3/511.0, 
                                            float(csv_row[i][1])*3.3/511.0,
                                            float(csv_row[i][2])*3.3/511.0,
                                            float(csv_row[i][3])*3.3/511.0,
                                            float(csv_row[i][4])*3.3/511.0,
                                            float(csv_row[i][5])*3.3/511.0,
                                            float(csv_row[i][6])*3.3/511.0,
                                            float(csv_row[i][7])*3.3/511.0,
                                            float(csv_row[i][8])*3.3/511.0,
                                            float(csv_row[i][9])*3.3/511.0,
                                            float(csv_row[i][10])*3.3/511.0,
                                            float(csv_row[i][11])*3.3/511.0])   
        except ValueError:
            csv_data.append([current_time, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    else:
        csv_data.append([current_time, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    current_time += sampling_frequency

###################              Creating CSV file              ####################################

with open("result.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
print()
print("..... Process finished .....")
print()
print(f"The frequency of acquiring the data is : {len(csv_data)/duration} Hz")
print()





