# (10) WAP to find out all the palindrome number between 100 and 500

print(
    "A Palindrome is number which when it has it's digits reversed is same as the original number \nThis program tells you the palindromes between 100 to 500"
)

palindromes = []

for number in range(100, 501):
    cop = number
    rev = 0
    for i in range(len(str(number))):
        rev *= 10
        rev += cop % 10
        cop = cop // 10

    if rev == number:
        palindromes.append(number)
    else:
        pass

print("The Palindromes between 100 and 500 are => ", palindromes)
