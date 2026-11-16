import sys

input = sys.stdin.readline

n = int(input())

lst = []
for i in range(n):
    a = list(map(int, input().split()))
    a = sorted(a)
    lst.append(a)

# print(lst)

for num_lst in lst:
    a = 0
    for i in range(2):
        if num_lst[i] + 1 == num_lst[i+1]:
            continue
        else:
            a = 1
            break

    if a == 1:
        print('NO')
    else:
        print('YES')

