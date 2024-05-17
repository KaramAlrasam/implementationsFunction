def remove_duplcate(m_list:list)->list:
  res=[]
  for item in m_list:
    if item not in res:
      res.append(item)
  print(res)
  return set(m_list)
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(remove_duplcate(a))#{40, 10, 80, 50, 20, 60, 30} 