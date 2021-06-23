"""
예제 입력 1
2
3 4
예제 출력 1
12

예제 입력 2
3
2 2 2
예제 출력 2
12
"""

n = int(input())
slime_arr = list(map(int, input().split()))

slime_arr.sort(reverse=True)
score = 0
total = 0

for i in range(n-1):
    score = slime_arr[i] * slime_arr[i+1]
    slime_arr[i+1] = slime_arr[i] + slime_arr[i+1]
    total += score

print(total)
