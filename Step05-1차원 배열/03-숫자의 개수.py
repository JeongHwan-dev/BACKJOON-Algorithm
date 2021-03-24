"""
예제 입력 1
150
266
427

예제 출력 1
3
1
0
2
0
0
0
2
0
0
"""

a, b, c = [int(input()) for _ in range(3)]
mul = a * b * c

[print(str(mul).count(str(i))) for i in range(10)]
