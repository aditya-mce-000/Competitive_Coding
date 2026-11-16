def invert_right(n):
    _ = '*'* n
    for i in range(n,0,-1):
        print(_[:i])

invert_right(4)