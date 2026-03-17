# mylist = ["prasshant", "ashish", "komal","ankush",77 ,"sandeep",60.52 ,"nishika"]
# # print(mylist)
# # print(type(mylist))
# # print(mylist[1])
# # print(mylist[2])
# # print(mylist[5])
# # print(mylist[2:5]) #2,3,4
# # print(mylist[1:8:2]) # confusion
# # print(mylist[:]) #all
# # print(mylist[: : -1])# start from the end

# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)

# #inert at a perticular index
# mylist.insert(1,"sanket")
# print(mylist)

# #remove 
# mylist.remove("sandeep")
# print(mylist)

# #cloning
# newlist = mylist.copy() 
# print(mylist)
# print(newlist)


# mylist = [['nishika', 'deotale'],['85.56'], [93356,"yyy"]]
# print("exammple of multidementional list:")
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])          
# print(mylist[2][1])
# # decode 
# # [    0            1
# # 0 ['nishika', 'deotale'],
# # 1 ['85.56'], 
# # 2 [93356,"yyy"]
# # ]

# list1 =['nishika','deotale']
# print(list1)
# print(list1*2) #will print twice

# list2=[40,25,50]
# print(list1+list2)

# del list2[2]
# print(list2)
# del list2
# #print(list2) #print ni hoga as mem se completely delete ho chuka h so it will give error

# #clear funtion
# list2 = [50,60,30,'nish']
# print(list2)
# list2.clear()
# print(list2)

# #typecasting
# name ='nishika'
# print(name)
# myname =list(name)
# print(myname) #['n', 'i', 's', 'h', 'i', 'k', 'a']

# #sorting
# # reverse= True
# # default sorting order for number is asending order
# #     default sorting order for string is apha order
# #     it should be homogeneous other wise it will get typeerror 

# mylist = [22,44,55,0,5,11]
# mylist.sort()
# print(mylist) #[0, 5, 11, 22, 44, 55]
# mylist.sort(reverse=True)
# print(mylist) #[55, 44, 22, 11, 5, 0]

# #id function is use to return the mem address of the variable
# math = 10
# print(id(math))

# # wil give same memory address  for both math n phy
# math =50
# phy =50
# print(id(math)) #140730377009608
# print(id(phy))  #140730377009608


# #alising means assignng one variable reference to another variable
# mylist=[3,4,5,622,56,0,9]
# newlist =mylist
# print(id(mylist)) #2868546004416
# print(id(newlist)) #2868546004416


#looping
# #2 types os special operator -membreship ND IDENTFY operation
# #membership operator = 1. in     2.not it
# name = 'nishika'
# print('Z' in name)
# print('Z'  not in name)


# for i in range(6): # 0 to 6 jayega
#     print(i)
# for i in range(1,6): # 1 to 6
#     print(i)


# for i in range(1,10,2):
#     print(i)

# for i in range(1,10,3):
#     print(i) #1,3,6,9

# for i in range(5,0,-1):
#     print(i) #5,4,3,2

# for i in range(-1,11):
#     print(i*2)
# for i in range(1,10,2):
#     print(i)

# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
# print("--------------------------------------")
# for i in range(1,11):
#     print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)


# #wap to accept any digit and check that pos, neg, zero

# no = int(input("enter any digit"))
# if no>0:
#     print('positive')
# if no<0:
#     print('negative')
# if no ==0:
#     print('zero')


# 

# #WAP to accept a 3 paper marks and calculate total % and if % is greater than or equaal to 60 then he/she is eligible for placement

# paper1 = float(input("enter paper 1st marks out of 100: "))
# paper2 = float(input("enter paper 2nd marks out of 100: "))
# paper3 = float(input("enter paper 3rd  marks out of 100: "))
# totalmarks = paper1+paper2+paper3
# print("total marks = ", totalmarks)
# percentage = (totalmarks/3)
# print("percentage= ",percentage)
# if(percentage >= 60):
#     print("eligible")
# else:
#     print("non eligible")


#WAP to accpet 5 diff values in 5 difff variable and check maximum value and print by using simple if statement

a = int(input("enter 1st no: "))
b = int(input("enter 2nd no: "))
c = int(input("enter 3rd no: "))
d = int(input("enter 4th no: "))
e = int(input("enter 5th no: "))
        
if (a>b and a>c and a>d and a>e):
    print(a,"is greastest")
if (b>a and b>c and b>d and b>e):
    print(b,"is greastest")
if (c>a and c>b and c>d and c>e):
    print(c,"is greastest")
if (d>a and d>b and d>c and d>e):
    print(a,"is greastest")
if (e>a and e>b and e>c and e>d):
    print(e,"is greastest")