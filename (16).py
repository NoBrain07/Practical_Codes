# (16) Write a program to read email IDs of n number of students and store them in a tuple.
# Create two new tuples, one to store only the usernamesfromthe email IDs
# second to store domain names fromtheemail IDs.
# Print all three tuples at the end of the program.

print(
    "Enter email ids of students and type 'done' when all email ids have been entered"
)

emails = []
while True:
    email_id = input("Enter email =>")
    if "@" in email_id and "." in email_id:
        emails.append(email_id)
    elif email_id == "done":
        break
    else:
        print("Not an email")

fixed_emails = tuple(emails)

usernames, domains = [], []

for i in emails:
    temp = i.split("@")
    username = temp[0]
    domain = temp[1]
    usernames.append(username)
    domains.append(domain)

emails = tuple(emails)
usernames = tuple(usernames)
domains = tuple(domains)

print(
    "\nThe emails are => ",
    emails,
    "\nThe usernames are => ",
    usernames,
    "\nThe domain names are => ",
    domains,
)
