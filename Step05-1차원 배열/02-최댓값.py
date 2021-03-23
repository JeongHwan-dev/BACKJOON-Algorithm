"""
예제 입력 1
3
29
38
12
57
74
40
85
61

예제 출력 1
85
8
"""

n_list = list(int(input()) for _ in range(9))

print(max(n_list))
print(n_list.index(max(n_list)) + 1)
