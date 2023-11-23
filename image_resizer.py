"""
image_resizer.py
Nick Flanders & João Vitor Caversan
Creates a new directory with all images in the given directory
resized to (orignal width * WIDTH_RATIO) x (original height * HEIGHT_RATIO)
"""

import sys
import os
import math
from PIL import Image


def update_progress(completed, message=None, width=40):
    """
    Display a progress bar for a task that is the given percent completed
    :param completed:   the ratio of the task completed (con the closed interval [0, 1])
    :param message:     the preceding message to display in front of the progress bar
    :param width:       the width of the progress bar
    """
    if message is None:
        message_str = ""
    else:
        message_str = message
    done_width = int(math.ceil(completed * width))
    sys.stdout.write("\r" + message_str + " [{}]".format(" " * (width - 1)) + " " + str(int(completed * 100)) + "%")
    sys.stdout.write("\r" + message_str + " " + '\u2588' * (done_width + 1))

# constants for the max height and width to resize images to
PREV_WIDTH = 800
NEW_WIDTH  = 480
PREV_HEIGHT = 480
NEW_HEIGHT  = 272

WIDTH_RATIO = (NEW_WIDTH/PREV_WIDTH)
HEIGHT_RATIO = (NEW_HEIGHT/PREV_HEIGHT)

if len(sys.argv) >= 3:
    # Joins the 3 last arguments into one because the fucking OneDrive puts a '-' in the directory name
    sys.argv[1] = " ".join((sys.argv[1], sys.argv[2], sys.argv[3]))
    sys.argv = sys.argv[:-2]
# check command line syntax
if len(sys.argv) != 2:
    print("Syntax:   python image_resizer.py <directory of images>")
    sys.exit(1)

directory = sys.argv[1]

# ensure target directory is reachable
if not os.path.exists(directory):
    print("Unable to find directory: ", directory)
    sys.exit(1)

output_dir = directory + "/resized"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

print("\nResizing images in", directory, "\n")

# log all errors to be displayed at script termination
error_log = []
img_files = os.listdir(directory)
img_files.remove("resized")
for index, infile in enumerate(img_files):
    outfile = output_dir + "/" + infile
    if not os.path.exists(outfile) and (infile == "LOGO_LogotipoKuhn.bmp" or infile == "LOGO_LogotipoKuhnElectronic.bmp"):
        try:
            im = Image.open(directory + "/" + infile)

            newWidth = int(im.width * WIDTH_RATIO)
            newHeigth = int(im.height * HEIGHT_RATIO)
            if newWidth == 0:
                newWidth = 1
            if newHeigth == 0:
                newHeigth = 1

            print(infile + " Width: " + str(im.width) + ", Height: " + str(im.height), end='')
            im = im.resize((newWidth, newHeigth), Image.Resampling.LANCZOS, reducing_gap=2.0)
            print(", newWidth: " + str(im.width) + ", newHeight: " + str(im.height))
            im.save(outfile, "bmp")
        except IOError:
            error_log.append("cannot create resized image for '%s'" % infile)
    # display progress bar
    update_progress((index + 1) / len(img_files), message="Resizing")

# check if any images failed to be resized
if len(error_log) == 0:
    print("\n\nAll images successfully resized!")
else:
    print("\n\nThe following errors occurred during resizing:")
    for error in error_log:
        print(error)