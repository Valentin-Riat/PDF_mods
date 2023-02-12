# Goals
- [x] rotate some pages
- [ ] remove the "title" of PDFs
	https://pikepdf.readthedocs.io/en/latest/topics/metadata.html
	
- [x] merge/remove pages from a PDF and merge them
	https://pikepdf.readthedocs.io/en/latest/topics/pages.html#mergepdf
- [x] find a way to access theses functions easily
	- Solution 1 : copy-paste the .py file to the right folder, then execute it with the powershell with arguments
	- Solution 2 : add these script as libraries to be imported with `import`, pre-import them in a ipython profile, and add a right-click option for launching this ipython

### Solution 2

#### add these script as libraries to be imported with `import`
put the python file in the following folder : `C:\Users\valen\AppData\Local\Programs\Python\Python38\Lib`

# Installation

1) Install Python
1) add python and python/scripts to the path
1) run `pip install pikepdf` in a terminal
1) optional : if on Windows, run `pip install notifypy`
1) Clone this repository
1) Execute `add_to_lib.py` by either
	- double clicking of the file
	- if that doesn't work opening a terminal in the folder and typing `python add_to_lib.py`
1) Check if no error by looking for Windows notifications or for a `erreur_add_to_lib.txt` that would have been created

# How to use

Once installed, any function can be run by opening a terminal in the folder containing the PDFs typing `py` (or `python` if that does not work).

This could open a python terminal.

You can then import the libs by typing `import ez_pdf as ez` for example.
On importation, a help message should appear. If not simply type `ez.help()` 

