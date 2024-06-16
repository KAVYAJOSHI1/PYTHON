print("ENTER THE NUMBER")
a=int(input())
n=a
rev=0
rem=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10

if(rev==a):
    print("MAGIC NUMBER")
else:
    print("NOT MAGIC")
 