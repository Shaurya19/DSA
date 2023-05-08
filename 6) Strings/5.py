# More string operations

s1 = "geeks"
print(len(s1))
s2 = s1.upper()
print(s2)
s3 = s2.lower()
print(s3)
print(s1.islower())
print(s2.isupper())

s = "GeeksforGeeks Python course"
print(s.startswith("Geeks"))
print(s.endswith("course "))
print(s.startswith("Geeks",1)) # Start searching from index 1 
print(s.startswith("Geeks",8,len(s))) # 