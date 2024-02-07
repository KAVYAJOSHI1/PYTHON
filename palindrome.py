rem=0
rev=0
print("ENTER THE NUMBER")
n=int(input())
n1=n
while (n>0) :
   
    rem=n%10
    rev=rev*10+rem
    n=n//10

if(n1==rev): 
    print(str(n1) +" IS A PALINDROME NUMBER")   
else:
    print(str(n1) +" IS NOT A PALINDROME NUMBER")    