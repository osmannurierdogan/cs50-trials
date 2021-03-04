# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4)
s.add(5)
s.add(6)
s.add(6)
print(s)
print(f"The set has {len(s)} elements.")

# You can not write the particular element more than one.
s.remove(4)
print(s)

print(f"The set has {len(s)} elements.")