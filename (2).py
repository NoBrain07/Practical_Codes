#(2) WAP to check max, min number in given ten numbers

print("This code gives largest on 10 numbers \nEnter 10 numbers ")
numbers = [int(input("=>")) for x in range(10)]
largest_number = numbers[0]
for i in numbers:
    if i > largest_number:
        largest_number = i
    else :
        continue
print(f"The largest number in the list => '{numbers}' is {largest_number}")
