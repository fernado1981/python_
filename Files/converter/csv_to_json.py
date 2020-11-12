import csv
import json

csvfile = open('../asociacion.csv', 'r')
jsonfile = open('../file.json', 'w')

#fieldnames = ("Importe", "Actividad Subvencionada", "Asociacion")
reader = csv.DictReader(csvfile)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
