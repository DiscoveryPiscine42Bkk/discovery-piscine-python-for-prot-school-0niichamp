x = int(input("Enter the first number: ")).__int__()
y = int(input("Enter the secord number: ")).__int__()
z = x * y

if z < 0 :
    print(f"{x} x {y} = {z}")
    print("This number is negative.")
elif z > 0 :
    print(f"{x} x {y} = {z}")
    print("This number is positive.")
else :
    print(f"{x} x {y} = {z}")
    print("This number is both positive and negative.")