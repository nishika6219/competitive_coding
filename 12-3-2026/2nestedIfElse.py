#WAP to accept  three paper marks and check maximum marks using nested if else

#nested ifelse
# if condition1:
#     if condition2:
#         # statement when condition1 AND condition2 are True
#     else:
#         # statement when condition1 is True but condition2 is False
# else:
#     if condition2:
#         # statement when condition1 is False but condition2 is True
#     else:
#         # statement when BOTH condition1 and condition2 are False

n1= int(input("enter maths marks:"))
n2= int(input("enter phy marks:"))
n3= int(input("enter chem marks:"))

if(n1>n2):
    if(n1>3):
        print("maths is highest")
    else:
        print("chem is highest")
else:
    if(n2>n3):
        print("phy is highest")
    else:
        print("chem is greater")


