import math


def m_cusum(n, m):
    cusum = 0
    for i in range(m):
        cusum += n
        n = math.sqrt(n)
    return cusum


while True:
    nums = list(map(int, input().split()))
    n, m = nums[0], nums[1]
    print("%.2f" % m_cusum(n, m))
