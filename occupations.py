import csv
datafile = open('Training_Dataset.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
data = []
for row in datareader:
	data.append(row) 
occs = []
sum1 = 0
count1 = 0
sum2 = 0
count2 = 0
for x in range(1,len(data)):
	if data[x][12].strip() not in occs:
		occs.append(data[x][12].strip())
	if int(data[x][3])!=0:
		sum1+=int(data[x][3])
		count1+=1
	if int(data[x][9])!=0:
		sum2+=int(data[x][9])
		count2+=1
print(int(sum1/count1))
print(int(sum2/count2))
countX0=0
countX1=0
countX2=0

cleaned_dataset = [["cm_key","family size","spending capacity","total_cards","Number of acc months","Club fees","High spend prob","Influncer score","Income","Platinum card","bussiness exp prob","customer payments","numclubs","num airlines","electronics","travel","household","car","retail","total","ext1","ext2","ext3","acc1","acc2","acc3","Class"]]
occs_list = []
print(10)
for x in range(0,18):
	occs_list.append("Occs"+str(x))
	print(occs_list[x])
	cleaned_dataset[0].append(occs_list[x])
for x in range(1,len(data)):
	temp = []
	temp.append(int(data[x][0]))
	temp.append(int(data[x][2]))
	if(int(data[x][3])==0):
		temp.append(int(sum1/count1))
	else:
		temp.append(int(data[x][3]))
	temp.append(int(data[x][4]))
	temp.append(int(data[x][5]))
	temp.append(int(data[x][6]))
	temp.append(float(data[x][7]))
	temp.append(float(data[x][8]))
	if(int(data[x][9])==0):
		temp.append(int(sum2/count2))
	else:
		temp.append(int(data[x][9]))
	temp.append(int(data[x][10]))
	temp.append(float(data[x][11]))
	temp.append(int(data[x][13]))
	temp.append(int(data[x][14]))
	temp.append(int(data[x][15]))
	temp.append(float(data[x][16])+float(data[x][17])+float(data[x][18])+float(data[x][19]))
	temp.append(float(data[x][20])+float(data[x][21])+float(data[x][22])+float(data[x][23]))
	temp.append(float(data[x][24])+float(data[x][25])+float(data[x][26])+float(data[x][27]))
	temp.append(float(data[x][28])+float(data[x][29])+float(data[x][30])+float(data[x][31]))
	temp.append(float(data[x][32])+float(data[x][33])+float(data[x][34])+float(data[x][35]))
	temp.append(float(data[x][36])+float(data[x][37])+float(data[x][38])+float(data[x][39]))
	temp.append(int(data[x][40]))
	temp.append(int(data[x][41]))
	temp.append(int(data[x][42]))
	temp.append(int(data[x][43]))
	temp.append(int(data[x][44]))
	temp.append(int(data[x][45]))
	if int(data[x][46])==0 and int(data[x][47])==0 and int(data[x][48])==0:
		y1=0
	elif(int(data[x][46])==1):
		y1=1
	elif(int(data[x][47])==1):
		y1=2
	else:
		y1=3
	if int(data[x][49])==0 and int(data[x][50])==0 and int(data[x][51])==0:
		y2=0
	elif(int(data[x][49])==1):
		y2=1
	elif(int(data[x][50])==1):
		y2=2
	else:
		y2=3
	if y2==0:
		temp.append(0)
		countX0+=1
	elif y1==y2:
		temp.append(1)
		countX1+=1
	else:
		temp.append(2)
		countX2+=1	
	z = occs.index(data[x][12].strip())
	if x==1:	print(z)
	for y in range(0,18):
		if y==z:
			temp.append(1)
		else:
			temp.append(0)
	cleaned_dataset.append(temp)
print(countX0)
print(countX1)
print(countX2)

with open("clean_data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(cleaned_dataset)