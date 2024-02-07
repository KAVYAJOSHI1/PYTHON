rem=rev=0
n=int(input("ENTER THE NUMBER"))
while n>0 :
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(str(rev)+"IS THE REVERSED NUMBER")
