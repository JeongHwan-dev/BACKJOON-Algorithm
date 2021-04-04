"""
예제 입력 1
baekjoon

예제 출력 1
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
"""

s = list(input())
result = []

for n in range(97, 123):
    if chr(n) in s:
        result.append(s.index(chr(n)))
    else:
        result.append(-1)

for idx in result:
    print(idx, end=" ")
