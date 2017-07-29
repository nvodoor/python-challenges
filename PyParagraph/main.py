import os

root_path = os.path.join(os.getcwd(), "..")
py_path = os.path.join(root_path, "PyParagraph")

filepaths = []
for file in os.listdir(py_path):
	if file.endswith(".txt"):
		filepaths.append(os.path.join(py_path, file))

sentlist = []

for file in filepaths:

	count = 0
	linecount = 0

	with open(file,'r') as fh:

		for line in fh:
			for x in line:
				linecount += 1
				char = line[linecount-2].upper()
				if x == "." and line[linecount-2] != char:
					count += 1
				if count > 1:
					sentences = line.split(".")
					for y in sentences:
						sentlist.append(y)
						# sentencelength += 1
					count = 0
					linecount = 0
					break
			if count == 1:
				sentlist.append(line)
				# sentencelength += 1
			count = 0
			linecount = 0

letters = 0
propwords = []
for sent in sentlist:
	if sent == "":
		sentlist.remove(sent)
	onesent = sent.split(" ")
	# print (onesent)
	for word in onesent:
		alphlet = 0
		notlet = 0
		for let in word:
			if let.isalpha() == True:
				letters += 1
				alphlet += 1
			else:
				notlet += 1
		if alphlet > notlet and "-" in word:
			newword = word.split("-")
			for subword in newword:
				propwords.append(subword)
			alphlet = 0
			notlet = 0
		elif alphlet > notlet:
			propwords.append(word)
			alphlet = 0
			notlet = 0
		else:
			alphlet = 0
			notlet = 0

sentencenumber = len(sentlist)
wordcount = len(propwords)
sentencelength = wordcount/sentencenumber
avgletcount = letters/wordcount

print("Paragraph Analysis")
print("------------------")
print(f"Approximate Sentence Count: {sentencenumber}")
print(f"Approximate Word Count: {wordcount}")
print(f"Average Sentence Length: {sentencelength}")
print(f"Average Letter Count: {avgletcount}")
# print(sentlist)
# print(propwords)