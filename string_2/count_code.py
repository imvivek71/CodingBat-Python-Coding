"""""
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

"""
def count_code(str):
  x = len(str)
  count = 0
  if x>3:
    for i in range(3,x):
        if (str[i]=='e' and str[i-2]=='o' and str[i-3]=='c') :
          count +=1
    return count
  return count
