from string import punctuation
#"john@example.com"
def corp_name(str1:str)->str:
  """It is in charge to corp the name from the email"""
  #make condition if the email doesn't have @ raise error
  if "@" not in str1:
    raise ValueError ("The email is missed @")
  index=str1.index("@")
  name=str1[:index]
  for s in punctuation:
    name=name.replace(s,"")
  return name
print("-> ",corp_name("john@example.com"))
print("-> ",corp_name("john.smith@example.com"))
print("-> ",corp_name("fully-qualified-domain@example.com"))
print("="*20)
########################################
def corp_name2(email:str)->str:
  """It is in charge to corp the name from the email"""
  if "@"not in email:
    raise ValueError ("It is missed @ in the email")
  index=email.index("@")
  return "".join(l for l in email[0:index] if l.isalpha())
print("-> ",corp_name2("john@example.com"))
print("-> ",corp_name2("john.smith@example.com"))
print("-> ",corp_name2("fully-qualified-domain@example.com"))