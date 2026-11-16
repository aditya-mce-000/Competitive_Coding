import sys

input = sys.stdin.readline

n = int(input())

output = []

for i in range(n):
    a = int(input())
    b = input()
    check = 0
    lst = []
    for j in range(a):
        if b[j] not in lst:
            lst.append(b[j])

    for k in range(len(lst)):
        str = b
        str2 = ""
        if str == reversed(str):
            break
        for l in len(str):
            print(True)

    output.append(check)