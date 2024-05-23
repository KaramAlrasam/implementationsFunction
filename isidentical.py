def isidentical(a_list:list, b_list:list)->bool:
  """It is in charge to return True if the two lists are identical
  ans vice versa"""
  return " ".join(map(str,a_list))in " ".join(map(str,b_list*2))
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]#10 10 10 0 0 10 10 10 0 0
list3 = [1, 10, 10, 0, 0]
print(isidentical(list1,list2))
print(isidentical(list1,list3))
