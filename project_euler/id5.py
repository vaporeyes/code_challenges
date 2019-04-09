# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

def sm(n):
  """
  smallest multiple
  """
  i = 1
  for k in range(1, n + 1):
    if i % k > 0:
      for j in range(1, n + 1):
        if (i * j) % k == 0:
          i *= j
          break
  
  return i


