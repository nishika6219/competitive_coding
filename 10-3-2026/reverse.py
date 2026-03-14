num = 123
print(num)
a =num%10  #3
num= num//10 #num = 12
b= num%10 #b=12
c=num //10  #num=1

rev = a*100 +b *10 +c*1 #300+20+1 =321
print(rev)




num = 1234567
print(num)

a = num % 10      # 7
num = num // 10   # 123456

b = num % 10      # 6
c = num % 10      # 5
d = num % 10      # 4
e = num % 10      # 3
f = num % 10      # 2
g = num % 10      # 1


rev = a*1000000 + b*100000 + c*10000 + d*1000 + e*100 + f*10 +g*1
print(rev)