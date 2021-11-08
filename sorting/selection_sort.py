def selection_sort(arr):
    
    for i in range(len(arr)-1,0,-1):

        max_index = 0;

        for j in range(i+1):

            if arr[j] > arr[max_index]:
                max_index = j
                
        temp = arr[i]
        arr[i] = arr[max_index]
        arr[max_index] = temp

if __name__ == "__main__":
    numbers = [5, 6, 8, 1, 15, 9, 20, 12, 19, 10, 11, 18, 4, 13, 2, 3, 17, 16, 14, 7]
    print(numbers)
    selection_sort(numbers)
    print(numbers)