#add and remove pair in dict
# remove key value pair from dictionary
#write a ufnction to remmove key value pair from 
#use pop()

mydict = {
    "name": "nishika",
    "age": 19
}

mydict["mobile_no"] = 56467355890
print(mydict)

mydict.pop("age")
print(mydict)

print(mydict.get("name"))
