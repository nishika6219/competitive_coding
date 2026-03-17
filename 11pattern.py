n = int(input("Enter number of rows: "))

for i in range(1, n+1): # rows
    for j in range(1, n+1): #col
        print(chr(64 + j), end=" ")
    print()

#(i,j=(1,1))=> 64+1=65=A  --> (1,2)=>64+2=66=B --> (1,3)=> 64+3=67=C  --> (1,4)=> 64+4=68=D  inner loop ends
#(i,j=(2,1))=> 64+1=65=A  --> (2,2)=>64+2=66=B --> (2,3)=> 64+3=67=C --> (2,4)=> 64+4=68=D inner loop ends
#and continue
# A B C D 
# A B C D
# A B C D
# A B C D

print("---------------")
n = int(input(" enter the no of rows: "))
for i in range(1,n+1): #rows
    for j in range(1,n+1): #col
        print(n+1-i, end=" ")
    print()
# 4 4 4 4 
# 3 3 3 3
# 2 2 2 2
# 1 1 1 1


print("---------")
n = int(input(" enter the no of rows: "))
for i in range(1,n+1): #rows
    for j in range(1,n+2-i): #col
        print("*", end=" ")
    print()

