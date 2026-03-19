s= [i*i for i in range(1,11)]
print(s)
#s is a list which is created using list comprehension. it will iterate through the range of
print("----------")
###[1,4,9,16,25,36,49,64,81,100]
val = [2**i for i in range(1,6)]# i =1,2,3,4,5
print(val)

print("------------")
val2=[i for i in range(1,11) if i%2==0]
print(val2)