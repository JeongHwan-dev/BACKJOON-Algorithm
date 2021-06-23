"""
예제 입력 1
3 10
10 11 13
예제 출력 1
12

예제 입력 2
9 1
9 5 8 1 3 2 7 6 4
예제 출력 2
10
"""

n, l = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()

for fruit in fruits:
    if fruit <= l:
        l += 1

print(l)
