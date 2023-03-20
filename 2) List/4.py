"""
How does dynamic size work?
1) Preallocating some extra space
2) If the memory becomes full :
- Allocate a new space of larger size (Multiply by x(For python it is 1.125))
- Copy old space to new
- Free old space

Theory:

Assumption : Initially space for 10 items is allocated and x = 2

Then when you add the 11th element, the old block is memory is deallocated and a new block of memory is allocated 
which is double the size (in this ex 20). Same thing will happen when you add 21st element, 41st elemnt, 81st element and so on.

So this is how dynamic memory is allocated

Appending a list has a constant time complexity but remember this is only if you are adding or removing an element at the end of the list.
Adding an element in the middle has theta n time complexity.
"""