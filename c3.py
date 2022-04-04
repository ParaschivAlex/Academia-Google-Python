def your_function(*args, **args2):
    s = 0
    for arg in args:
        if isinstance(arg, int):
            s += arg
    return s

print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))

def check_integer():
  nr = float(input())
  if int(nr) == nr:
    return nr
  return 0

check_integer()

def sum_0_n(n):
  if n == 0:
    return 0
  return sum_0_n(n-1) + n

def sum_even_0_n(n):
  if n == 0:
      return 0
  if n % 2 == 1:
      return 0 + sum_even_0_n(n-1)
  if n % 2 == 0:
      return n + sum_even_0_n(n-1)

def sum_odd_0_n(n):
  if n == 1:
      return 1
  if n % 2 == 1:
      return n + sum_odd_0_n(n-1)
  if n % 2 == 0:
      return 0 + sum_odd_0_n(n-1)


print(sum_0_n(4))
print(sum_even_0_n(3))
print(sum_even_0_n(4))
print(sum_odd_0_n(3))
print(sum_odd_0_n(4))