"""
예제 입력 1
110
예제 출력 1
99

예제 입력 2
1
예제 출력 2
1
"""


def hansu(x):
    hansu = 0

    for n in range(1, x + 1):
        if n <= 99:
            hansu += 1
        else:
            nums = list(map(int, str(n)))
            if nums[0] - nums[1] == nums[1] - nums[2]:
                hansu += 1
    return hansu


num = int(input())
print(hansu(num))
