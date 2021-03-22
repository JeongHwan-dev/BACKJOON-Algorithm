"""
예제 입력 1
5
1 1
2 3
3 4
9 8
5 2

예제 출력 1
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
"""

n = int(input())
result = []

for _ in range(n):
    a, b = map(int, input().split())
    result.append([a, b])

for i in range(n):
    print(f'Case #{i+1}: {result[i][0]} + {result[i][1]} = {sum(result[i])}')

