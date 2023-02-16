"""
Please put the following line in the powershell if the ANSI codes do not displays correctly :

            reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 1

"""

import pikepdf
import os
from operator import attrgetter

def rotate(file, angle, pages=[], overwrite=False):
    """
    rotate selected pdf pages

    file  : input pdf filename
    angle : rotation angle (multiple of 90). 
            type 90 for clockwise rotation, -90 for ccw rotation, 180 to reverse the page
    pages : pages selected for rotation (write [1 3] to rotate pages 1 and 3), 
            if none are specificed, all pages are rotated
    """
    
    # verify if overwrite is a bool
    if type(overwrite) != type(True) :
        raise TypeError("overwrite must be True of False but is of type '{}' instead".format(type(overwrite).__name__))
    
    
    # Open the pdf 
    with pikepdf.Pdf.open(file) as pdf:
        nb_pages = len(pdf.pages)
        
        # if pages is empty, it means that no pages where specified,
        # in this case, we want to select all the pages
        if pages == [] :
            pages = range(1,nb_pages+1)
        
        for page_num in pages :
            pdf.pages[page_num-1].Rotate = angle

        # save back the file
        rotated_filename = '.'.join(file.split('.')[0:-1]) + "_rotated.pdf"
        pdf.save(rotated_filename)

    if overwrite :
        os.remove(file)
        os.rename(rotated_filename, file)




def open(filename) :
    """
    open a pdf and returns a pdf object
    filename : string containing the name of the pdf to open
    """
    return pikepdf.Pdf.open(filename)


def save(pdf,filename, used_pdfs = [], close = True):
    """
    saves a pdf file from a pdf object and closes the IO object if 'close=True'
    if 'used_pdfs' is not empty, the function will cleanup the pdf before saving

    pdf       : pdf object to be saved
    filename  : filename of the saved pdf (string)
    used_pdfs : array of all the pdfs used to make the pdf to be saved 
                (for example while merging pdfs)
                This option is optonnal but useful to ensure the right pdf version is used 
    close     : is True the pdfs objects are close after the save
    """
    
    # done to accept used_pdfs inputs that are only one file instead of an array of files
    if type(used_pdfs) != type([]) :
        used_pdfs = [used_pdfs]

    # adding pdf to the list of pdfs but only if it is not already present
    # (if we put it 2 times, it will be closes 2 times at the end of the functon => error)
    if not any(elem == pdf for elem in used_pdfs):
        used_pdfs.append(pdf)

    # find the min version that the pdf to save will need to have
    version = max(used_pdfs, key=attrgetter('pdf_version')).pdf_version

    # further cleaning
    pdf.remove_unreferenced_resources()

    # save the main file
    pdf.save(filename, min_version=version)

    # close all used files
    if close :
        for p in used_pdfs :
            p.close()
    




def help():
    help_str = \
    """
    ------------------------
    {header}FUNCTIONS : {rst}

    {y}rotate{rst}(file, angle, pages=[], overwrite=False){g}
        - angle must one of these [0, 90, -90, 180]
        - if no pages is given all pages are rotated{rst}

    {y}open{rst}(filename){g}
        - takes a string give a pdf object{rst}

    {y}save{rst}(pdf,filename, used_pdfs = [], close = True){g}
        - saves pdf with the given filename
        - optionally, a list of used pdfs can be specified to ensure compatibility{rst}

    {header}PDF OBJECTS :{rst}

    pdf.pages is a list of the pages, they can be manupulated like any list :
        - expend(list_of_pages)
        - append(page)
        - insert(pos, pages)
        - (pdf.pages[0], pdf.pages[1] = pdf.pages[1], pdf.pages[0])

    ------------------------
""".format(header='\033[95m', rst= '\033[0m', y='\033[1;33m',g='\033[90m') #header is violet, y is yellow, g is gray
    
    print(help_str)


# prints the help directly when importing the lib
help()


# maybe later
# def modify_pages(, out_tuple) :








if __name__ == '__main__' :
    rotate('test.pdf', 90, [1,2])
