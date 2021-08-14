from pyunpack import Archive
Archive('.\\output\\output.zip').extractall(".\\output")

import os
import glob
import pandas as pd
os.chdir(".\\output")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

df1 = pd.read_csv('combined_csv.csv') 
df2=df1[['Roll No','CGPA']]
print(df2)
df2.to_csv("result.csv")