even = 0
odd = 0
positive = 0
negative = 0

for _ in range(5): 
    x = int(input())
    if x %2 == 0 :
        even += 1
    if x % 2 != 0 :
        odd += 1
    if 0 < x :
        positive += 1
    if x < 0 :
        negative += 1

print("{:} valor(es) par(es)".format(even))
print("{:} valor(es) impar(es)".format(odd))
print("{:} valor(es) positivo(s)".format(positive))
print("{:} valor(es) negativo(s)".format(negative))

