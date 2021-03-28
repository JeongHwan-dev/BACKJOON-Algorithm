"""
예제 입력 1
10 10
예제 출력 1
9 25

예제 입력 2
0 30
예제 출력 2
23 45

예제 입력 3
23 40
예제 출력 3
22 55
"""

h, m = map(int, input().split())
time = (h * 60 + m) - 45
h, m = time // 60, time % 60

if h < 0:
    h += 24

print(h, m)
