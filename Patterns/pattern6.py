def num_invert_right(n):
    s = "".join(str(i+1) for i in range(n))
    for i in range(n,0,-1):
        print(s[:i])

num_invert_right(9)