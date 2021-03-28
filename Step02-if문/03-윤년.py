"""
예제 입력 1
2000
예제 출력 1
1

예제 입력 2
1999
예제 출력 2
0
"""

year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(1)
else:
    print(0)
