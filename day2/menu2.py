#add comment lines here
print "CALCULATOR"
#add comment lines here

import ops
import os
import sys

def f_main():
  #os.system("cls")
  print "#".center(60,"#")
  print "CALCULATOR".center(60,"#")
  print "#".center(60,"#")
  print "1. simple calc"
  print "2. sci calc"
  print "3. exit"
  choice=input("Enter your choice ")
  if(choice==1):
    f_simcal()
  elif(choice==2):
    f_scical()
  elif(choice==3):
    sys.exit()
  else:
    print "Wrong Input"
    print ""
    f_main()
    
def f_simcal():
  """Implements Simple calculator"""
  os.system("cls")
  print "SIMPLE CALCULATOR"
  print "1.add"
  print "2.sub"
  print "3.mul"
  print "4.div"
  print "5.goback"
  choice=input("Enter your choice of operation: ")

  if(choice==1):
    f1=open("input.txt","r")
    list1=f1.readlines()
    #a=
    #b=
    #value=ops.f_add(a,b)
    #if(value!=None):
       #print "The addition value is: ",value
    print list1
  elif(choice==2):
    a=input("Enter value of a:")
    b=input("Enter value of b:")
    value=ops.f_sub(a,b)
    if(value!=None):
      print "The subtraction value is: ",value
  elif(choice==3):
    a=input("Enter value of a:")
    b=input("Enter value of b:")
    value=ops.f_mul(a,b)
    if(value!=None):
      print "The multiplication value is: ",value
  elif(choice==4):
    a=input("Enter value of a:")
    b=input("Enter value of b:")
    value=ops.f_div(a,b)
    if(value!=None):
      print "The division value is: ",value
  elif(choice==5):      
    f_main()
  else:
    print "wrong choice"
    f_simcal()
  print ""
  f_main()

def f_scical():
  #os.system("cls")
  print "Scientific Calculator"
  print "1.sin"
  print "2.cos"
  print "3.power of"
  print "4.square root"
  print "5.go back"
  choice=input("Enter your choice of operation: ")
  if(choice==1):
    a=input("Give the input for sine operation: ")
    value=ops.f_sin(a)
    if(value!=None):
      print "The sin value of given input is: ",value
  elif(choice==2):
    a=input("Give the input for cosine operation: ")
    value=ops.f_cos(a)
    if(value!=None):
      print "The cos value of given input is: ",value
  elif(choice==3):
    a=input("Input the number to perform power operation: ")
    b=input("Input the frequency of power operation: ")
    value=ops.f_pow(a,b)
    print "The power of value of given input is: ",value
  elif(choice==4):
    a=input("Input the value to perform square root operation: ")
    value=ops.f_sqrt(a)    
    print "The square-root value of given input is: ",value
  elif(choice==5):
    f_main()
  else:    
    print "Wrong value"
    f_scical()
  f_scical()

os.system("cls")  
f_main()


