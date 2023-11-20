# (7) WAP to accept a number from the user and find highest digit of anumber

print("This program will return you the highest digit of a given number")

while True:
    inp_num = input("Enter a number =>")

    if inp_num.lower() == "end":
        print("Closing program")
        break
    elif inp_num.isdigit() == True:
        numbers = list(inp_num)
        largest_number = int(numbers[0])
        for i in numbers:
            if int(i) > largest_number:
                largest_number = int(i)
            else:
                continue
        print("The largest digit in ", inp_num, "is ", str(largest_number))
    else:
        print("invalid input")
        continue
