# # # ##part 1
# # # #tuples are not mutable which means it can be stored more densely than lists. you can append, index, but not sort, extend, etc. 
# # # #assignment. can put on left hand side of assignment statement.
# # # (x,y) = (4,'fred')
# # # print(y)
# # # (a,b) = (99,98)
# # # print(a)
# # # #.items() prints out list of tuples 
# # # d = dict()
# # # d['csev'] = 2
# # # d['cwen'] = 4
# # # for (k,v) in d.items():
# # #     print(k,v)
# # # tups = d.items()
# # # print(tups)
# # # #sorting tuples
# # # d = {'a':10, 'c':22, 'b':1}
# # # print(d.items())
# # # #sorted(d.items()) #sorts by the first element. also dictionary cannot have more than one key. iterating through now.
# # # print(sorted(d.items()))
# # # for k,v in sorted(d.items()):
# # #     print(k,v)
# # # #sorting by values
# # # c = {'a':10, 'b':1, 'c':22}
# # # tmp = list()
# # # for k,v in c.items():
# # #     tmp.append((v,k)) #reversing order
# # # print(sorted(tmp, reverse = True)) #reversing sort 

# # #top 10 words
# # fhand = open('romeo.txt')
# # #fh = read(fhand) only need to read if want to read the whole thing 

# # wordCount = dict() #this is a dictionary so we can add stuff to it
# # for line in fhand:
# #     words = line.split() #for word in line:
# #     for word in words:
# #         wordCount[word] = wordCount.get(word,0) + 1 

# # listByVal = list() #because might not work if values are same number. this is a list of tuples
# # for k,v in wordCount.items(): #need to get the items so it can be iterated through
# #     listByVal.append((v,k))


# # sortByVal = sorted(listByVal, reverse = True) #this is just a sorted version of that list of tuples.

# # topTen = list() 
# # for k,v in sortByVal[:10]: #iterating through the tuples of the list of tuples, for just the first 10 keys
# #     topTen.append((k,v))
# # print(topTen)

# # #shorter version of flipping
# # print(sorted([(v,k) for k,v in wordCount.items()], reverse=True)[:10]) 

# x = (5, 1, 3)
# if (6, 0, 0) > x :
#     print('Yes')
# else:
#     print('Not')


## Assignment: Sort and Count Messages 
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
fh = open('mbox-short.txt')

counts = dict()
for line in fh:
    if line.startswith('From '):
        words = line.split()
        hour = words[5].split(':')[0]
        counts[hour] = counts.get(hour,0) + 1
sortedCounts = sorted(counts.items())

for k,v in sortedCounts:
    print(k, v)



