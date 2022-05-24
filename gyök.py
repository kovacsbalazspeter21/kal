def masodfoku(a, b, c):
  if (b**2 - 4*a*c) ** 0.5 >= 0:
    x1 = -b + (b**2 -4*a*c)**0.5 / 2*a
    x2 = -b - (b**2 -4*a*c)**0.5 / 2*a
    return x1, x2
print(masodfoku(2, -12, 10))