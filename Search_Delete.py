import csv

lines = list()

members= 'PRMS'

with open('.\\output\\result.csv', 'r') as readFile:

    reader = csv.reader(readFile)

    for row in reader:

        lines.append(row)

        for field in row:

            if field == members:

                lines.remove(row)
    print("Removed Rows containing Unwanted Values")
with open('.\\output\\mycsv.csv', 'w') as writeFile:

    writer = csv.writer(writeFile)

    writer.writerows(lines)

