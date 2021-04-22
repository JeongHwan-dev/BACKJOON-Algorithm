"""
예제 입력 1
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

예제 출력 1
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
"""

n = int(input())
words = []

for _ in range(n):
    word = str(input())
    word_length = len(word)
    words.append((word, word_length))

words = list(set(words))
words.sort(key=lambda word: (word[1], word[0]))

for word in words:
    print(word[0])
