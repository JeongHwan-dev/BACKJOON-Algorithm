"""
예제 입력 1
2
3 ABC
5 /HTP

예제 출력 1
AAABBBCCC
/////HHHHHTTTTTPPPPP
"""

n = int(input())

for _ in range(n):
    r, s = input().split()
    for i in range(len(s)):
        print(s[i] * int(r), end='')
    print('\n',  end='')
