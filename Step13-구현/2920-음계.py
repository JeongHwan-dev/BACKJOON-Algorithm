"""
예제 입력 1
1 2 3 4 5 6 7 8
예제 출력 1
ascending

예제 입력 2
8 7 6 5 4 3 2 1
예제 출력 2
descending

예제 입력 3
8 1 7 2 6 3 5 4
예제 출력 3
mixed
"""

arr = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if arr[i] > arr[i - 1]:
        descending = False
    elif arr[i] < arr[i - 1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
