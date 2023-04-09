import os
import sys
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for k in letters.lower():
    os.system("./display {} {} {}".format(sys.argv[1],sys.argv[2],k))


