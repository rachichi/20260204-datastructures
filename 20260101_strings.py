#20260101
print("Hello, World!")

#20260516
##using a WHILE statement and an iteration variable, and the len function, can construct a loop to look at each of the letters in a string individally
fruit  = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
##FOR statmenet. A definite loop is better. 
fruit = 'banana'
for letter in fruit :
    print(letter)
#count number of as
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
#slicing
s = 'Monty Python'
print(s[:2], s[8:], s[:])

