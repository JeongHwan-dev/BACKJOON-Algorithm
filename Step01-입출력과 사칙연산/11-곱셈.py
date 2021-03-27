"""
예제 입력 1
472
385

예제 출력 1
2360
3776
1416
181720
"""

n1 = int(input())
n2 = input()

result = 0

for i in range(1, 4):
    result += n1 * int(n2[-i]) * (10 ** (i - 1))
    print(n1 * int(n2[-i]))

print(result)
