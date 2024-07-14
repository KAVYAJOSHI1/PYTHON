#program to find first non repeating element in the string using function
def non(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in s:
        if d[i]==1:
            return i
s=input("ENTER THE STRING\n")
print("THE FIRST NON REPEATING ELEMENT IN THE STRING IS",non(s))