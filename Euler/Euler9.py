a= 1 
b = 499
c = 500



while c != (a**2 + b**2)**(1/2):
    
    a += 1
    b -= 1
    
    if a + 2 >=  b:
        c -= a

print(a,b,c)
