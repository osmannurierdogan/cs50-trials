import functions

base = int(input("x: "))
top = int(input("y: "))

print(f"{base}^{top} = ", functions.square(base,top))

for i in range(11):
    print(f"The square of {i} is {functions.getSquare(i)}")