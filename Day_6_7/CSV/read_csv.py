import csv
with open('people.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import csv
