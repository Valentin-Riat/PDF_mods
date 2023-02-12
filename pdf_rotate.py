import pikepdf
import os

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


if __name__ == '__main__' :
    rotate('test.pdf', 90, [1,2])
