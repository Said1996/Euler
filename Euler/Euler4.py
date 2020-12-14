biggest = 0
index = 0
for i in range (999,99,-1):
    for j in range (999, 99,-1):
        palin = str(i*j)
        num = i*j
        if palin[:] == palin[::-1]:    
            if num > biggest:
                biggest = num
print(biggest)
                
            
            
    

    
    
    

