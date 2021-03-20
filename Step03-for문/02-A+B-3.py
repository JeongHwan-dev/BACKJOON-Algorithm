"""
예제 입력 1
5
1 1
2 3
3 4
9 8
5 2

예제 출력 1
2
5
7
17
7
"""

n = int(input())
result = []

for _ in range(n):
    num1, num2 = map(int, input().split())
    result.append(num1 + num2)


[print(r) for r in result]
