print("ENTER THE STRING:")
a=str(input())
l=len(a)
temp="AEIOUaeiou"
print("VOWELS ARE:")
for i in range(l):
    if a[i] in temp:

      print(a[i])
print("CONSONANTS ARE:")      
for i in range(l):
    if a[i] not in temp:

      print(a[i])