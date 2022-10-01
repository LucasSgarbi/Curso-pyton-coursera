l = int(input("digite a largura: "))
a = int(input("digite a altura: "))
i=0
j=0
while i<a:
  j=0
  while j<l:
    if j == 0 or j == (l-1) or i == 0 or i == (a-1):
      print("#", end="")
    else:
       print(" " , end="")
    j=j+1
  print("")
  i=i+1