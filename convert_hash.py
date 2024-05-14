def convert_hash(str1:str):
  #use split function to get list
  m_list=str1.split(" ")
  #use for loop and make condition for each length word which is greader or equil
  #to five
  for i in range(len(m_list)) :
    if len(m_list[i])>=5:
      m_list[i]=len(m_list[i])*"#"
  return " ".join(m_list)
print(convert_hash("Python - Remove punctuations from a string"))
print(convert_hash("Count the lowercase letters in the said list of words"))
