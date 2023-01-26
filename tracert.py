import subprocess
import csv
ipORurl = input("Eneter IP or URL: ")  # taking IP or URL as input
with open("output.csv", "w") as file:  # opening the output.csv file to write the output
    process = subprocess.Popen(["tracert", ipORurl], stdout=subprocess.PIPE)  # performing 'tracert' on the input
    for line in process.stdout:
        line_list = line.decode('utf-8').split()  # spliting the line to write in different cells
        file.write(','.join(line_list) + '\n')
