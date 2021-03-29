"""
예제 입력 1
10 5
1 10 4 9 2 3 8 5 7 6

예제 출력 1
1 4 2 3
"""

n, x = map(int, input().split())
num_list = list(map(int, input().split()))

for i in range(n):
    if num_list[i] < x:
        print(num_list[i], end=" ")
