import os
import csv

#getting root path and resource path
root_path = os.path.join(os.getcwd(), "..")
py_path = os.path.join(root_path, "PyBank")



filepaths = []
for file in os.listdir(py_path):
	if file.endswith(".csv"):
		filepaths.append(os.path.join(py_path, file))

#iterate through results. Create data.
months = 0
revenue = 0
highdate = ""
highnum = 0
lowdate = ""
lownum = 0
for file in filepaths:

	with open(file) as csvfile:

		reader = csv.DictReader(csvfile)
		for row in reader:
			months += 1
			revenue += int(row['Revenue'])
			if lownum == 0:
				lownum = int(row['Revenue'])
				lowdate = row['Date']
			elif int(row['Revenue']) < lownum:
				lownum = int(row['Revenue'])
				lowdate = row['Date']

			if highnum == 0:
				highnum = int(row['Revenue'])
				highdate = row['Date']
			elif int(row['Revenue']) > highnum:
				highnum = int(row['Revenue'])
				highdate = row['Date']

avg = round(revenue/months,0)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {months}")
print(f"Total Revenue: ${revenue}")
print(f"Average Revenue Change: ${avg}")
print(f"Greatest Increase in Revenue: {highdate}, $({highnum})")
print(f"Greatest Decrease in Revenue: {lowdate}, $({lownum})")

#creating output directory
if not os.path.exists("output"):
	os.mkdir("output")

#writing a text file
output = os.path.join('output', 'bankdata.txt')
with open(output, 'w') as bank:
    bank.write('Financial Analysis\n')
    bank.write('---------------------\n')
    bank.write(f"Total Months: {months}\n")
    bank.write(f"Total Revenue: ${revenue}\n")
    bank.write(f"Average Revenue Change: ${avg}\n")
    bank.write(f"Greatest Increase in Revenue: {highdate}, $({highnum})\n")
    bank.write(f"Greatest Decrease in Revenue: {lowdate}, $({lownum})\n")