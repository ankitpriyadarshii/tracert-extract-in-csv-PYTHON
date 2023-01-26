import subprocess
import csv
ipORurl = input()
with open("output.csv", "w") as file:
    process = subprocess.Popen(["tracert", ipORurl], stdout=subprocess.PIPE)
    for line in process.stdout:
        line_list = line.decode('utf-8').split()
        file.write(','.join(line_list) + '\n')