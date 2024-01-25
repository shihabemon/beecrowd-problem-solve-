P_number =  0
sum_number = 0

for _ in range(6):
    x = float(input())
    if x > 0 :
        P_number += 1
        sum_number += x

average_all_positive = sum_number / P_number 

print("{:} valores positivos".format(P_number))
print("{:.1f}".format(average_all_positive))
