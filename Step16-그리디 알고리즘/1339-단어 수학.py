"""
예제 입력 1
2 162
예제 출력 1
5

예제 입력 2
4 42
예제 출력 2
-1
"""

A, B = map(int, input().split())
count = 1

while True:
    if A == B:
        break
    elif A > B or (B % 10 != 1 and B % 2 != 0):
        count = -1
        break
    elif B % 2 == 0:
        B = B // 2
        count += 1
    else:
        B = (B - 1) // 10
        count += 1

print(count)
