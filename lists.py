# Lists

# demo_list
demo_list = [1, "helo", True, False, [1, 2, 3, 4]]
print(demo_list)

# range
r = list(range(1, 25))
# print(r)

# for item in r: 
#   print(item + 25)

# colors
colors = ['red', 'green', 'blue']

# colors.append('yellow')
# colors.insert(1, 'orange')
# colors.remove('blue')
# colors.pop(0)
# colors.reverse()
# colors.sort()

print(len(colors))
# print(dir(colors))
colors.append('crimson')
print(len(colors))
print(sorted(colors))
colors.extend(['red', 'orange'])
colors.extend(['violet', 'white', 'black'])

print(colors)
colors.pop(0)
print(colors)
print(colors.index('violet'))
colors.remove('red')
colors.remove('green')
colors.remove('blue')
print(colors)
