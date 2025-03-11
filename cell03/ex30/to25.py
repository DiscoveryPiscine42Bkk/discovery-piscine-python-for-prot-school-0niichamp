x = int(input("Enter a number less than 25 : ")).__int__()
y = 25

if x < y :
    i = x
    while i < 26:
        print(f"Inside the loop, my variable is {i}")
        i += 1

else :
    print("Error")