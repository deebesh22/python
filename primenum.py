num=int(input("enter the num:"))
c=0
for i in range(2,num):
   if(num/i==0):
     c=c+1
if(c>=0):
  print("the num is prime")
else:
  print("the num is not prime")
