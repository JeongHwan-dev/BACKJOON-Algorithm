"""
예제 입력 1
3
124
25
194

예제 출력 1
4 2 0 4
1 0 0 0
7 1 1 4
"""

n = int(input())
charge_list = [int(input()) for _ in range(n)]
coin_list = [25, 10, 5, 1]
result = []

for charge in charge_list:
    charge_result = []
    for coin in coin_list:
        charge_result.append(charge // coin)
        charge = charge % coin
    result.append(charge_result)

for counts in result:
    for c in counts:
        print(c, end=' ')
    print()
