n = int(input())
if 5 < n < 2000:
   for i in range(2, n+1, 2):
    square = i ** 2 
    print("{i}^2 = ".format(square))


