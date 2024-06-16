class human:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def methods(self):
    print("NAME IS "+self.name)
h1=human("MANAS",19)
print(h1.name)
print(h1.age)
h1.methods()

# del h1