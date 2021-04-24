"""
예제 입력 1
26
예제 출력 1
4

예제 입력 2
55
예제 출력 2
3

예제 입력 3
1
예제 출력 3
60
"""

n = original_n = int(input())
count = 0

while True:
    ten = n // 10
    one = n % 10
    total = ten + one
    count += 1
    n = int(str(one) + str(total % 10))
    if original_n == n:
        break

print(count)
