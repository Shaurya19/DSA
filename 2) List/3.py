l = [10,40,20,50]
print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)

# If the elements in the list are strings then they are compared lexographically

# In python every element in the list is referenced i.e it gives the address of the elements
# Continous block of memory
# The elements may or may not be in continous memory blocks

"""
Advantages:
1) Random Acess
2) Cache Friendly

Disadvantages:
1) Insertion, deletion and search is slow because lists are ordered therefore it does linear search for
insertion, deletion and search. In insertion and deletion the position of the elements is changed everytime which takes time
2) Sorting is slow because linearly the whole list needs to be searched.
Therefore sets and dictionaries are faster because they are not ordered.
"""