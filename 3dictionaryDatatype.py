# #DICTIONARY
# mydict = {
#     "name": "nishika",
#     #key      value
#     "profession": "student",
#     "studentId": 10023
# }
# print(mydict)
# print(type(mydict))



mydict ={
    101: "nishika",
    102: "bhavika",
    103: "mohini",
    104: "namrata",
    101: "arpita",
    104: "shreya"
}
print(mydict)

#with the help of keys to print value 
a = mydict[102]
print(a)

#replace old value by new value
mydict[102] = "peter"
print(mydict)

#only print key x=0,1 (all)
for x in mydict:
    print(x)

#only print values
for x in mydict.values():
    print(x)

#printng key and values both
for x, y in mydict.items():
    print(x,y)


#if i have to add new key and value pair in my dictionar
mydict["mobile_no"]=56467355890
print(mydict)

#imp if we want to represent binary data like image , vid

#pop() method remove pair by specific key name
mydict = {
    101: "nishika",
    "profession": "student",
    "studentId": 10023
}
mydict.pop(101)
print(mydict)