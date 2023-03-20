#sort()
#--- Works only for list.
#--- Sorts in-place

#sorted()
#--- Works for any iterable.
#--- Does not modify the passed container 
#--- Returns a list of sorted items

# Both these methods use Tim Sort (combo of merge and insertion sort) and are stable
# TC: O(n*log n)

l1 = [5,10,15,1]
l1.sort()
print(l1)

# Sorting in descending order
l2 = [1,5,3,10]
l2.sort(reverse=True)
print(l2)

l3 = ["gfg","ide","courses"]
l3.sort()
print(l3)