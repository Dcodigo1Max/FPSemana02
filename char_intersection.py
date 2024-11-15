word1 = input()
word2 = input()
same = "" 

for letter in word1:
    set(word1)

for letter in word2:
    if letter in word1:

        if letter not in same:
            same += letter

print(word1)
print(word2)
print(same)



