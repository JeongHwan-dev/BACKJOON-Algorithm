"""
예제 입력 1
100
예제 출력 1
0 1 4

예제 입력 2
189
예제 출력 2
-1
"""

t = int(input())
buttons = [300, 60, 10]
counts = []

for button in buttons:
    count = 0
    count += t // button
    t = t % button
    counts.append(count)

if t == 0:
    for count in counts:
        print(count, end=' ')
else:
    print(-1)
