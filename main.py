from os import listdir
from os.path import isfile, join
mypath="."
onlyfiles = [f for f in listdir(mypath) if f.endswith(".md")]
for f in onlyfiles: print(" ..\dataproductpoc-docs\%s: ''"%f)