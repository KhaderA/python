class A:
  def __init__(self):
    self.x=10
    self._y=20
    self.__z=30
  def fn1(self):
    print "ln fn1"
  def _fn2(self):
    print "ln _fn2"
  def __fn3(self):
    print "ln __fn3"

m=A()
print m.x
print m._y
#print m.__z
m.fn1()
m._fn2()
#m.__fn3()
