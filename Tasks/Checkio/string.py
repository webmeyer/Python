#Checkio

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    words = text.split()
    return words[0]


print(first_word('a word'))
print(first_word('Димка - дурачок :D'))
print(first_word('hi'))