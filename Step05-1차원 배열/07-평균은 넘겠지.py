"""
예제 입력 1
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

예제 출력 1
40.000%
57.143%
33.333%
66.667%
55.556%
"""

n = int(input())
result = []

for i in range(n):
    score = list(map(int, input().split()))
    avg = (sum(score) - score[0]) / score[0]
    count = 0

    for i in range(1, score[0] + 1):
        if score[i] > avg:
            count += 1

    rate = ("{:.3f}%".format(round(count / score[0] * 100, 3)))
    result.append(rate)

for rate in result:
    print(rate)
