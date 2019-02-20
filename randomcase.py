#!/usr/bin/env python3
import sys
from random import seed, randint
if len(sys.argv) != 2:
    print("No input.")
    sys.exit(1)
seed()
output = ""
for i in sys.argv[1]:
    if randint(0, 1) == 0:
        output += i.upper()
    else:
        output += i.lower()
print(output)