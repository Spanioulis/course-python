# Tuples
# Valor inmutable, no soporta reasigación de valores

x = (1, 2, 3)
y = ("hello", "world")

# print(x)
# print(x[2])
# print(y)

#? Importante diferenciar una tupla y un integer añadiendo esa coma, aunque sea únicamente un elemento
tup = (1,)
no_tup = (1)

print(tup)
print(type(tup))
print(no_tup)
print(type(no_tup))

# Uso: por ejemplo en localizaciones
locations = {
  (35.324, 40.534): "Madrid",
  (37.775, -122.418): "San Francisco",
  (40.714, -74.006): "New York"
}
print(locations)