import re
import sys

if len(sys.argv) > 1 :
    scan = (sys.argv[1])
    text = ' '.join(sys.argv[2:])
    pattern = rf"\b{scan}\b"
    res = re.findall(pattern, text, re.IGNORECASE)
    print(len(res))

else :
    print("none")