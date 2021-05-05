"""
예제 입력 1
380

예제 출력 1
4
"""

price = int(input())
change = 1000 - price
coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
    count += change // coin
    change = change % coin

print(count)
