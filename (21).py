# (21) Create a dictionary with roll number, name and marks of n students in a class
# display the names of students who have scored marks above 75

print("Enter 'done' when you have entered all the student details")
students = {"Roll No.": ["Name", "Marks"]}

while True:
    roll_no = input("Enter Roll Number of Student => ")
    if (
        roll_no.lower() != "end"
        and roll_no.isdigit() == True
        and roll_no not in students.keys()
    ):
        details = [input("Enter Name => "), int(input("Enter Marks => "))]
        students.update({roll_no: details})
    elif roll_no.lower() == "end":
        print("Student Info is recorded")
        break
    else:
        print("Don't repeat Roll numbers or use letters as Roll number")

keys = students.keys()

for i in keys:
    try:
        if students[i][1] > 75:
            print(students[i][0], ",", sep="", end=" ")
        else:
            continue
    except:
        continue

print("have scored more than 75 ")
