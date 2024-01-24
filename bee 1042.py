X,Y,Z = map(float,input().split())

if X<Y<Z:
    print(X)
    print(Y)
    print(Z)
elif X<Z<Y:
    print(X)
    print(Z)
    print(Y)
elif Y<X<Z:
    print(Y)
    print(X)
    print(Z)
elif Y<Z<X:
    print(Y)
    print(Z)
    print(X)
elif Z<X<Y:
    print(Z)
    print(X)
    print(Y)
elif Z<Y<X:
    print(Z)
    print(Y)
    print(X)

print()

print(X)
print(Y)
print(Z)