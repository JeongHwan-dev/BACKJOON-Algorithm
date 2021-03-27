"""
예제 입력 1
5 8 4

예제 출력 1
1
1
0
0
"""

a, b, c = map(int, input().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
