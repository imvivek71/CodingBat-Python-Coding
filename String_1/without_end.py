"""""
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'

"""
def without_end(str):
  x = len(str)
  if x>1:
    return (str[1:x-1])
  return str
