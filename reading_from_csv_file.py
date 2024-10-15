import csv

with open("newfile.csv",'r') as f:
    reader=csv.reader(f)
    for line in reader:
        print(line)