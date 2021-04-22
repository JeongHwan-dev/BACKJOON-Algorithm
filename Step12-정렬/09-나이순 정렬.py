"""
예제 입력 1
3
21 Junkyu
21 Dohyun
20 Sunyoung

예제 출력 1
20 Sunyoung
21 Junkyu
21 Dohyun
"""

n = int(input())
members = []

for i in range(n):
    age, name = input().split()
    i += 1
    members.append((i, int(age), name))

members.sort(key=lambda member: (member[1], member[0]))

for member in members:
    print(member[1], member[2])
