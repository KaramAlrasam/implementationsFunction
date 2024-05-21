
digram="The quick brown fox".split(" ")
m_sorted=sorted(digram,key=len)
res=[m_sorted[-1],]
for i in range(2,len(m_sorted)):
  if len(m_sorted[-i])==len(m_sorted[-1]):
    res.append(m_sorted[-i])
  else:
    break
print(res)