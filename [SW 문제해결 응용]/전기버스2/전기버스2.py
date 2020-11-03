import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, *B = map(int, input().split())

    battery = B[0]
    cur = 0
    cnt = 0
    while cur < N:

        if cur + battery >= N - 1:
            break
        optimal_dist = 0
        optimal_val = 0

        for dist in range(1, battery + 1):
            temp = cur + dist + B[cur + dist]

            if optimal_val < temp:
                optimal_dist = dist
                optimal_val = temp

        cur += optimal_dist
        battery = B[cur]
        cnt += 1

    print(f'#{t} {cnt}')
