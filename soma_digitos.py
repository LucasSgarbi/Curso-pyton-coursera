n = input("Digite um número inteiro: ")
i=0
soma=0
x= len(n)
n= int(n)
while i<=x:
    soma=soma+n%10
    n=n//10
    i=i+1
print(soma)
