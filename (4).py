# (4) WAP to sum of all Even digit of a given numbers in a list
numbers = list()
print("Type 'end' if you want to end the list of numbers\nEnter Numbers")

while True:
    element = input("=>")
    if element.isdigit() == True:
        numbers.append(int(element))
    elif element.lower() == "end":
        break
    else:
        print("Enter numbers only")
        continue
print("Your list is => ", numbers)

sum_nums = 0

for i in numbers:
    if i % 2 == 0:
        sum_nums += i
    else:
        pass

print("The sum of all even digits is ", sum_nums)
