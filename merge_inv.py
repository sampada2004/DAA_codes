#nlogn
def mergesort(arr,n):
    temp_arr=[0]*n
    return _mergesort(arr,temp_arr,0,n-1)
def _mergesort(arr,temp_arr,left,right):
    inv_count=0
    if left<right:
        mid=(left+right)//2
        inv_count+=_mergesort(arr,temp_arr,left,mid)
        inv_count+=_mergesort(arr,temp_arr,mid+1,right)
        inv_count+=merge(arr,temp_arr,left,mid,right)
    return inv_count
def merge(arr,temp_arr,left,mid,right):
    i=left
    k=left
    j=mid+1
    inv_count=0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp_arr[k]=arr[i]
            k+=1
            i+=1
        else:
            temp_arr[k]=arr[j]
            inv_count+=(mid-i+1)
            k+=1
            j+=1
    while i<=mid:
        temp_arr[k]=arr[i]
        k+=1
        i+=1
    while j<=right:
        temp_arr[k]=arr[j]
        k+=1
        j+=1
    for loo_val in range(left,right+1):
        arr[loo_val]=temp_arr[loo_val]
    return inv_count
arr1=[8,7,6,5,4,3,2,1]
arr2=[8,7,6,5,4,3,2,1]
arr3=[3,4,5,6,7,8,1,2]
a1=len(arr1)
a2=len(arr2)
a3=len(arr3)
res1=mergesort(arr1,a1)
res2=mergesort(arr2,a2)
res3=mergesort(arr3,a3)
min_res=min(res1,res2,res3)
if min_res==res1:
    print("1")
elif(min_res==res2):
    print("2")
else:
    print("3")