import numpy as np

import pikepdf

with pikepdf.Pdf.open('test.pdf') as pdf:

    pdf.pages.extend(pdf.pages[0:2])
    pdf.pages[1], pdf.pages[0] = (pdf.pages[0], pdf.pages[1])

    del pdf.pages[-1]
    pdf.pages.append(pdf.pages[0])

    pdf.save('test-mod.pdf')