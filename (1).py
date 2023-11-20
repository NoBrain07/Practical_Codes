# (1) WAP to calculate HCF (GCD) and LCM of two numbers

print("This program calculates the GCD and LCM ")

first_number = int(input("Enter The First Number =>"))
second_number = int(input("Enter The Second Number =>"))
hcf = 1
lcm = 0

if first_number > second_number:
    for i in range(2, first_number//2):
        if second_number % i == 0 and first_number % i == 0:
            hcf = i
        else:
            continue
elif second_number > first_number:
    for i in range(2, second_number//2):
        if second_number % i == 0 and first_number % i == 0:
            hcf = i
        else:
            continue
else:
    for i in range(2, first_number//2):
        if second_number % i == 0 and first_number % i == 0:
            hcf = i
        else:
            continue

lcm = (first_number * second_number) / hcf

print(f"The HCF is {hcf} and the LCM is {lcm}")
