array=[]

num=int(input("Enter the contiguous numbers:\n"))

while(num!=-1):
    array.append(num)
    num=int(input())

print("The given array with a missing number,")
print("\t",array)

minn=array[0]

for i in range(0,len(array)):
    if(minn>array[i]):
        minn=array[i]

maxx=array[0]

for i in range(0,len(array)):
    if(maxx<array[i]):
        maxx=array[i]
        
og=False

for i in range(minn,maxx+1):
    og=False
    for j in range(0,len(array)):
        if(i==array[j]):
            og=True
            break
    if(og==False):
        print("The missing number is:",i)
        break
    
