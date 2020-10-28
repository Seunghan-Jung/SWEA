import sys
sys.stdin = open('input.txt')

def deci_to_ternary(deci: int):

    res = []

    while deci:
        res.append(deci % 3)
        deci //= 3

    return ''.join(map(str, reversed(res)))


T = int(input())

for tc in range(1, T + 1):

    b = list(input())
    t = input()

    answer = 0

    for i in range(len(b)):
        b[i] = '1' if b[i] == '0' else '0'

        temp = deci_to_ternary(int(''.join(b), base=2))

        if len(t) != len(temp):
            b[i] = '1' if b[i] == '0' else '0'
            continue

        diff = 0
        for j in range(len(t)):
            if t[j] != temp[j]:
                diff += 1

        if diff == 1:
            answer = int(''.join(temp), base=3)
            break

        b[i] = '1' if b[i] == '0' else '0'


    print(f'#{tc} {answer}')
