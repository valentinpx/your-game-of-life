import sys
import base64
from img import createImage

MAN = """USAGE
\tpython3 src/main.py [key path]

DESCRIPTION
\t[key path]\tPath to the ssh key"""
WIDTH = 112
DEST_PATH = "ygol.png"

# Definitions
def get_map(key_path):
    dest = []
    key_str = open(key_path, "r").read().replace("\n", "")[35:-33].encode("ascii")
    decoded = base64.decodebytes(key_str)
    line = ""

    for byte in decoded:
        if (len(line) >= 112):
            dest.append(line)
            line = ""
        line += "{:08b}".format(byte)
    return dest

# Args parse
if (len(sys.argv) != 2 or sys.argv[1] == "-h"):
    print(MAN)
    sys.exit(1)

# Execution
cells = get_map(sys.argv[1])

# Print
createImage(DEST_PATH, cells)
