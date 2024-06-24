#  Time Complexity: O(n log n) where n is the number of elements in the input array.
"""
    The given Python function implements the quicksort algorithm to sort an input array in O(n log n)
    time complexity.
    
    :param arr: The code you provided is an implementation of the quicksort algorithm in Python. It
    takes an input array `arr`, partitions it based on a pivot element, and recursively sorts the left
    and right partitions until the entire array is sorted
    :return: The `quicksort` function returns the sorted array after applying the quicksort algorithm on
    the input array `arr`.
    """

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

print("Enter arr size")
n=int(input())
arr=[]
print("enter elements:")
for i in range(n):
    ip=int(input())
    arr.append(ip)   
sorted_arr = quicksort(arr)
print("Sorted array is:", sorted_arr)