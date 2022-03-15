import csv
data=[]
with open("bright_stars.csv","r") as F:
    csvreader = csv.reader(F) 
    for row in csvreader:
        data.append(row)
headers1=data[0]
planet_data1=data[1:]
data2=[]
with open("unit_converted_stars.csv","r") as F:
    csvreader = csv.reader(F) 
    for row in csvreader:
        data2.append(row)
headers2=data2[0]
planet_data2=data2[1:]
headers=headers1+headers2
planet_data=[]
for i,row in enumerate(planet_data1):
    planet_data.append(planet_data1[i]+planet_data2[i])
with open ("final_stars.csv","a+") as F:
    csvwriter = csv.writer(F) 
    csvwriter.writerow (headers)
    csvwriter.writerows(planet_data)