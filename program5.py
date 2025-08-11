
import math

num=int(input("Enter any number: "))

og=True

print(math.floor(math.sqrt(num)))

for i in range(2,math.floor(math.sqrt(num))+1):
    if((num%i)==0):
        og=False
        break

if(og):
    print("The given number",num,"is a prime number")
else:
    print("The given number",num,"is not a prime number")
