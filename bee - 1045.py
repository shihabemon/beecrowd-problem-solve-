X,Y,Z = map(float,input().split())
 
A = 0.0
B = 0.0
C = 0.0

if X>=Y>=Z:
  A = X
  B = Y 
  C = Z
elif X>=Z>=Y:
  A = X
  B = Z
  C = Y
elif Y>=X>=Z:
  A = Y
  B = X
  C = Z
elif Y>=Z>=X:
  A = Y
  B = Z
  C = X
elif Z>=X>=Y:
  A = Z
  B = X
  C = Y
elif Z>=Y>=X:
  A = Z
  B = Y
  C = X


if A >= B+C:
  print("NAO FORMA TRIANGULO")
if A ** 2 == B ** 2 + C ** 2 :
  print("TRIANGULO RETANGULO")
if A ** 2 > B ** 2 + C ** 2 :
  print("TRIANGULO OBTUSANGULO")
if A ** 2 < B ** 2 + C ** 2:
  print("TRIANGULO ACUTANGULO")

if A == B == C:
  print("TRIANGULO EQUILATERO")
elif A == B :
  print("TRIANGULO ISOSCELES")
elif A == C :
  print("TRIANGULO ISOSCELES")
elif B == C :
  print("TRIANGULO ISOSCELES")