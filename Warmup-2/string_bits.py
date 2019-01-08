""""""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

"""
def string_bits(str):
  result = ""
  n = len(str)
  if n<2:
    return str
  else:
    z =0
    for i in range(0,n,2):
      result +=str[i]
    return result
