"""
예제 입력 1
5

예제 출력 1
*
**
***
****
*****
"""

n = int(input())

[print('*' * i) for i in range(1, n+1)]
