x = int(input())

if 1 < x < 1000:
    for i in range(1, 11):
        integer = i * x 
        print("{0} x {1} = {2}".format(i,x, integer))
