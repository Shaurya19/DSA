# Formatted strings in python

name = "Shaurya"
love = "coding"

s1 = "My name is %s and I love %s"%(name, love)
print(s1)
s2 = "My name is {} and I love {}".format(name,love)
print(s2)
s3 = f"My name is {name} and I love {love}"
print(s3)

a = 10
b = 20

s4 = f"Product of {a} and {b} is {a*b}."
print(s4)

s1 = "ABC"
print(f"lower case of {s1} is {s1.lower()}")