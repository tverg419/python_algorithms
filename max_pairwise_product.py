'''
Find the maximum product of two distinct numbers
in a sequence of non-negative integers.

Input:
3
1 2 3

Output:
6

'''
def max_pairwise_product_naive(numbers):

    n = len(numbers)
    max_product = 0

    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product(numbers):

    first_max = 0
    second_max = 0

    for number in numbers:
        if (number > first_max):
            second_max = first_max
            first_max = number
        elif (first_max >= number > second_max):
            second_max = number


    return first_max * second_max
    
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))