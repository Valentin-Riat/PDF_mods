import numpy as np
import argparse
import pikepdf
import os

# Go to the folder where the python file is executed
# This way, if the python file is called from a command line,
# the relative filepaths will have the folder of the python file as a refence 
# and not the folder from which the command line is opened
file_path = os.path.dirname(__file__)
if file_path != "" :
    os.chdir(file_path)


# # uncomment only for tests
# # it replaces the parsed arguments with a "fake" ones
# class arguments:
#   def __init__(self):
#     self.file = "test - Copie.pdf"
#     self.angle = 90
#     self.pages = "2"
# args = arguments()

# Parse arguments passed from the command line
parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help="pdf filename")
parser.add_argument('angle', type=int, help="rotation angle (multiple of 90). type 90 for clockwise rotation, -90 for ccw rotation, 180 to reverse the page")
parser.add_argument('pages', type=str, help="pages selected for rotation (write \"1 3\" or '1 3' to rotate pages 1 and 3), if none are specificed, all pages are rotated",default="",nargs="?") # nargs="?" allows the argument to be present 0 or 1 time
parser.add_argument('-o','--overwrite', action='store_true', help="specifies that the original file must be overwritten")
args = parser.parse_args()
print(args.overwrite)
# get all the pages as list of ints
pages = [int(page) for page in args.pages.split(" ") if page != ""]

# Open the pdf 
with pikepdf.Pdf.open(args.file) as pdf:
    nb_pages = len(pdf.pages)
    
    # if pages is empty, it means that no pages where specified,
    # in this case, we want to select all the pages
    if pages == [] :
        pages = range(1,nb_pages+1)
    
    for page_num in pages :
        pdf.pages[page_num-1].Rotate = args.angle

    # save back the file
    rotated_filename = '.'.join(args.file.split('.')[0:-1]) + "_rotated.pdf"
    pdf.save(rotated_filename)

if args.overwrite :
    os.remove(args.file)
    os.rename(rotated_filename, args.file)