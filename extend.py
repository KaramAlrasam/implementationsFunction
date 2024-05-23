def m_extend(a_list:list, b_list:list)->list:
  """It is in charge to conctenate two list togather"""
  res=a_list+b_list
  return res
a=["karam"," ","Alrasam"]
b=[" ","Loves"," ","painting"]
print(m_extend(a,b))
cars = ["Audi","BMW","Jaguar"]
other_cars = ["Maruti", "Tata"]
a.extend(b)
print(a)