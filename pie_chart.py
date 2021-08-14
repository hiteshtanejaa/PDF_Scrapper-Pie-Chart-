import csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.axes.Axes.pie
matplotlib.pyplot.pie
with open('.\\output\\mycsv.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    below7 = 0
    above7 =0
    above9orequalto10 = 0
    below4 = 0
    for row in reader:
        if row['CGPA'] < '7' and row['CGPA'] > '4' :
            below7 = below7 + 1
        elif row['CGPA'] >= '7' and row['CGPA'] < '9':
            above7 = above7 + 1
        elif row['CGPA'] >= '9' :
            above9orequalto10 = above9orequalto10 + 1
        elif row['CGPA'] <= '4' and row['CGPA'] > '0' :
            below4 = below4 + 1
     
print (f' CGPA below 4 {below4} , CGPA below 7 {below7} , CGPA above 7 {above7} , CGPA above 9 or equal to 10 {above9orequalto10} ')



labels = 'Below 4', 'Below 7 and Above 4', 'Above 7 and Below 9', 'Above 9 or Equal to 10 '
sizes = [below4, below7, above7, above9orequalto10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()