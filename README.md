I - Description

The project generates xlf files used by symfony for translation
The generation is done from a classic xlsx file.
The file is normalized as follows: 
- First column the key of the word  
- N column the word in a language (beware the first line must be the acronym of the language example FR/EN/ES)

II - Installation

This project need some module. To install the dependence you need install the package manager PIP
After PIP install, run in project directory:

- pip install xlrd


III - Run
To run this script you need Python.

python generation_lang.py XLSXPATH


IV - Parameter

XLSXPATH is path of  XLSX file