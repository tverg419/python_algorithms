## Naive solution, checks each number between 1 and sum of a and b
def gcf_naive(a, b):
    if a <= 0 or b <= 0:
        return -1
    else:
        factor = -1
        for div in range(1, a+b):
            if (a / div == 0) and (b / div == 0):
                factor = div
        return factor

def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

print(gcf(357, 234))