
num=int(input("Enter your inputs: "))
array=[]
real=[]
visited=[]

while(num!=-1):
    array.append(num)
    num=int(input())

print("Given array is,")
print("\t",array)

for i in range(0,len(array)):
    visited.append(False)

for i in array:
    if(visited[i]):
        continue
    else:
        real.append(i)
        visited[i]=True

print("The array without duplicates while maintaining the same order,")
print("\t",real)

