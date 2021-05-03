"""
예제 입력 1
10
예제 출력 1
3628800

예제 입력 2
0
예제 출력 2
1
"""


def factorial(num):
    if num <= 0:
        return 1
    return num * factorial(num - 1)


n = int(input())
print(factorial(n))
