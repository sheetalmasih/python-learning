def lcm(a, b):
  t = a % b
  if t == 0:
        return a
  return a * lcm(b, t) // t
print(lcm(2, 5))