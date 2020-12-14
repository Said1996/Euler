squareOfSum = (50*101)**2
sumOfSquare = 0



for i in range(101):
    sumOfSquare += i**2


diff = squareOfSum - sumOfSquare

print(diff)
