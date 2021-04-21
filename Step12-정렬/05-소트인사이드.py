"""
예제 입력 1
2143

예제 출력 1
4321
"""

n = list(map(str, input()))
n.sort()
n.reverse()

print(''.join(n))

