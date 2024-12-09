import numpy as np

FILE_PATH = '2024/day-02/data.txt'

def import_data(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            reports.append([int(x) for x in line.split()])
    return reports

reports = import_data(FILE_PATH)

safe = 0
for report in reports:
    j = report[0]
    safe_steps = 0
    for i in range(1,len(report)):
        if report[i] == report[i-1]:
            break
        if report[i] < j and not (report[i] - report[i-1] in range(-3,-1)):
            break
        if report[i] > j and not (report[i] - report[i-1] in range(1,3)):
            break
        safe_steps += 1
    if safe_steps == len(report) - 1:
        safe += 1

print(safe)
        




