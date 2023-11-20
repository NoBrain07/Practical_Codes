# (14) WAP as per specifications given below:
# ->Repeatedly prompt for a sentence (string) or for ‘q’ to quit.
# ->Upon input of a sentence or string (s), print the string produced from ‘s’ by converting each lower case letter toupper case and vice-versa.
# ->All other characters are left unchanged

while True:
    s = input("Enter a sentence or type 'q' to quit\n=>")
    new_s = ""
    if s == "q":
        print("Closing Program")
        break
    else:
        for i in s:
            if i.islower():
                new_s += i.upper()
            elif i.isupper():
                new_s += i.lower()
            else:
                new_s += i
        print("Your new string is \n=>", new_s)
