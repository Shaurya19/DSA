# Check if a string is an anagram or not
# Anagram - all the characters in one string appear in another string amd the number of occurence of all characters should also be same

 # Naive soln - sort both the arrays and then check if they are equal   TC: O(nlogn)


s1 = "abbca"
s2 = "acabb"

if len(s1) != len(s2):
    print(False)

count = [0]*256

for i in range(len(s1)):
    count[ord(s1[i])] += 1
    count[ord(s2[i])] -= 1

    # Python ord() function takes string argument of a single Unicode character 
    # and return its integer Unicode code point value.

for i in count:
    if i != 0:
        print(False)
else:
    print(True)