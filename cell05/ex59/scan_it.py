import re

text = (input("Text : "))
seacrh = (input("Seacrh : "))
pattern = rf"\b{seacrh}\b"
res = re.findall(pattern, text, re.IGNORECASE)

if len(res) == 0 :
    print("none")

else :
    print(len(res))