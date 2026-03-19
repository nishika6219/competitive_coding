#replacing a string with another string
#s.replae(oldstring, newstring,)
#inside s, every occurrence of oldstring will be replaced with newstring and it will return a new string. it will not change the original string because string is immutable.

s = "this is difficult"
s1 = s.replace("difficult", "easy")
print(s1)

# all occurrences will be replaced
s = "abababababababa"
s1 = s.replace("a", "b")
print(s1)