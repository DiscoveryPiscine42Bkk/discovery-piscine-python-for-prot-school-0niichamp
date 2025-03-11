row = 0
while row <= 10:
    colum = 0
    print(f"Tabe de {row}: ", end="")
    while colum <= 10 :
        print(f"{row*colum}",end=" ")
        colum += 1
    row += 1
    print()
