# (20) Write a program to shift element of a list
# first element moves to the second index
# second index moves to the third index, etc.
# last element shifts to first position .

print("Enter a list and this program will shift each element one index further")
the_list = eval(input("=>"))
the_list.insert(0, the_list[len(the_list) - 1])
the_list.pop()
print("The new list is => ", the_list)
