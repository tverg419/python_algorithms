def bubble_sort(arr):
    
    stop = len(arr) - 1

    while stop > 0:
        for i in range(stop):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
        stop -= 1

if __name__ == "__main__":
    numbers = [5, 6, 8, 1, 15, 9, 20, 12, 19, 10, 11, 18, 4, 13, 2, 3, 17, 16, 14, 7]
    print(numbers)
    bubble_sort(numbers)
    print(numbers)