list=[]
print("ENTER THE SIZE OF THE LIST:")
n=int(input())
print("ENTER THE ELEMENTS:")
for i in range(0,n):
    list.append(input())
print(list)  
max=list[0]
for i in range(0,n):
    if(list[i]>max):
        max=list[i]
print("THE MAXIMUM ELEMENT IS "+ str(max))
      
 
