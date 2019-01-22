"""""
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'

"""
def non_start(a, b):
   x =len(a)
   y = len(b)
   if x>1 and y>1:
     a = a.replace(a[0],'',1)
     b = b.replace(b[0],'',1)
     return a+b
   elif x>1:
     return a.replace(a[0],'',1)
   elif y>1:
    return    b.replace(b[0],'',1)
   return ''
