#153 =1+125+27=153
a=int(input("ENTER THE NUMBER"))
n=a
n1=a
rem=0
count=0
sum=0
while (n>0):
    rem=n%10
    count=count+1
    n=n//10
rem=0
while(n1>0):
 rem=n1%10
 sum=sum + int(pow(rem,count))
 n1=n1//10
if(a==sum):
   print("IT IS AN ARMSTRONG NUMBER")
else:
   print("IT IS NOT AN ARMSTRONG NUMBER")     

    
