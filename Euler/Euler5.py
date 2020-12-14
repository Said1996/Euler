flag = True
a = 0
counter = 0

while flag == True:
    a+=210
    counter = 0
    for x in range(1,21):
        if a%x == 0:
            counter +=1
        else:
            break
    if counter == 20:
        print(a)
        flag = False
        
            
