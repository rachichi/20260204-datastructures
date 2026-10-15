str = 'banana'
# beg = 0
# end = len(str) - 1
# for i in str:
#     print(i, beg, str[end], end)
#     beg = beg + 1
#     end = end - 1
##iterate through the string, when it gets to an a, make it capital and say "oh no!", when it gets to n, replace with x and say "yay!".
g = 0
newstr = ""
for i in str:
    if str[g] == 'a':
        add = str[g].upper()
        print(add,'oh no!')
        g = g + 1
    elif str[g] == 'n':
        add = 'x'
        print(add, 'yay!')
        g = g + 1
    else:
        add = str[g]
        print(add,'nothing exciting here') 
        g = g + 1
    newstr = ''.join([newstr,add])
    print(newstr)

print(str.replace('a','A').replace('n','x'))


##playing with built in formulas 
##'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print("hello".center(20,"0"))
print("helloelellelelelelleelel".count("el",0,4))
print("hello".encode('utf-8','strict'))
print('hello'.isupper())
print('banana'.replace('a','x',2))
print(' '.join(['haha','ur','funny']))