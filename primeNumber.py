import math,time
def test(m_list:list):
  return all(check_prime_Number(i)for i in m_list)

def check_prime_Number(num:int)->bool:
  """It is in charge to return boolean True if 
  the elementes are prime numbers and vice versa"""
  if num<2:
    return False
  else:
    for x in range(2,num):
      if num%x==0:
        return False
    return True
 
# digram=[1,2,3,4,5,6,7,8,9]
# print(test(digram))
start=time.time()
for i in range(25):
  print(i," ->",check_prime_Number(i))
print(time.time()-start)
print("="*30)


def check_prime_Number2(num:int)->bool:
  """It is in charge to return boolean True if 
  the elementes are prime numbers and vice versa"""
  if num==1:
    return False
  else:
    floor=math.floor(math.sqrt(num))
    for x in range(2,1+floor):
      if num%x==0:
        return False
    return True
start=time.time()
for i in range(25):
    print(i," ->",check_prime_Number2(i))
print(time.time()-start)



print("="*20)
def check_prime_Number3(num:int)->bool:
  """It is in charge to return boolean True if 
  the elementes are prime numbers and vice versa"""
  #first make condition to discove if the num ==1 return False
  #second condition to discover if the num belong to even number to return False
  if num==1 or (num!=2 and num%2==0):
    return False
  #make condition if the number == 2 which means it's prime number
  elif num==2:
    return True
  else:
    #use math.squt()to get squier integer  biggest number to reduce the operations of division
    max_squerNum=math.floor(math.sqrt(num))
    #now make the search on the prime numbers only for odd numbers
    #because we made condition allready
    for x in range(3,max_squerNum+1,2):
      if num%x==0:
        return False
    return True
start=time.time()
for i in range(25):
   print(i," ->",check_prime_Number3(i))
print(time.time()-start)
 