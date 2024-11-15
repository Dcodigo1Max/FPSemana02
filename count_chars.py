input = input()
input = input.split()
book = {}

for word in input:

    book[word] = len(word)

print(book)

