import csv

fields = ['name','age','city']

rows = [
    ['abhijeet','22','Kanpur'],
    ['sachin','24','mumbai'],
    ['sourav','25','kolkata'] 

    ]

filename = 'people.csv'

with open(filename , 'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
