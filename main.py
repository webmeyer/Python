#Example

n = int(input())
books = []

while n > 0:
    abc = input()
    n -= 1

k = int(input())
for i in range(n):
    books = books.append([k])
print(books)