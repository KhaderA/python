##Here the dictionary's values are updated in the original copy
##as dictionary is a mutable object. This is as per the python rule for mutable objects
dct1={10:20,"Sachin":99}
print dct1
def dcttest(dct2):
  dct2[10]=50
  dct2["Sachin"]+=3
  print dct2
dcttest(dct1)
print dct1


