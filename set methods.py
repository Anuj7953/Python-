s= {1,3,4,6,8,9, "Anuj"}

print(s, type(s))  # Output: <class 'set'>

s.add(45)
print(s)  # Output: {1, 3, 4, 6, 8, 9, 'Anuj', 45}

s.remove(3)  # removes 3 from the set
print(s)  # Output: {1, 4, 6, 8, 9, 'Anuj', 45}

s.pop()  # removes and returns an arbitrary element from the set
print(s)  # Output: {4, 6, 8, 9, 'Anuj', 45}

p = {23,56,34,78,6, "Anuj"}

print(s.union(p))  # combines elements from both sets, removing duplicates
print(s.intersection(p))  # finds common elements in both sets