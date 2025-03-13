import sys

if len(sys.argv) > 1 :
    args = sys.argv[1:]
    print(f"Parameter : {len(args)}")
    word = []
    for i in args:
        word.extend(i.split())
    for text in word:
       print(f"{text} :  {len(text)} ")

else :
    print("none")