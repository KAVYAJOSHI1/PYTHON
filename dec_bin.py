print("ENTER THE NUMBER")
n=int(input())
rem=0
rev=0
bin=0
base=1
while n>0 :
    rem=n%2
    bin=bin+rem*base
    base=base*10
    n=n//2

print("BINARY IS "+str(bin))    
