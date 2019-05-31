def fizzbuzz(n):
    if n % 15 == 0:
      return 'Fizzbuzz'
    elif n % 3 == 0:
      return 'Fizz'
    elif n % 5 == 0:
      return 'buzz'
    else:
      return n

for n in range(1, 101):
  print(fizzbuzz(n))
