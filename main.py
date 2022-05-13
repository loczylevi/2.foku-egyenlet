def masodfoku(a,b,c):
  if b + (b **2 -4*a*c) < 0:
    return None
  else:
    minusz = -b - (b **2 -4*a*c) ** 0.5
    osztas = minusz / (2*a)
    plusz = -b + (b **2 -4*a*c) ** 0.5
    osztas2 = plusz / (2*a)
    return osztas, osztas2
p = masodfoku(7,8,9)
print(p)
z = masodfoku(2, -12, 10)
print(z)
  

