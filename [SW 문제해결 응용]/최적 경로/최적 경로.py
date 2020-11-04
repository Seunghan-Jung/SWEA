import sys

sys.stdin = open('input.txt')


def dfs(x, y, dist, n):
    global answer

    if dist >= answer:
        return

    if n == N:
        answer = min(answer, dist + abs(x-ex) + abs(y-ey))

    for i in range(N):
        if visit[i]:
            continue

        visit[i] = True
        nx, ny = C[i]
        dfs(nx, ny, dist + abs(x - nx) + abs(y - ny), n+1)
        visit[i] = False


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    sx, sy, ex, ey, *customers = map(int, input().split())
    C = []

    for i in range(0, len(customers), 2):
        x = customers[i]
        y = customers[i + 1]

        C.append((x, y))
    visit = [False] * N
    answer = float('inf')
    dfs(sx, sy, 0, 0)

    print(f'#{t} {answer}')
