import csv
data_covid = []
data_estados = []
data_migracion = []
with open('reporte_covid19.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        data_covid.append(row)
with open('estados_parsed.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        data_estados.append(row)
with open('migracion.csv') as File:
    reader = csv.reader(File, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        data_migracion.append(row)
data_final = []
for row in data_estados:
        for row2 in data_covid:
                for row3 in data_migracion:
                        if (row[0] == row2[0] and row[0] == row3[0]):
                                tasa_migracion = int(row3[7]) / int(row[1])
                                data_final.append([row[0],row[1],row2[5],row2[6],row2[7],tasa_migracion])
print("a",";","b",";","c",";","d",";","e",";","f")
for row in data_final:
        print(row[0],";",row[1],";",row[2],";",row[3],";",row[4],";",row[5])
