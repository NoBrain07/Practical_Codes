# (13) WAP to print the given 24,99,224, 399,…… n series

print("This program gives you the terms from the series 24,99,224, 399,…… n ")

term_no = int(input("How many terms do you want ? \n=> "))

n = 75
term = 24
for i in range(term_no - 1):
    print(term, end=", ")
    term += n
    n += 50
print(term)
