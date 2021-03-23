"""
예제 입력 1
5
20 10 35 30 7

예제 출력 1
7 35
"""

n = int(input())
n_list = list(map(int, input().split()))

print(min(n_list), max(n_list))
