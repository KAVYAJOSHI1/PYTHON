def pal(s: str )-> bool:
    s=s.replace(" ","")
    return s == s[::-1]
s=input("ENTER THE STRING\n")
if pal(s) == True:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
