"""
예제 입력 1
1000 70 170
예제 출력 1
11

예제 입력 2
3 2 1
예제 출력 2
-1
"""

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(a // (c - b) + 1)
