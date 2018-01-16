import math


def f_add(a,b):
  """Performs addition of given numbers"""
  try:
    c=a+b
  except TypeError:
    print "/!\\ Type Error: Enter integer values /!\\"
  else:
    return c


def f_sub(a,b):
  """Performs subtraction of given numbers"""
  try:
    c=a-b
  except TypeError:
    print "/!\\ Type Error: Enter integer values /!\\"
  else:
   return c


def f_mul(a,b):
  """Performs multiplication of given numbers"""
  c=a*b
  return c


def f_div(a,b):
  """Performs division of given numbers"""
  try:
    c=a/b
  except ZeroDivisionError:
    print "/!\\ Divide By Zero Occurred /!\\"
  else:
    return c

def f_sin(a):
  "Performs sin operation on the given number"
  try:
    x=math.sin(math.radians(a))
  except TypeError:
    print "/!\\ Type Error: Enter a float value /!\\"
  else:
    return x

def f_cos(a):
  "Performs cos operation on the given number"
  try:
    x=math.cos(math.radians(a))
  except TypeError:
    print "/!\\ Type Error: Enter a float value /!\\"
  else:
    return x

def f_pow(a,b):
  "Performs power operation on the given number"
  x=math.pow(a,b)
  return x

def f_sqrt(a):
  "Performs square-root operation on the given number"
  x=math.sqrt(a)
  return x

