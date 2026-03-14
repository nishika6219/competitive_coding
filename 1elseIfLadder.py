##else if ladder

# if condition:
#     #statement
# elif condition:
#     #statement
# elif condition:
#     #statement
# else:
#     #default block 

#WAP to accept % and if %    --- 
# %>90==>A
# %>80 ==>B  
# %>60 ==>C
# %<60 ==>FAIL 

n = float(input("enter percentage: "))
if (n>90):
    print("A")
elif (n>80 and n<90):
    print("B")
elif (n>60 and n<80):
    print("C")
else:
    print("FAIL")