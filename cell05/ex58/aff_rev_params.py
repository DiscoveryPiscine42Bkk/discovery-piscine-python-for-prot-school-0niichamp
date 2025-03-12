import sys

if len(sys.argv) > 1 :
    reversed = sys.argv[1:][::-1]
    for arg in reversed :
        print(arg)

else :
    print()