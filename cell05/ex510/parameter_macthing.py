import sys

if len(sys.argv) > 1 :
    original_word = (sys.argv[1])
    secord_word = (input(f"What was the parameter? : "))
    if original_word == secord_word :
        print("Good jod!")

    else :
        print("Nope, sorry....")

else :
    print("none")