a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [2, 4]
def isSubListExist(main_l, sub_l)->bool:
  """It checks if the sub_list is existent in the main_list"""
  #first you ned to know the length of the list
  if len(sub_l)>len(main_l) or len(sub_l)<=0:
    raise ValueError (f"{sub_l} must be its length lesser than main list")
  else:
    return (" ".join(map(str,sub_l)) in " ".join(map(str,main_l)))
original_list = [1, 2, 3, 4, 5, 6]
sublist = [3, 4, 5]
# print(isSubListExist(original_list, sublist))
print(isSubListExist(a,b))
print(isSubListExist(a,c))
print("-"*30)

def isSubListExist2(main_l, sub_l)->bool:
  """It checks if the sub_list is existent in the main_list"""
  #first you ned to know the length of the list
  if len(sub_l)>len(main_l) or len(sub_l)<=0:
    raise ValueError (f"{sub_l} must be its length lesser than main list")
  else:
    for i in range(0,len(main_l)):
      if sub_l == main_l[i:len(sub_l)+i]:
        return True
    return False
# print(isSubListExist2(original_list,sublist))
print(isSubListExist2(a,b))
print(isSubListExist2(a,c))