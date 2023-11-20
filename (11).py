# (11) Write a program to accept numbers from the user until user saysyes-‘Y’
# It should calculate the mean of all entered numbers
# The program ends when the user says no- ‘N’ or programs aborts if number is less than zero.

print(
    "This program will return you the mean of the numbers you enter. Give input",
    "=> 'Y' to get the mean of all given numbers",
    "=>'N' to close program ",
    "*negative numbers are invalid inputs and this will abort the program",
    "Enter Numbers",
    sep="\n",
)

total = 0
track = 0
while True:
    inp_num = input("=> ").replace(" ", "")
    if inp_num.isdigit():
        if int(inp_num) < 0:
            print("Program Abort")
            break
        else:
            total += int(inp_num)
            track += 1
    elif inp_num.isalpha():
        if inp_num.lower() == "y":
            mean = total / track
            print("The mean of all entered numbers is ", mean)
            break
        elif inp_num.islower() == "n":
            print("Closing Program")
    else:
        print("Invalid Input", "\nInput not counted for the mean")
