a , b , c  = map(int,input().split())

if a >= b and a >= c :
 x = a 
elif b >= a and b >= c :
 x = b 
else:
 x =c 
    
print("{:} eh o maior".format(x))
