def m_index(iterEl, item,num=None)->int:
  """return integer index"""
  tottal_indexes=[]
  if item not in  iterEl:
    raise ValueError(f"{item} is not exist")
  for x,i in enumerate(iterEl):
    if num==None and i==item:
      return x
    elif num!=None and num>0 and i==item:
      tottal_indexes.append(x)
      if num==len(tottal_indexes):
        break  
  return tottal_indexes
digram=["k","a","r","a","m","a"]
print(m_index(digram,"a",2))