"""
예제 입력 1
5
3 1 4 3 2

예제 출력 1
32
"""

n = int(input())
array = list(map(int, input().split()))
array.sort()
t = 0

for i in range(n):
    t += array[i] * (n - i)

print(t)
