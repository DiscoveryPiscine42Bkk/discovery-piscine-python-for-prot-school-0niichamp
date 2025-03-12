import sys
if len(sys.argv) > 1 :
    print(" ".join(arg.upper() for arg in sys.argv[1:]))

else :
    print()