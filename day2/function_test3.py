def test11(*pos,**kwd):
  print "positional",pos
  print "keyword",kwd
test11(10,20,a=30,b=40)
test11(50,70)
test11(a=70,b=90)
test11()
