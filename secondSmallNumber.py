def secondSmallNumber(m_list:list)->int:
  #check the length of the list if it is lesser than 2 get out of the function
  if (len(m_list)<2 )or(len(m_list)==2 and m_list[0]==m_list[1]):
    return
  #make condition if the length of the list == 2 and to items in it resemblence
  # get out of the function
  else: 
    uniqueItems=list(set(m_list))
    
    return sorted(uniqueItems)[1]
print(secondSmallNumber([1, 2, -8, -2, 0, -2]))#-2
print(secondSmallNumber([1, 1, 0, 0, 2, -2, -2]))#0
print(secondSmallNumber([1, 1, 1, 0, 0, 0, 2, -2, -2]))#0
print(secondSmallNumber([2, 2]))#None
print(secondSmallNumber([2]))#None