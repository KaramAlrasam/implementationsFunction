def test(text:str)->str:
  """It is in charge to find the index for each chr in input"""
  #make empty string variable
  res=""
  #make for loop on the text and use function chr() to get ASCII index
  for l in text.lower():
    if l.isalpha():
      res+=str(ord(l)-96)+" "
  return res
print(test("Python"))
print(test("Java"))
print(test("Python Tutorial"))# "16 25 20 8 15 14 20 21 20 15 18 9 1 12"