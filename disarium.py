print("ENTER THE NUMBER")
a=int(input())
n1=a
n=a
sum=0
count=0
while(n1>0):
    
    count=count+1
    n1=n1//10
while(n>0):
    rem=n%10
    sum=sum+pow(rem,count)
    count=count-1
    n=n//10    
if(sum==a):
    print("ITS A DISARIUM NUMBER")
else:
    print("ITS NOT A DISARIUM NUMBER")
     