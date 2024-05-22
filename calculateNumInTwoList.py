a=[1,2,3,4,5,6,7,8,9]
b=[1,2,3,4,5,6,7,8,10]

def calculate_unique_numbers( a_list:list, b_list:list)->int:
  """return the calculation difference between the two lists."""
  #get rid of the commen items first
  commen_num=[num for num in a_list if num in b_list]
  total=a_list+b_list
  res=0
  for num in total:
    if num not in commen_num:
      res+=num
  return res

print(calculate_unique_numbers(a,b))

def calculate_unique_numbers2(a_list:list, b_list:list)->int:
  """return the calculation difference between the two lists."""
  a=set(a_list)
  b=set(b_list)
  unique=list(a-b)
  unique2=list(b-a)
  return sum(unique+unique2)
print(calculate_unique_numbers2(a,b))