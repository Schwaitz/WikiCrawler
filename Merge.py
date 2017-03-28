combined = set()

to_combine = "wow.txt"

print("Reading existing words")
file = open("merge.txt")
merge = file.readlines()
file.close()

for i in merge:
    combined.add(i[:-1])

print("Reading new words")
file = open(to_combine)
u_list1 = file.readlines()
file.close()

print("Merging lists")

for i in u_list1:
    combined.add(i[:-1])


print("Writing merge to file")
file = open("merge.txt", "w")
for i in combined:
    file.write(i + "\n")
file.close()

print("Merge complete")


