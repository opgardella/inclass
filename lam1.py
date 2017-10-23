L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
        
y = sorted(d.keys())
for x in y:
    print (str(x) + " appears " + str(d[x]) + " times")

# or in reverse order
print ("---------")
for x in sorted(d.keys(), reverse = True):
     print (str(x) + " appears " + str(d[x]) + " times")


L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

items = d.items();
sorted_items = sorted(items, key = lambda x: x[1], reverse=True)
for x in sorted_items:
    print (str(x[0]) + " appears " + str(x[1]) + " times")

