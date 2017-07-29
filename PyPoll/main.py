import os
import csv

#getting root path and resource path
root_path = os.path.join(os.getcwd(), "..")
py_path = os.path.join(root_path, "PyPoll")



filepaths = []
for file in os.listdir(py_path):
	if file.endswith(".csv"):
		filepaths.append(os.path.join(py_path, file))

#iterate through results. Create data.

total = 0
votes = {}

for file in filepaths:

	with open(file) as csvfile:

		reader = csv.DictReader(csvfile)
		for row in reader:
			total += 1
			key = row['Candidate']
			if key in votes:
				votes[key] += 1
			else:
				votes[key] = 1

count = 0
winner = ""
print("Election Results")
print("---------------------")
print(f"Total Votes: {total}")
print("---------------------")
for k,v in votes.items():
	totes = round(round((int(v)/int(total)),2)*100,2)
	if totes > count:
		count = totes
		winner = k
	print(f"{k}: {totes}% ({v}) ")
print("---------------------")
print(f"Winner: {winner}")


#writing a text file
output = os.path.join(os.getcwd(), 'polldata.txt')
with open(output, 'w') as poll:
    poll.write('Election Results\n')
    poll.write('---------------------\n')
    poll.write(f"Total Votes: {total}\n")
    for k,v in votes.items():
    	totes = round(round((int(v)/int(total)),2)*100,2)
    	poll.write(f"{k}: {totes}% ({v})\n")
    poll.write("----------------------\n")
    poll.write(f"Winner: {winner}\n")
