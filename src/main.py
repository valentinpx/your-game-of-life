import sys
import base64
from math import sqrt
from img import create_image, create_gif
from gol import get_next_gen

MAN = """USAGE
\tpython3 src/main.py [key path]

DESCRIPTION
\t[key path]\tPath to the ssh key"""
DEST_PATH = "ygol.gif"
FRAMES = 1000

# Definitions
def key_to_binary(key_path):
    dest = []
    key_str = open(key_path, "r").read().replace("\n", "")[35:-33].encode("ascii")
    decoded = base64.decodebytes(key_str)

    for byte in decoded:
        for bit in "{:08b}".format(byte):
            dest.append(0 if bit == '0' else 1)
    return dest

def binary_to_map(binary, width):
    dest = []
    line = []

    for bit in binary:
        if (len(line) >= width):
            dest.append(line)
            line = []
        line.append(bit)
    if (line != []):
        while (len(line) < width):
            line.append(0)
        dest.append(line)
    return dest

def compute_height(bin_len, width):
    if (bin_len / width == bin_len // width):
        return (bin_len // width)
    return int(bin_len / width + 1)

# Args parse
if (len(sys.argv) != 2 or sys.argv[1] == "-h"):
    print(MAN)
    sys.exit(1)

# Execution
binary = key_to_binary(sys.argv[1])
width = int(sqrt(len(binary)))
height = compute_height(len(binary), width)
cells_arr = [binary_to_map(binary, width)]

for i in range(FRAMES - 1):
    cells_arr.append(get_next_gen(cells_arr[-1]))

# Result
imgs = []

for cells in cells_arr:
    imgs.append(create_image((width * 10, height * 10), cells))
create_gif(DEST_PATH, (width * 10, height * 10), imgs)
