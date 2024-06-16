
def prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count=count+1
    print(count)        
    if count==0:
        print("NUMBER IS PRIME")
    else:
        print("NUMBER IS COMPOSITE")
print("ENTER THE NUMBER")
n=int(input())
prime(n)
