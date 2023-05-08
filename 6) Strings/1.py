# Strings are immutable

# Multiple line string

s1 = """Hi,
My name is Shaurya.
I am learning Python"""

print(s1)
# Use escape sequences to put single quotes within single quotes and same for double quotes

s2 = 'Welcome to Geek\'s'
print(s2)

# To skip a line

s3 = "Take me to the \n next line"
print(s3)

# To print a backlash use two backlashes

s4 = '\\n'
print(s4)

# To ignore the escape sequences wherein you want to print the backlashes using a raw string

s5 = "C:\project\name.py"
s6 = r"C:\project\name.py"
print(s5)
print(s6)