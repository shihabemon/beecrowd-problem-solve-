x = float(input())

if 0 <= x <= 400.00:
    y = x * 15/100
    z = y + x 
    print("Novo salario: {:.2f}".format(z))
    print("Reajuste ganho: {:.2f}".format(y))
    print("Em percentual: 15%")
    
elif 400.01 <= x <= 800.00:
    y = x * 12/100
    z = y + x
    print("Novo salario: {:.2f}".format(z))
    print("Reajuste ganho: {:.2f}".format(y))
    print("Em percentual: 12%") 
    
elif 800.01 <= x <= 1200.00:
    y = x * 10/100
    z = x + y
    print("Novo salario: {:.2f}".format(z))
    print("Reajuste ganho: {:.2f}".format(y))
    print("Em percentual: 10 %")
    
elif 1200.01 <= x <= 2000.00:
    y = x * 7/100
    z = y + x
    print("Novo salario: {:.2f}".format(z))
    print("Reajuste ganho: {:.2f}".format(y))
    print("Em percentual: 7%")
    
elif x > 2000.00:
    y = x * 4/100
    z = y + x 
    print("Novo salario: {:.2f}".format(z))
    print("Reajuste ganho: {:.2f}".format(y))
    print("Em percentual: 4%")
