'''
Select a pivot value (start of list)
Partition List (use two pointers)
    if less than pivot, move to leftside
    if greater than pivot, move to rightside
    once both pointers reach a value that fits criteria, swap and continue with partition
    partition stops when pointers cross
Once partition ends, move pivot point to the appropriate sorted position
'''
def quick_sort(arr):
    helper(arr, 0, len(arr) - 1)

def helper(arr, start, end):
    if start < end:
        split = partition(arr, start, end)
        helper(arr, start, split - 1)
        helper(arr, split + 1, end)

def partition(arr, start, end):
    pivot = start
    left = start + 1
    right = end

    while left < right:
        if arr[left] < arr[pivot]:
            left += 1
        if arr[right] >= arr[pivot]:
            right -= 1
        
        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            temp = arr[right]
            arr[right] = arr[left]
            arr[left] = temp
        
    temp = arr[left-1]
    arr[left-1] = arr[pivot]
    arr[pivot] = temp
    print(arr)
    return right

if __name__ == '__main__':
    numbers = [5, 6, 8, 1, 15, 9, 20, 12, 19, 10, 11, 18, 4, 13, 2, 3, 17, 16, 14, 7]
    print(numbers)
    print(quick_sort(numbers))
    print(numbers)