import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
### The runtime for this is Polynomial O(n^c)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

################## ----- My Solution Starts Here ----- #####################

### Potential optimizations?
###     -To hit stretch, the sprint mentions a solution of O(n log n) or better. 
###         -is it possible to use a binary search tree? How would you compare strings? Would I need to
###             modify the logic?
###         - Would it be beneficial to sort the files alphabetically and then do a binary search?
###             (pretty much the BST)
###         - Would DLL/que/stack be beneficial here? (Currently can not think of a solution with them)

### Objective
###     - Research viability of BST with string values.
###         - Comparison operators can be used on strings, it compares my individual characters and then
###             by the unicode when the character is different. So the BST should be viable to use.

bst = BinarySearchTree()

for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)
### This would be O(n log n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

###### --- STRETCH --- ######

# hash table (dict and set) has the best search time complexities
stretch_time = time.time()

names_set = set(names_1)
stretch_dups = []

for name in names_2:
    if name in names_set:
        stretch_dups.append(name)

end_stretch_time = time.time()
print (f"\n\n{len(stretch_dups)} Stretch-dups:\n\n{', '.join(duplicates)}\n\n")
print (f"Stretch_runtime: {end_stretch_time - stretch_time} seconds")