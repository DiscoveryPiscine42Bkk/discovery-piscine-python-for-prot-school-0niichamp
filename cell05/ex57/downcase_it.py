import sys
if len(sys.argv) > 1 :
    print(" ".join(arg.lower() for arg in sys.argv[1:]))

else :
    print()