import sys

input = sys.stdin.readline

n = int(input())
output = []

for j in range(n):
    a = int(input())
    b = input()
    switch = 0
    if b[0] == 'B':
        switch += 1
    for i in range(a-1):
        if b[i] == b[i+1]:
            switch += 1

    output.append(switch)

for i in range(n):
    print(output[i])