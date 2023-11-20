# Write a program to remove duplicates from a tuple.


def list_gen_end():
    sequence = list()
    print("Type 'end' if you want to end the list")
    while True:
        element = input("Enter Element -> ")
        if not element == "end":
            sequence.append((element))
        else:
            break
    return sequence


tup = tuple(list_gen_end())
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
