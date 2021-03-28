"""
예제 입력 1
12
5
예제 출력 1
1

예제 입력 2
9
-13
예제 출력 2
4
"""

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
