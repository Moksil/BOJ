from functools import reduce


lst = [1]

out = reduce(lambda x, y : x + y, lst)

print(out)