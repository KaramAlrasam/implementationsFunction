def getUniqueItem(m_list:list)->list:
  """It is in charge to get unique item from the list"""
  #make for loop ans make condition to get know which item is unique
  unique_items=[]
  for item in m_list:
    if m_list.count(item)==1:
      unique_items.append(item)
  return unique_items

a=[1,1,2,2,3,3,4,45]
print(getUniqueItem(a))