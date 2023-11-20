# (6) WAP to check given number is Nelson or not

print(
    "A Nelson number is number which is a multiple of 111",
    "Enter a number and the program will tell whether your number is a nelson number ",
    sep="\n",
)

while True:
    nelson = input("Enter Number => ")

    if nelson.lower() == "end":
        print("Closing Program")
        break

    elif nelson.isdigit() == False:
        print("Invalid Input")

    elif int(nelson) % 111 == 0:
        print(nelson, "is a Nelson Number")

    else:
        print(nelson, "is not a Nelson Number")
