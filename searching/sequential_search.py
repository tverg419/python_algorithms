def seq_search(arr, ele):

    for val in arr:
        if val == ele:
            return True
    
    return False

def seq_search_ordered(arr, ele):

    index = 0

    while index < len(arr):
        if arr[index] == ele:
            return ele
        else:
            if arr[index] > ele:
                return False
            else:
                index += 1

if __name__ == '__main__':
    data = [int(x) for x in input("Enter a list of numbers:\n").split()]
    search = int(input())

print(seq_search_ordered(data, search))
