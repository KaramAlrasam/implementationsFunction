from itertools import combinations
def generateSubLists(m_list)->list:
  """It generates whole posiables sublist from the main list"""
  #we make empty list to save whole subLists in it 
  subLists=[]
  #make for loop and get numbers from the range between zero and
  #the number of the length of the list
  for i in range(0,len(m_list)+1):
    #use list comprehantion to save the sublist
    sub=[list(x) for x in combinations(m_list,i)]
    if len(sub)>0:
      subLists.extend(sub)
  return subLists
a=["x","y","z"]
print(generateSubLists(a))