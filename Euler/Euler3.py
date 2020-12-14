
num = 600851475143 
k = 1


while num > 1:
    num = num // k
    for i in range(num+1):
        counter = 0
        for j in range(1,i+1):
            if i%j == 0:
                counter += 1
        if counter == 2 :
            if num % i == 0:
                k = i
                print(k)
                break
    
print("Largest prime number in 600851475143 is : "+ str(k))              
    
            
    
    
    
    
    


