def remove_repetidos(ab):
  ab.sort()
  i=0
  j=1
  ac=[]
  while i<len(ab):
    if (j+1 > len(ab)):
      break
    else: 
      if(ab[i]==ab[j]):
        del ab[i] 
      else:
        ac.append(ab[i])
        i=i+1
        j=i+1

  ac.append(ab[len(ab)-1])
  return ac  