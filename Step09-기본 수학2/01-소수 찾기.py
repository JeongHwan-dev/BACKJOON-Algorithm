"""
예제 입력 1
4
1 3 5 7

예제 출력 1
3
"""

n_length = int(input())
n_list = list(map(int, input().split()))
count = 0

for n in n_list:
    error = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                error += 1
        if error == 0:
            count += 1

print(count)
