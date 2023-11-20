# (5) WAP to check given number is duck or not

print(
    "Give a number [ONLY NUMBERS] and the program will tell you if this is a duck number or not ",
    "Enter 'end' to close program",
    sep="\n",
)

while True:
    inp_num = input("Enter a number => ")

    if inp_num.lower() == "end":
        print("Closing Program")
        break
    elif inp_num.isdigit() == False:
        print("Invalid Input")
    elif "0" in inp_num and inp_num[0] != "0":
        print(inp_num, "is a Duck number")
    else:
        print(inp_num, "is not Duck number")
