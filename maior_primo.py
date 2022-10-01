def maior_primo(x):
  primo=0
  while primo!=1:
    primo=0
    i=1
    while i<x:
      if x%i==0:
        primo=primo+1
      i=i+1
    
    if primo!=1: 
     x=x-1  
  return x 

x = int(input("Digite um numero inteiro"))   
maior_primo(x)
