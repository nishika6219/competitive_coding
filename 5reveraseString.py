#WAP to reverse a string with any loop

#without loop
name ="nihika"
print(name[::-1])

#with loop
name = "deotale"
reverse = ""

for i in name:
    reverse = i + reverse

print("Original:", name)
print("Reverse:", reverse)
