"""
예제 입력 1
5
3 4
1 1
1 -1
2 2
3 3

예제 출력 1
1 -1
1 1
2 2
3 3
3 4
"""

n = int(input())
coordinate = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append([x, y])

coordinate.sort()

for x, y in coordinate:
    print(x, y)
