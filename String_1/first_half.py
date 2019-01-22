"""""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

"""
def first_half(str):
  strlen = len(str)
  if strlen>1:
    x = int(strlen/2)
    str = str[0:x]
    return str
  return str
