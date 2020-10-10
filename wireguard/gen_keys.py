import os
import sys
from subprocess import call

N = 11
WG_PATH = "/usr/bin/wg"

if __name__ != "__main__":
    print("I am not a module")
    sys.exit(0)


os.chdir(os.path.dirname(os.path.realpath(__file__)))
try:
    os.mkdir("keys")
    os.chdir("keys")
except FileExistsError:
    print("Remove ./keys directory first")
    sys.exit(1)

for i in range(N):
    keyname = "%d.key" % i
    os.system(
        f'{WG_PATH} genkey | tee private{keyname} | {WG_PATH} pubkey > public{keyname}')
    if not os.path.isfile("private" + keyname):
        print("Failed to gen: %s" % keyname)
        break
else:
    print("All ok")
