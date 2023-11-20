# Show this pattern
# AAAAA
# BBBB
# CCC
# DD
# E

a = 0

for i in range(5, 0, -1):
    print(chr(65 + a) * i)
    a += 1
