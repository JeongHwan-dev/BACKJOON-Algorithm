"""
예제 입력 1
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
예제 출력 1
6

예제 입력 2
10 4790
1
5
10
50
100
500
1000
5000
10000
50000
예제 출력 2
12
"""

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
coins.sort(reverse=True)
count = 0

for coin in coins:
    count += k // coin
    k = k % coin

print(count)
