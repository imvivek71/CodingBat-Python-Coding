"""""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. 
Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True

"""
def common_end(a, b):
  x = len(a)
  y = len(b)
  if x>0 and y>0:
    if a[0]==b[0]:
      return True
    elif x>1 and y>1:
      if a[x-1]==b[y-1]:
        return True
    else:
      return False
    
  return False
