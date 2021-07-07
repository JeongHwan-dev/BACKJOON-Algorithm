"""
예제 입력 1
5 21
5 6 7 8 9
예제 출력 1
21

예제 입력 2
10 500
93 181 245 214 315 36 185 138 216 295
예제 출력 2
497
"""

n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))

result = 0
length = len(cards)

for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum_value = cards[i] + cards[j] + cards[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)
