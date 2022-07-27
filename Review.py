TotalNumberOfStrings = int(input())

for i in range (0, TotalNumberOfStrings):
    s = input()

    print(s[::2], s[1::2])