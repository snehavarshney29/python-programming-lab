num = int(input("Enter a number \n"))
sqr = num**2
sumofDigit = 0
while sqr>0:
    sumofDigit =sumofDigit + sqr%10
    sqr = sqr//10
if (num == sumofDigit):
    print("Neon Number \n")
else:
    print("Not a Neon Number \n")
