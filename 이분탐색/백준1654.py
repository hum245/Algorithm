from pandas import array


def binary_search(target, start, end, arr):
    if start > end:
        return None
    
    mid = (start+end)//2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid - 1
    else:
        start = mid+1
        
    return binary_search(target, start, end, array)

arr = [i * 3 for i in range(11)]
target = 6
idx = binary_search(target, 0, 10, arr)

print(arr)
print(idx)