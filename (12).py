# (12) WAP to print the given 1, 9, 25, 49, ………………n series.

print("This program gives you the terms from the series 1, 9, 25, 49, ……………… n ")

term_no = int(input("How many terms do you want ? \n=> "))
n = 1
for i in range(term_no - 1):
    print(n**2, end=", ")
    n += 2
print(n**2)
