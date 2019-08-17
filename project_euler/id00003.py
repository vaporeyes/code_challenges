# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

def lpf(n):
  """
  print largest prime factor
  """
  p = 2
  while n >= p * p:
    if n % p == 0:
      n = n // p
    else:
      p += 1
  
  return n
  