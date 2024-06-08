def recursive(arr,low,high,x):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return recursive(arr,low,mid-1,x)
        else:
            return recursive(arr,mid+1,high,x)
    else:
        return -1

def iterative(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return -1

print("Enter the input size:")
n=int(input("enter size:"))
arr=[]
print("enter elelments:")
for i in range(0,n):
    r=int(input())
    arr.append(r)
print("enter key:")
k=int(input("enter key:"))    
p=recursive(arr,0,len(arr)-1,k)    
if p==-1:
    print("not found")
else:
    print("found at index ",p)

print("using iterative")
q=iterative(arr,k)
if q==-1:
    print("not found")
else:
    print("found at index ",q)
    
                
        