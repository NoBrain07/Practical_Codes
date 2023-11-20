# (3) WAP to display Reverse of a given numbers.

number = int(input("Enter A number => "))
cop = number
rev = 0
for i in range(len(str(number))):
    rev *= 10
    rev += cop % 10
    cop = cop // 10
print("The original number is => ", number, "\nThe number reversed is => ", rev)
