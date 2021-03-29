"""
예제 입력 1
3
40 80 60
예제 출력 1
75.0

예제 입력 2
3
10 20 30
예제 출력 2
66.666667

예제 입력 3
4
1 100 100 100
예제 출력 3
75.25
"""

n = int(input())
s = list(map(int, input().split()))
new_s = []

for i in range(n):
    new_s.append(s[i] / max(s) * 100)

average = sum(new_s) / n
print(average)
