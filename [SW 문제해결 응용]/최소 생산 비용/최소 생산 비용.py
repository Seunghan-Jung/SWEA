import sys

sys.stdin = open('input.txt')


def dfs(n, s):
    global answer

    if s >= answer:
        return

    if n == N:
        answer = s


    for j in range(N):
        if visit[j]:
            continue

        visit[j] = True
        dfs(n + 1, s + G[n][j])
        visit[j] = False


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    visit = [False] * N

    G = [[*map(int, input().split())] for _ in range(N)]

    answer = float('inf')
    dfs(0, 0)

    print(f'#{t} {answer}')
