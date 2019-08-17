# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def lpp(n):
  """
  set n to the number of digits
  """
  l = []
  m = int(str(1) + ((n - 1) * str(0)))
  n = int(n * str(9))
  print(m, n)
  for i in range(m, n):
    for j in range(m, n):
      k = i * j
      if str(k)[::1] == str(k)[::-1]:
        l.append(k)
  return l
