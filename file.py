"""import os
f=open("file.txt","a")
f.write("\nADDITION DONE")
f.close()
f=open("file.txt","r")

print(f.read())
if os.path.exists("newfile.txt"):

  os.remove("newfile.txt")
else:
  print("THE FILE DOES NOT EXIST")"""
f=open("file.txt","w")
f.write("NEW LINE")

f.close()
f=open("file.txt","r")
print(f.read())