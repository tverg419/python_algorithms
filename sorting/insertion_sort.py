def insertion_sort(arr):

    for i in range(1, len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            


if __name__ == "__main__":
    numbers = [5, 6, 8, 1, 15, 9, 20, 12, 19, 10, 11, 18, 4, 13, 2, 3, 17, 16, 14, 7]
    print(numbers)
    insertion_sort(numbers)
    print(numbers)