#!/usr/bin/env mpcpython
#jordi-r Thu 25 Nov 2010 17:14:28 GMT

import sys
import os

sTarget = sys.argv[1]
listWords = sys.argv[2:]
listWords.reverse()
for i in listWords:
    os.system("echo %s | oi -i %s"  %(i,sTarget))



