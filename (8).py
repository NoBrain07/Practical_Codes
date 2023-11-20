# (8) WAP to display prime number between 1 and 1000

print("This Program gives you the prime numbers between 1 and 1000")

prime_numbers = []
flag = True

for i in range(2, 1000):
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

print("Prime numbers between 1 and 1000 are => \n", prime_numbers)
print(len(prime_numbers))
