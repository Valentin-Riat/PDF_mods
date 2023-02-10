import numpy as np

import pikepdf

with pikepdf.Pdf.open('test-rotated.pdf') as pdf:
    print(pdf.pages[0]["/Type"])
    print(pdf.pages[0]["/MediaBox"].items)
    print(pdf.pages[1]["/MediaBox"].items)
    print(pdf.pages[2]["/MediaBox"].items)
    
    # pdf.pages[0].Rotate = 90
    # for page in pdf.pages:
    #    page.Rotate = 180
    # pdf.save('test-rotated2.pdf')
