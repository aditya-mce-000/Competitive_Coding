n = int(input())

lst = []

initial = 0

for i in range(n):
    inp = input()
    if "++" in inp:
        initial += 1
    else:
        initial -= 1

print(initial)