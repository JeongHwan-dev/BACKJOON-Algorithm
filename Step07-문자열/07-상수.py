"""
예제 입력 1
734 893

예제 출력 1
437
"""


def change_sangsu(n):
    return int(n[0]) + (int(n[1]) * 10) + (int(n[2]) * 100)


n1, n2 = input().split()
print(max(change_sangsu(n1), change_sangsu(n2)))
