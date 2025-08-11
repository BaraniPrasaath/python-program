arr=[3,34,4,12,5,2]

value=int(input("Enter a number: "))

for i in range(6):
    for j in range(i,6):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

og=False

for i in range(6):
    if(arr[i]==value):
        og=True
        break
    for j in range(i,6):
        temp=arr[i]+arr[j]
        if(temp==value):
            og=True
            break
        elif(temp>value):
            og=False
    if(og):
        break

if(og):
    print(og)
else:
    print(og)

