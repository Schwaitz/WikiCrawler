print("Reading file")
file = open("fixed_items.txt", 'r')
items = file.readlines()
file.close()

item_set = set()

print("Adding items to set")
for i in items:
    it = i[:-1]
    split = it.split('_')
    if len(split) > 1:
        for s in split:
            item_set.add(s)
    item_set.add(it)

print("Writing items to file")
file = open("split_items.txt", 'w')
for i in item_set:
    file.write(i + '\n')
file.close()

print("Complete")