"""
예제 입력 1
60
100
예제 출력 1
620
61

예제 입력 2
64
65
예제 출력 2
-1
"""

m = int(input())
n = int(input())
result = []


def is_prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


for num in range(m, n + 1):
    if is_prime_number(num) is True:
        result.append(num)

if not result:
    print(-1)
else:
    print(sum(result))
    print(min(result))

