#######################################################
#                                                     #
#         Visualizing CSV file into .png image        #
#                                                     #
#######################################################

import csv
import matplotlib.pyplot as plt

time_row = []
result_row = []
# Open and read the CSV file
with open('result.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        time_row.append(float(row[0]))
        result_row.append(float(row[1]))
plt.plot(time_row, result_row)
plt.xlabel('Time (in ms)')
plt.ylabel('Voltage Value')
plt.title('ADC Test')
plt.grid(True)
plt.savefig('results.png')