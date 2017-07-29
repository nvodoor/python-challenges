import os
import csv
from datetime import datetime
import us_state_abbrev as us

#Plan:
#Name will involve creating a split array from the Name column.
#I will then take this split array and create new arrays titled first and last name
#put first name in first array
#last name in second array.
#0,1 on split array should suffice
#DOB will also involve a split array. Three items in array.
#loop through items and add to a new array. Each new append will be accompanied
#by an append of a /
#then join that array together
#append that joined array to a master DOB array

# Establish the root path and resource path
root_path = os.path.join(os.getcwd(), "..")
resource_path = os.path.join(root_path, "PyBoss")
# Iterate through the listdir results
filepaths = []
for file in os.listdir(resource_path):
    if file.endswith(".csv"):
        filepaths.append(os.path.join(resource_path, file))


for file in filepaths:
    # @TODO: Create empty lists to house new reconfigured data for the new csv sheet
    first = []
    last = []
    DOB = []
    SSN = []
    State = []
    Emp_ID = []

    with open(file) as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            fullname = row['Name'].split(" ")
            first.append(fullname[0])
            last.append(fullname[1])
            Birth = row['DOB'].split("-")
            newbirth = []
            newbirth.append(Birth[1])
            newbirth.append(Birth[2])
            newbirth.append(Birth[0])
            DOB.append("/".join(newbirth))
            ss = list(row['SSN'])
            for x in range(0,7):
                if ss[x] != "-":
                    ss[x] = "*"
            SSN.append("".join(ss))
            for state in us.us_state_abbrev:
                if row['State'] == state:
                    State.append(us.us_state_abbrev[state])
            Emp_ID.append(row['Emp ID'])
    # print(first)
    # print(last)
    # print(DOB)
    # print(SSN)
    # print(State)
    csvpath = os.path.join(os.getcwd(), "skcrub_emp_data.csv")
    with open(csvpath, "w") as csvfile:
        fieldnames = ["Emp ID", "first_name", "last_name", "DOB", "SSN", "State"]
        # @TODO: Use csv.DictWriter to write new_employee_data to a csv file
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        x = 0
        for row in Emp_ID:
            writer.writerow({'Emp ID': row,'first_name': first[x], 'last_name': last[x], 'DOB': DOB[x], 'SSN': SSN[x], 'State': State[x]})
            x += 1