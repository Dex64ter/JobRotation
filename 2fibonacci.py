
def fiboSequence(number):
  fibonacci = [0, 1]
  while fibonacci[-1] < number:
    fibonacci.append((fibonacci[-1]+fibonacci[-2]))

  if fibonacci[-1] == number: 
    return True
  else:
    return False

print(fiboSequence(255))