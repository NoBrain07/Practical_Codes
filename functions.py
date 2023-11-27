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


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def Prime(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1

    return primes[-1]


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    a = 0
    b = 1
    count = 0
    try:
        if n <= 0:
            print("no negative integers or 0 is allowed")
        elif n == 1:
            return a
        else:
            for i in range(1, n):
                temp = a + b
                a = b
                b = temp
            return a
    except:
        raise TypeError(": Only integers are allowed")


def binary_num_search(arr, start, stop, item):
    array = sorted(arr)
    if not stop >= start:
        return "not in array"
    middle = (start + stop) // 2
    if array[middle] == item:
        return f"{item} is at {middle}"
    elif array[middle] > item:
        return f"item at {binary_num_search(arr,start,middle-1,item)}"
    elif array[middle] < item:
        return f"item at {binary_num_search(arr,middle-1,stop,item)}"


x = [1, 23, 2425, 44, 235, 3254, 325, 435, 234, 523, 423, 452345, 23, 234]

print(binary_num_search(x, 0, len(x), 23))
