"""
예제 입력 1
9
5 12 7 10 9 1 2 3 11
13

예제 출력 1
3
"""

n = int(input())
num_list = list(map(int, input().split()))
x = int(input())

num_list.sort()

left, right = 0, n - 1
ans = 0

while left < right:
    tmp = num_list[left] + num_list[right]
    if tmp == x:
        ans += 1
        right -= 1
    elif tmp < x:
        left += 1
    else:
        right -= 1

print(ans)
