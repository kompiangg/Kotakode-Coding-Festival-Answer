def cariPasangan(inputList,inputInt):
  inputList.sort()
  output = []
  if len(inputList) < 2 : return False
  for i in range(len(inputList)):
    for j in range(i, len(inputList)):
      if i == j: continue
      elif inputList[i] + inputList[j] == inputInt:
        output += [[inputList[i],inputList[j]]]
  return output