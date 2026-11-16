def num_right(n):
    # num = ""
    # for i in range(n):
    #     num += str(i+1)
    num = "".join(str(i+1) for i in range(n))
    for i in range(n):
        print(num[:i+1])

num_right(7)
