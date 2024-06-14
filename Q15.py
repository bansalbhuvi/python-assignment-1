import csv
f3=open("data.csv","r")
for i in csv.reader(f3):
    print(i)
f3.close()