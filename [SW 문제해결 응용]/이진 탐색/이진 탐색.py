import sys
sys.stdin = open('sample_input (2).txt')

def bin_search(arr, target):
    n = len(arr)

    l = 0
    r = n-1

    pre = None

    while l <= r:
        m = (l + r) // 2

        if arr[m] > target:
            r = m - 1
            if pre == 'left':
                return False
            pre = 'left'
        elif arr[m] < target:
            l = m + 1
            if pre == 'right':
                return False
            pre = 'right'
        else:
            return True

    return False

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    A = [*map(int, input().split())]
    B = [*map(int, input().split())]
    A.sort()
    answer = 0
    for b in B:
        if bin_search(A, b):
            answer += 1

    print(f'#{t} {answer}')