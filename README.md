# Useful Scripts
A repo with many useful scripts for many different uses.

## Ultimate Encoding Fixer for C language - encodingFixer.py
A python script to open a folder, replaces all special characters in comments and save all files within it, with utf-8 encoding.
All special charaters replaced are from the portuguese language, feel free to change it. The comments in question are the C language comments (// or /**/).

In order to use it, simply place it in the folder you want do modify, and run it.

## Image Resizer - image_resizer.py
Creates a new directory with all images in the given directory resized to (orignal width * WIDTH_RATIO) x (original height * HEIGHT_RATIO).
The images are saved in the .bmp format.

Syntax: python3 image_resizer.py \<directory path with all the images\>
