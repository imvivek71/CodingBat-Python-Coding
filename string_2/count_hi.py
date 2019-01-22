"""""
Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

"""

def count_hi(str):
  x = len(str)
  count = 0
  if x>1:
    for i in range(1,x):
      if (str[i]=='i' and str[i-1]=='h') :
        count = count+1
      
    return count
  return count
