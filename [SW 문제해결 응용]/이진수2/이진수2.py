# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):

    N = float(input())

    res = []

    while N != 0.0:

        N *= 2
        if N >= 1:
            res.append(1)
            N -= 1
        else:
            res.append(0)

    answer = ''.join(map(str, res)) if len(res) <= 12 else 'overflow'

    print(f'#{t} {answer}')
