def merge_sort(arr):
    '''
    Split the array into left and right halfs until you get individual lists
    Note: right side will be larger if there is an odd number of element
    Recursively call merge sort until the whole array is broken up completely
    Loop through each list (LH and RH) and start filling in the array with the smallest number of each
    '''
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i,j = 0,0
        arr_index = 0
 
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[arr_index] = left_half[i]
                i += 1
            else:
                arr[arr_index] = right_half[j]
                j += 1
            arr_index += 1
        while i < len(left_half):
            arr[arr_index] = left_half[i]
            i += 1
            arr_index += 1
        while j < len(right_half):
            arr[arr_index] = right_half[j]
            j += 1
            arr_index += 1
    print('Merging', arr)

if __name__ == '__main__':
    numbers = [5, 5, 6, 8, 1, 15, 9, 20, 12, 19, 10, 11, 18, 4, 13, 2, 3, 17, 16, 14, 7]
    print(numbers)
    print(merge_sort(numbers))
    print(numbers)