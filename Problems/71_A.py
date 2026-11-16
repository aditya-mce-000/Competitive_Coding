n = int(input())
words = []

for i in range(n):
    words.append(input())

outputs = []
for word in words:
    n = len(word)
    if n > 10:
        outputs.append(f"{word[0]}{n-2}{word[-1]}")
    else:
        outputs.append(word)

for output in outputs:
    print(output)