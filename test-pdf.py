import numpy as np

import pikepdf

with pikepdf.Pdf.open('test.pdf') as pdf:

    pdf.pages.extend(pdf.pages[0:2])
    pdf.pages[1], pdf.pages[0] = (pdf.pages[0], pdf.pages[1])

    del pdf.pages[-1]
    pdf.pages.append(pdf.pages[0])

    pdf.save('test-mod.pdf')

with pikepdf.Pdf.open('test2.pdf') as pdf:
    print(pdf.pages[0].label)
    print(pdf.pages[1].label)
    print(pdf.pages[3].label)