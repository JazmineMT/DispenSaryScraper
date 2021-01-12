import json 
import csv


with open ("flower_higherLeaf.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = { "flower" : []}
    for row in reader:
        data["flower"].append(
            {'ID' : row[0] , 
             'Brand' : row[1],
             'Title' : row[2], 
             'Type'  : row[3],
             'Price' : row[4],
             'Amount' : row[5],
             'ImageLink': row[6]
             }
            )
    with open('flower.json', 'w') as f:
        json.dump(data, f, indent=4)