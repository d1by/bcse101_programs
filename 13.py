import pandas as pd

df = pd.read_csv('C:/DesktopStuff/Python stuff/uni/pps2/diabetes.csv')
print("Number of lines: ", len(df))
nulltot = 0
cols = list(df.columns)
for x in cols:
    for y in df[x]:
        if(y==0):
            nulltot+=1
print("Number of null values: ", nulltot)

df.to_csv('diabetesdata.csv')