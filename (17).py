# (17) Write a program to remove duplicates from a tuple.

tup = eval(input("Enter a tuple => "))
print("Your tuple is ", tup)
un_tup = list(tup)
clean_tup = []
for i in un_tup:
    if i not in clean_tup:
        clean_tup.append(i)
    else:
        continue
clean_tup = tuple(clean_tup)
print("Your tuple without repeated terms is", clean_tup)
