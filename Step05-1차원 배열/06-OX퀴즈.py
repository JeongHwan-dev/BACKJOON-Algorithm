"""
예제 입력 1
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

예제 출력 1
10
9
7
55
30
"""

n = int(input())
result_list = [input() for _ in range(n)]

for r in result_list:
    score = 0
    count = 1
    for i in list(r):
        if i == 'O':
            score += count
            count += 1
        else:
            count = 1
    print(score)
