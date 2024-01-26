even = 0
P_number =0

for _ in range(5):
    x = int(input())
    if x % 2 ==0   :

        even += 1
    elif x >= 0:

        P_number += 1     

print("{:} valores pares".format(even))
print("{:} valores pares".format(P_number))