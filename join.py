m_list=["k","a","r","a","m"," ","a","l","r","a","s","a","m"]
name="karam"
print("-".join(name))
print("".join(m_list))

def m_join(digram,sp:str):
  """It is in charge to conctenate the elements"""
  
  newDigram=""
  for i in range(1,len(digram)):
    newDigram+=sp+digram[i]
  return digram[0]+newDigram
print(m_join(name,"-"))
print(m_join(m_list,""))