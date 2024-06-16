def fib(n):
   a=0
   b=1
   c=0
   
   while(c<=n):
    print(c) 
    a=b
    b=c
    c=a+b
    
print("ENTER THE NUMBER")
n=int(input())
fib(n)