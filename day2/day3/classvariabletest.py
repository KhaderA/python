class Employee:
    empcount=0 #class attribute
    def __init__(self,sal):
        Employee.empcount+=1
        self.sal=sal
    def __del__(self):
        Employee.empcount-=1
    def displaycount(self):
        return Employee.empcount
    def displaysal(self):
        return self.sal
    #@staticmethod
    #def displaycount():
    #   return Employee.empcount

emp1=Employee(1000)
print emp1.displaycount()
print emp1.displaysal()
emp2=Employee(2000)
print emp2.displaycount()
print emp2.displaysal()
print "deleting emp2"
del emp2
print Employee.empcount

    
