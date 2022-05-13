def masodfoku(a,b,c):
  
  minusz = -b - (b **2 -4*a*c) ** 0.5
  osztas = minusz / (2*a)
  
  plusz = -b + (b **2 -4*a*c) ** 0.5
  osztas2 = plusz / (2*a)
  if osztas or osztas2 < 0:
    return None
  elif osztas or osztas2 > 0:
    return osztas, osztas2
  
p = masodfoku(7,8,9)
print(p)
  

