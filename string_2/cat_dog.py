"""""
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

"""
def cat_dog(str):
  x = len(str)
  cat = 0
  dog = 0
  if x>1:
    for i in range(2,x):
      if (str[i]=='t' and str[i-1]=='a' and str[i-2]=='c') :
        cat = cat+1
      if (str[i]=='g' and str[i-1]=='o' and str[i-2]=='d') :
        dog = dog+1
    if dog ==cat:
      return True
    return False
    
  return True
    
