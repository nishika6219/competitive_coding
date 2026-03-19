#removing spaces from the string
#rstrip()==> to remove space at rhs
#lstrip()==> to remove space at lhs
#strip()==> to remove space at both sides

city = input("enter the city name: ")
scity=city.strip()
if scity == 'hyderabad':
    print("welcome to hyderabad")
elif scity == 'delhi':
    print("welcome to delhi")
else:
    print("welcome to india")
    