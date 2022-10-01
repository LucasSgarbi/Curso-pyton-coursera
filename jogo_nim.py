
def computador_escolhe_jogada(n , m):
  n=int(n)
  m=int(m)
  z = n%(m+1)
  if z == 0:
    if n<m:
      print( "O computador tirou " + str(n) + " peças")
      return(n)
      n=n-n
      print ("Agora restam "+ str(n) +" peças no tabuleiro.")
      
    else:
      print( "O computador tirou " + str(m) + " peças")
      n=n-m
      print ("Agora restam "+ str(n) +" peças no tabuleiro.")
      return(m)
  else:
    print( "O computador tirou " + str(z) + " peças")
    n=n-z
    print ("Agora restam "+ str(n) +" peças no tabuleiro.")
    return(z)

def usuario_escolhe_jogada(n,m):
  jc=0
  n=int(n)
  m=int(m)
  while jc == 0:
    a =int(input("Quantas peças você vai tirar?"))
    if a>n or a>m or a<=0:
      print("Oops! Jogada inválida! Tente de novo.")
    else:
      n=n-a
      print("Voce tirou "+ str(a) + " peças")
      print ("Agora restam "+ str(n) +" peças no tabuleiro.")
      jc=1
      return(a)
  
def partida():
  n=int(input("Quantas peças?"))
  m=int(input("Limite de peças por jogada?"))
  
  if n%(m+1)==0:
    print("Voce começa!")
    while n>0:
      x=usuario_escolhe_jogada(n,m)
      n=n-x
      if n==0:
        print("Fim do jogo! Você ganhou!")
        return(1)
      z=computador_escolhe_jogada(n , m)
      n=n-z
      if n==0:
        print("Fim do jogo! O computador ganhou!")
        return(2)
  else:
    print("Computador começa!")
    while n>0:
      z=computador_escolhe_jogada(n , m)
      n=n-z
      if n==0:
        print("Fim do jogo! O computador ganhou!")
        return(2)
      x=usuario_escolhe_jogada(n,m)
      n=n-x
      if n==0:
        print("Fim do jogo! Você ganhou!")
        return(1)
      


use = 0
pc=0
i=0
print("Bem-vindo ao jogo do NIM! Escolha:") 
print("1 - para jogar uma partida isolada")
camp = int(input("2 - para jogar um campeonato "))
if camp == 1:
  qg = partida()
  if qg==1:
    use=use+1
  if qg==2:
    pc=pc+1
  print("Placar: Você "+ str(use)  + " X " + str(pc) + " Computador")
else : 
  if camp==2:
    while i<3:
      qg = partida()
      if qg==1:
        use=use+1
        print("Placar: Você "+ str(use)  + " X " + str(pc) + " Computador")
      if qg==2:
        pc=pc+1
        print("Placar: Você "+ str(use)  + " X " + str(pc) + " Computador")
      i=i+1
