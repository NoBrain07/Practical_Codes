# (19) Write a program to accept a list and an element.
# The program should count and display the frequency of entered element in the list.

# Getting the list

print(
    "Enter the elements of your list",
    "Type 'end' if you want to end the list",
    sep="\n",
)

sequence = list()
while True:
    element = input("=> ")
    if not element.lower() == "end":
        sequence.append(element)
    else:
        break

print("Your list is => ", sequence)

while True:
    print("Type the element which you want to count 'end' to end the counting ")
    cnt_ele = input("=> ")
    count = 0
    if not cnt_ele == "end":
        print(cnt_ele, "is present", sequence.count(cnt_ele), "times in your list")
    else:
        print("Closing Program")
        break
