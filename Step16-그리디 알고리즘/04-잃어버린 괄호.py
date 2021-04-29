"""
예제 입력 1
55-50+40

예제 출력 1
-35
"""

array = input().split('-')
num_list = []

for a in array:
    n_list = a.split('+')
    s = 0
    for n in n_list:
        s += int(n)
    num_list.append(s)

result = num_list[0]

for i in range(1, len(num_list)):
    result -= num_list[i]

print(result)
