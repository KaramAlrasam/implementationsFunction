a=[1,2,3,4,5,6,7,8,9]
def BinnarySearch(a_list,item):
  """It is in charge to get the item quickly"""
  #make start_poin its value zero and end_point its value the length of the list
  start_point,end_point=0,len(a_list)
  #divide the list into half
  
  #make while loop to search for the item 
  while start_point<end_point:#[1,2,3,4,5,6,7,8,9]
    mid=(start_point+end_point)//2
    if a_list[mid]>item:
      end_point=mid
    elif a_list[mid]<item:
      start_point=mid+1
    else:
      return mid
  return None
                                 #0       #9
def BinnarySearch2(a_list,item, start_p, end_p):#item=7
       #1- mid=5
       #2- mid=6
  mid=(start_p+end_p)//2
    #a_list[mid]=6<  item=7
  if a_list[mid]<item:               #start_p=mid+1=6
     return BinnarySearch2(a_list, item, mid+1, end_p=end_p)
  elif a_list[mid]>item:
     return BinnarySearch2(a_list, item, start_p, end_p=mid)
  else:
     #a_list[mid]=7==item=7
     return mid

print(BinnarySearch2(a,7,0,len(a)))
print(BinnarySearch(a,7))
    