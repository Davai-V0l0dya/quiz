import csv

with open('qusestions.csv', newline='', encoding='utf-8') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row[0], row[1], row[2])