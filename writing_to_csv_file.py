import csv

with open("newfile.csv","a",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["name","address","email"])
    my_array=[
        ["jim","california","whatever"],
        ["carr6y","los angeles","whatever2"]
    ]
    writer.writerows(my_array)