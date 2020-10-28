import sys

sys.stdin = open('input.txt')



def find():
    for j in reversed(range(M)):
        for i in range(N):
            if arr[i][j] == 1:
                return i, j - 55


def solution():
    code = []

    for k in range(8):
        y = sy + k * 7

        temp = tuple(arr[sx][y:y + 7])

        if temp in D:
            code.append(D[temp])
        else:
            return 0

    if (sum(code[:-1:2]) * 3 + sum(code[1:-1:2]) + code[-1]) % 10 == 0:
        return sum(code)
    else:
        return 0

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [[*map(int, input())] for _ in range(N)]

    sx, sy = find()

    D = {
        (0, 0, 0, 1, 1, 0, 1): 0,
        (0, 0, 1, 1, 0, 0, 1): 1,
        (0, 0, 1, 0, 0, 1, 1): 2,
        (0, 1, 1, 1, 1, 0, 1): 3,
        (0, 1, 0, 0, 0, 1, 1): 4,
        (0, 1, 1, 0, 0, 0, 1): 5,
        (0, 1, 0, 1, 1, 1, 1): 6,
        (0, 1, 1, 1, 0, 1, 1): 7,
        (0, 1, 1, 0, 1, 1, 1): 8,
        (0, 0, 0, 1, 0, 1, 1): 9,
    }

    answer = solution()

    print(f'#{t} {answer}')
