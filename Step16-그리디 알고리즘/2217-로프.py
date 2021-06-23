"""
예제 입력 1
2
10
15

예제 출력 1
20
"""


def solution():
    max_rope = 0
    rope_arr.sort(reverse=True)

    for i in range(N):
        if max_rope < (rope_arr[i] * (i + 1)):
            max_rope = rope_arr[i] * (i + 1)
    return max_rope


N = int(input())
rope_arr = []

for _ in range(N):
    rope_arr.append(int(input()))

print(solution())
