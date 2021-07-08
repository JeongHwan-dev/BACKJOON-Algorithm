"""
예제 입력 1
8
4
3
6
8
7
5
2
1
예제 출력 1
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-

예제 입력 2
5
1
2
5
3
4
예제 출력 2
NO
"""

n = int(input())

count = 1
stack = []
result = []

for i in range(1, n + 1):   # 데이터 개수 만큼 반복
    data = int(input())
    while count <= data:    # 입력 받은 데이터에 도달할 때까지 삽입
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:   # 스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else:   # 불가능한 경우
        print('NO')
        exit(0)
    
print('\n'.join(result))    # 가능한 경우
