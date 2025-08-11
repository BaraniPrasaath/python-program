name=str(input("Enter a String: "))

length=len(name)

for i in range(length-1,-1,-1):
    print(name[i],end="")

