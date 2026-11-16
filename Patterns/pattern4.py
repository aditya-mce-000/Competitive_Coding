def same_num_right(n):
    num = '1' * n
    for i in range(n):
        print(int(num[:i+1])*(i+1)) #ineer loop is better

same_num_right(9)