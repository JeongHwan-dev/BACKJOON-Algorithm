"""
예제 입력 1
18
예제 출력 1
4

예제 입력 2
4
예제 출력 2
-1

예제 입력 3
6
예제 출력 3
2
"""

n = int(input())
count = 0

while n >= 0:
    if n % 5 == 0:
        count += (n // 5)
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)
