# from collections import Counter
def counter(lst,x):
    count = 0
    for i in range(len(lst)):
        if lst[i] == x:
            count += 1

    return count

n = int(input())

lines = []

for i in range(n):
    inp = input()
    lines.append(inp.split())

output = 0

for line in lines:
    if counter(line, "1") >= 2:
        output += 1
    
    

print(output)

