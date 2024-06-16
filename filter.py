#runs a function in a collection but only stores true values
age=[1,2,3,4,5,6]
def adult(x):
    if x>2 :
        return True
    else:
        return False
#adult=list(filter(adult,age))
adult=list(filter(lambda x:x>2,age))
print(adult)