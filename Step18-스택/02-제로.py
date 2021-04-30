"""
예제 입력 1
4
3
0
4
0
예제 출력 1
0

예제 입력 2
10
1
3
5
4
0
0
7
0
0
6
예제 출력 2
7
"""

k = int(input())
stack = []

for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
