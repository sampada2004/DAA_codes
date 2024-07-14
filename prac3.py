def quicksort(arr):
    if(len(arr))<=1:
        return arr
    else:
        pivot=arr[len(arr)//2]
        left=[x for x in arr if x<pivot]
        middle=[x for x in arr if x==pivot]
        right=[x for x in arr if x>pivot]
    return quicksort(left)+middle+quicksort(right)
arr=[5,2,7,9,3]
res=quicksort(arr)
print(res)