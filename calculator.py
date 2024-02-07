ch=0
a=int(input("ENTER VALUE OF A"))
b=int(input("ENTER VALUE OF B"))
print("ENTER 1 FOR ADDITION")
print("ENTER 2 FOR SUBSTRACTION")
print("ENTER 3 FOR MULTIPLICATION")
print("ENTER 4 FOR DIVISION")
ch=int(input())

if ch==1 :

    sum=0
    sum=a+b
    print("SUM OF "+str(a)+"AND "+str(b)+"IS "+str(sum))

elif ch==2 :

    sub=a-b
    print(str(sub))

elif ch==3 :

    mul=a*b
    print(str(mul))
    
elif ch==4 :

    div=a/b
    print(str(div))

else:
    
    print("ENTER FROM 1 TO 4")
