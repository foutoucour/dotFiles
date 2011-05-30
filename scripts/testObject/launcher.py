import os
import sys

sCurrentScriptPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(sCurrentScriptPath)

from testObject.testObject import Test

t = Test()

