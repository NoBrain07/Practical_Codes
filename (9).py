# (9) WAP to find out all the Armstrong numbers between 1 and 1000

print(
    "An armstrong number is a number whose sum of digits raised to power of length on the number is equal to the digit itself \n"
)

armstrong_numbers = []

for number in range(1, 1001):
    armstrong = 0
    power = len(str(number))
    for i in list(str(number)):
        i = int(i)
        armstrong += i**power

    if armstrong == number:
        armstrong_numbers.append(int(number))
    else:
        continue

print("The Armstrong numbers between 1 and 1000 are ", armstrong_numbers)
