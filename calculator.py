print("WELCOME TO THE CALCULATOR")
print("ENTER VALUE OF 2 NUMBERS")
a=int(input())
b=int(input())
while True:
    print("ENTER 1 FOR ADDITION")
    print("ENTER 2 FOR SUBSTRACTION")
    print("ENTER 3 FOR MULTIPLICATION")
    print("ENTER 4 FOR DIVISION")
    print("ENTER 5 TO EXIT")
    print("ENTER YOUR CHOICE")
    ch=int(input())
    if ch==1:
        print("THE SUM IS",a+b)
    elif ch==2:
        print("THE SUBSTRACTION IS",a-b)
    elif ch==3:
        print("THE MULTIPLICATION IS",a*b)
    elif ch==4:
        print("THE DIVISION IS",a/b)
    elif ch==5:
        print("THANK YOU,QUITTING PROGRAM")
        break
    else:
        print("INVALID CHOICE")