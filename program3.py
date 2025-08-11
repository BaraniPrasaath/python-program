
num=int(input("Enter your inputs: "))
array=[]
freq=[]
visited=[]

while(num!=-1):
    array.append(num)
    num=int(input())

print("Given array is,")
print("\t",array)

for i in range(0,len(array)):
    freq.append(0)
    visited.append(False)

for i in array:
    freq[i]+=1

print("\nIts frequency is,")

for i in array:
    if(visited[i]):
        continue
    else:
        if(freq[i]==1):
            print("\t",i,"-->",freq[i],"time")
        else:
            print("\t",i,"-->",freq[i],"times")
            visited[i]=True

maxx=freq[0]

for i in range(1,len(array)):
    if(maxx<=freq[i]):
        maxx=freq[i]
        ele=i

if(maxx==1):
    print("The maximum occuring element is ",ele,"-->",maxx,"time")
else:
    print("The maximum occuring element is ",ele,"-->",maxx,"times")
