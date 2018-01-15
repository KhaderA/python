lst1=[10,"hi","20"]

print lst1

size=len(lst1)
#print size
i=0
while(i<size):
  print lst1[i]
  i=i+1

lst1.insert(0,30)
print lst1

lst1.insert(1,40)
print lst1

lst1.append(50)
print lst1

del lst1[1]
print lst1

lst1.pop(1)
print lst1

lst1.remove(50)
print lst1


