"""
예제 입력 1
6 8 10
25 52 60
5 12 13
0 0 0

예제 출력 1
right
wrong
right
"""

while True:
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    max_num = max(nums)
    nums.remove(max_num)
    if nums[0]**2 + nums[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')
