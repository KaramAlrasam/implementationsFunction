import itertools
shallowList=[[1,2,3],[4],[5,6,7],[8,9,10,11,12]]
def flattingList(m_list:list):
  """It is in charge to convert shallow list into flatting list """
  res=[]
  for row in m_list:
    for item in row:
      res.append(item)
  return res
print(flattingList(shallowList))

print(list(itertools.chain(*shallowList)))