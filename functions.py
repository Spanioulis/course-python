def helloWorld(message):
  print(message, "Soy Sergio")

helloWorld("Hola Mundo!")

def sum(a, b):
  if a > b:
    return a - b
  else:
    return b - a

a = 10
b = 20
print(sum(a, b))

add = lambda num1, num2: num1 + num2

print(add(66, 88))