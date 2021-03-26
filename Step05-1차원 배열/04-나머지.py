"""
예제 입력 1
1
2
3
4
5
6
7
8
9
10
예제 출력 1
10

예제 입력 2
42
84
252
420
840
126
42
84
420
126
예제 출력 2
1

예제 입력 3
39
40
41
42
43
44
82
83
84
85
예제 출력 3
6
"""

n_list = []
result = []

[n_list.append(int(input())) for _ in range(10)]
[result.append(n % 42) for n in n_list]

print(len(set(result)))
