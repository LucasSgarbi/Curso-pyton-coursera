import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    as_b = [wal, ttr, hlr, sal, sac, pal]
    return as_b

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    
    i=0
    as_cmp = 0
    while i<6:
      as_cmp = as_cmp + abs(as_a[i]-as_b[i]) 
      i=i+1

    as_cmp = as_cmp / 6
    
    return as_cmp 



def calcula_assinatura(texto):
    sents = separa_sentencas(texto)
    frases = []
    palavras = []
    tam_med = 0
    tam_med_sent = 0
    r_hapax = 0
    s_sents = 0
    Compx = 0
    r_type_token  = 0
    s_palav = 0
    t_med_fras = 0
    t_let_fras = 0
    f=0
    p=0

    
    for sentenca in sents:      
        s_sents = s_sents + len(sentenca)        
        l_fras = separa_frases(sentenca)

        while f < len(l_fras):
            frases.append(l_fras[f])
            f=f+1

    for fras in frases:
        t_let_fras = t_let_fras + len(fras)
        l_palav = separa_palavras(fras)

        while p < len(l_palav) :
            palavras.append(l_palav[p]) 
            p=p+1   
    
    for palavra in palavras:
        s_palav = s_palav + len(palavra)
    
    tam_med = s_palav/len(palavras)
    r_type_token = n_palavras_diferentes(palavras)/len(palavras)
    r_hapax = n_palavras_unicas(palavras)/len(palavras)
    tam_med_sent = s_sents / len(sents)
    Compx = len(frases) / len(sents)
    t_med_fras = t_let_fras / len(frases)
    as_a = [tam_med ,  r_type_token ,r_hapax, tam_med_sent , Compx , t_med_fras]
    return as_a

def avalia_textos(textos, ass_cp):
  ass=0
  l_ass=[]
  i =0
  
  
  while i < len(textos):
    ass= calcula_assinatura(textos[i])
    l_ass.append(ass)
    i=i+1

  j=0
  menor = l_ass[0]
  loc_men = 0  

  while j<len(l_ass):
    if menor > l_ass[j] :
       menor = l_ass[j]
       loc_men = j   
    j=j+1  
  return loc_men + 1


ass = le_assinatura()
textos= le_textos()
copiao = avalia_textos(textos, ass)
copiao = str(copiao)
print ("O autor do texto " + copiao +  " está infectado com COH-PIAH")
    
