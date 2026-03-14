#wap to to check if two strings are anagram of each other

#logic check if tthe character counts in both string are the same
#sample ---  input = listen and silent
#output -- anagrams

string1 = input("enter string 1: ")
string2 = input("enter string 2: ")

if( len(string1) and len(string2)):
    print("anagram")
else:
    print("not anagram")