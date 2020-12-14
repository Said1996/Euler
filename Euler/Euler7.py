n = 1
save_n = 0
listOfPrimes = [2 ,3]

while len(listOfPrimes) != 10001:
    if n != save_n:
        num = 6* n - 1
        save_n = n
    else:
        num = 6 * n + 1
        n += 1

    listOfPrimes_rooted = [i for i in listOfPrimes if i <= num ** (1 / 2)]

    point = 0
    for x in listOfPrimes_rooted:
        if num % x != 0:
            point += 1
            if point == len(listOfPrimes_rooted):
                listOfPrimes.append(num)
        else:
            break

print(listOfPrimes[-1])
                     











