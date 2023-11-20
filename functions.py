# making number lists


def list_gen_end():
    sequence = list()
    print("Type 'end' if you want to end the list")
    while True:
        element = input("Enter element => ")
        if not element.lower() == "end":
            try:
                sequence.append(eval(element))
            except:
                sequence.append(element)
        else:
            break
    return sequence


def num_list_len(num):
    a = 0
    var = list()
    while a < num:
        element = input("=>")
        if element.isdigit():
            var.append(int(element))
            a += 1
        else:
            print("Invalid Input\nEnter ONLY numbers")
    return var


def num_list_end():
    numbers = list()
    print("Type 'end' if you want to end the list of numbers")
    while True:
        element = input("enter number")
        if element.isdigit() == True:
            numbers.append(eval(element))
        elif element.lower() == "end":
            break
        else:
            continue
    return numbers


# Prime number finder
def prime(begr, endr):
    prime_numbers = []
    flag = True

    for i in range(begr, endr + 1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = False
                break
            elif i % j > 0:
                flag = True
        if flag == True:
            prime_numbers.append(i)
        else:
            continue
    return prime_numbers
    return (
        f"The number of prime numbers between {begr} and {endr} is {len(prime_numbers)}"
    )


def is_arms(arg):
    inp_num = str(arg).replace(" ", "")

    if inp_num.isdigit():
        armstrong = 0
        num = int(inp_num)
        inp_num = str(num)
        power = len(str(inp_num))

        for i in list(inp_num):
            i = int(i)
            armstrong += i**power

        if armstrong == num:
            print(inp_num, " is an Armstrong number")

        else:
            print(inp_num, " is not an Armstrong number")

    else:
        return TypeError
