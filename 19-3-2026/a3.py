#input=nishika is a good programmer
#WAP to write to count the words
#output = 4

name = "nishika is a good programmer"
count = 1
for i in name:
    if i == " ":
        count += 1
    else:
        continue
print(count)