print("Reading file")
file = open("items.txt", 'r')
items = file.readlines()
file.close()

print("Fixing items")
file = open("fixed_items.txt", 'w')
for i in items:
    if ':' not in i and '#' not in i:
        file.write(i.lower())
file.close()

print("Complete")