def subsetTerbesar(inputList):
  subset_list = [[]]
  if sum(inputList) + abs(sum(inputList)) == 0:
    return 0
  
  for i in inputList:
    subset_list += [temp_list + [i] for temp_list in subset_list]
  
  length_subset = len(subset_list)
  i = 0

  while i < length_subset:
    if len(subset_list[i]) > 1:
      for j in range(1, len(subset_list[i])):
        if abs(inputList.index(subset_list[i][j]) - inputList.index(subset_list[i][j - 1])) == 1:
          subset_list.pop(i)
          length_subset -= 1
          i -= 1
          break
        continue
    i += 1
  
  output = 0
  for i in subset_list:
    if output < sum(i) : output = sum(i)

  return output