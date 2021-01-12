import json 
import csv


with open ("edible_higherLeaf.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = { "edibles" : []}
    for row in reader:
        data["edibles"].append(
            {'ID' : row[0] , 
             'Brand' : row[1],
             'Title' : row[2], 
             'Type'  : row[3],
             'Price' : row[4],
             'Amount' : row[5],
             'ImageLink': row[6]
             }
            )
    with open('edibles.json', 'w') as f:
        json.dump(data, f, indent=4)