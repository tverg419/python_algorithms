def binary_search(arr, ele):
    left = 0
    right = len(arr) - 1

    # find the middle of the array, check if that is your element
    # if element value is lower, shift right pointer to middle
    # if element value is higher, shift lef tpointer to the middle and check again

    while left < right:
        middle = (right + left) // 2

        if arr[middle]:
            return True
        else:
            if ele > arr[middle]:
                left = middle
            else:
                right = middle
    return False

def binary_recursion(arr, ele):

    length = len(arr)

    if length == 0:
        return False

    else:
        if arr[length // 2] == ele:
            return True
        
        else:
            if arr[length // 2] < ele:
                return binary_recursion(arr[(length //2)+1:], ele)
            else:
                return binary_recursion(arr[: length//2], ele)
    

if __name__ == '__main__':
    # data = [int(x) for x in input("Enter a list of numbers:\n").split()]
    # search = int(input())
    data = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    search = 5

print(binary_recursion(data, search))
