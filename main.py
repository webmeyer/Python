# Example

words = input().split()
new_words = []

for word in words:
    new_word = word[1:] + word[0] + 'ки'
    new_words.append(new_word)
print(*new_words, sep=' ')
