def partition(arr,low,high):
    p=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=p:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
data=[60,20,10,11,12]
size=len(data)
quicksort(data,0,size-1)
print(data)