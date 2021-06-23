"""
예제 입력 1
200
예제 출력 1
19
"""


def solution(n):
    temp = 1
    count = 0

    while True:
        n -= temp

        if n >= 0:
            count += 1
            temp += 1
        else:
            break

    return count


N = int(input())
print(solution(N))
