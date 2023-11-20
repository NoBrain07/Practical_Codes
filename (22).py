# (23) Write a program as per following specification :
# Return the length of the shortest string in the tuple of a strings str_tuple.
# Precondition : the tuple will contain at least one element .

print(
    "This program returns the length of the largest string in a tuple of strings",
    "Enter a tuple with atleast one string as element",
    sep="\n",
)

while True:
    choice = input("Do you want to continue ?\n'yes' or 'no' => ")
    if choice == "yes":
        str_tuple = eval(input("Enter your tuple => "))
        len_str = 0

        if len(str_tuple) >= 1:
            for i in str_tuple:
                if len(i) > len_str:
                    len_str = len(i)
                else:
                    continue

            print("The length of longest string here is", len_str)
        else:
            print("Empty tuples shouls not be entered")
    elif choice == "no":
        print("Closing Program")
        break
    else:
        print("Invalid Input")
