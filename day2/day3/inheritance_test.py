##Multilevel inheritance
class a():
    def __init__(self,i):
      self.i=i
    def fn1(self):
      print "fn1 from class a",id(self)

class b():
    def __init__(self,j):
      self.j=j
    def fn2(self):
      print "fn2 from class b",id(self)

class c(a,b):
    def __init__(self,i,j,k):
      a.__init__(self,i)
      b.__init__(self,j)
      self.k=k
    def fn3(self):
      print "fn3 from class c",id(self)


#a1=a(20)
#print a1.i
#a1.fn1()

#b1=b(10)
#print b1.j
#b1.fn2()

c1=c(10,20,30)
print c1.i
print c1.j
print c1.k
c1.fn1()
c1.fn2()
c1.fn3()
