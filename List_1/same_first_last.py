"""""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True

"""

def same_first_last(nums):
  a = len(nums)
  if a>=1:
    if a==1:
      return True
    if nums[0]==nums[a-1]:
      return True
  return False
