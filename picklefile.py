import pickle

a={'1':'a','2':'b'}
pickle_file=open("pocklefile.txt","wb")
pickle.dump(a,pickle_file)
pickle_file=open("pocklefile.txt","rb")
new_a=pickle.load(pickle_file)
print(new_a)