#nested loop
#end=" " is use for space between elements

for i in range(1,4):  #outer loop =>rows
    for j in range(1,4):  #inner loop =>columns
        print(i,end=" ") #end=" " is use for space between elements
    print( )



#--------------
#   1 2 3
# 1
# 2
# 3
# (i,j=(1,1)) --> (1,2)  ---> (1,3) => 1 1 1
# (i,j=(2,1)) --> (2,2) --> (2,3) => 2 2 2
# (i,j=(3,1)) --> (3,2) -->( 3,3) => 3 3 3


