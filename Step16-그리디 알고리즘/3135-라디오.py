"""
예제 입력 1
100 15
1
15
예제 출력 1
1

예제 입력 2
88 17
3
18
1
42
예제 출력 2
2
"""

A, B = map(int, input().split())
N = int(input())
btns = []
start = A
count = 0

for i in range(N):
    btns.append(int(input()))

for btn in btns:
    if abs(start - B) > abs(btn - B):
        start = btn

if start != A:
    count = abs(start - B) + 1
else:
    count = abs(start - B)

print(count)
