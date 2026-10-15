#20260516
##string concatenation
a = "Hello"
b = a + "There"
print(b)
c = a + ' ' + "There"
print(c)
##in as a logical operator
fruit = 'banana'
print('n' in fruit, 'nan' in fruit)
if 'a' in fruit:
    print("Found it!")
##string library
greet = 'Hello Bob'
zap = greet.lower()
print(zap, 'Hi There!'.lower())
##definitions of things
stuff = 'Hello world'
print(type(stuff))
print(dir(stuff))
##startswith
greet = '    Hello Bob     '
print(greet.lstrip().startswith('H'))
##parsing and extracting
data = 'From rachel.liu.1688@gmail.com Sat Jan 5 09:14:16 2008'
atpos = data.find('@') #search for the start of something
sppos = data.find(' ',atpos) #search for the end of something
host = data[atpos+1 : sppos] #extract between becaused starts at the first position, ends before the second position
print(host)
#every string inside of python3 is capable of representing all character sets