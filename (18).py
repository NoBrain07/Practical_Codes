# (18) Write a program to display the lowest and highest element of a given list/tuple of numbers

print(
    "This program gives you the highest and lowest number from then list or tupple which you enter",
    "Enter a proper tuple or list with numbers only else error will be shown",
    """Enter list/tuple or " 'end' " to end the program""",
    sep="\n",
)
while True:
    inp_seq = eval(input("=> "))
    flag = True
    if type(inp_seq) == tuple or type(inp_seq) == list:
        for i in inp_seq:
            if not type(i) == int:
                print("invalid list/tuple")
                flag = False
                break
            else:
                continue
        if flag == True:
            inp_seq = list(inp_seq)
            max_ele = max(inp_seq)
            min_ele = min(inp_seq)
            print(
                "The max element is => ", max_ele, "\nThe min element is => ", min_ele
            )
        else:
            print("Your sequence has alphabets or special characters")
    elif inp_seq is not tuple or inp_seq is not list:
        if inp_seq == "end":
            print("Closing Program")
            break
        else:
            print("invalid input")
    else:
        print("invalid input")
