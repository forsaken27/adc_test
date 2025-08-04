#######################################################
#                                                     #
#         Visualizing CSV file into .png image        #
#                                                     #
#######################################################

import csv
import matplotlib.pyplot as plt


####################          Restoring the information from the csv file         ######################
time_row = []
results_row = [[] for _ in range(12)]
# Open and read the CSV file
with open('result.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        time_row.append(float(row[0]))
        for i in range(12):
            results_row[i].append(float(row[i+1]))


#####################                  Plotting the results            #################################
fig, axs = plt.subplots(3, 4, figsize=(15, 10))

for i in range(3):
    for j in range(4):
        axs[i][j].plot(time_row, results_row[4*i+j])
        axs[i][j].set_title(f"Pin {4*i+j}")
        axs[i][j].set_xlabel(f"Time")
        axs[i][j].set_ylabel(f"Voltage")
        axs[i][j].grid(True)
plt.tight_layout()
plt.savefig('results.png')