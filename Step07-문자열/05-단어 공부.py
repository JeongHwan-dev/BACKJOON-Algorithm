"""
예제 입력 1
Mississipi
예제 출력 1
?

예제 입력 2
zZa
예제 출력 2
Z

예제 입력 3
z
예제 출력 3
Z
"""

word = input().upper()
unique_words = list(set(word))

count_list = []

for x in unique_words:
    count = word.count(x)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    max_index = count_list.index(max(count_list))
    print(unique_words[max_index])
