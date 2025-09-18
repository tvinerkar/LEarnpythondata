# list = []
# tuple=()

a = (12,10,10,4,8,9,0)
# slicing
print(a[::-1])

print("jGAskbcnllanclkanslcma"[::-1])

b = (12, 10, 10, 4, 8, 9, 0)

# Convert to list and sort
sorted_list = sorted(b)
print(sorted_list)   # [0, 4, 8, 9, 10, 10, 12]

# Convert back to tuple
sorted_tuple = tuple(sorted_list)
print(sorted_tuple)  # (0, 4, 8, 9, 10, 10, 12)

d= (10,20,30,80,100,5)
e = list(d)
f = sorted(e)
g = sorted(e, reverse=True)

print(f)
print(g)
print(tuple(f))
print(tuple(g))