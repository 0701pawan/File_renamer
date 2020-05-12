# This Program basically converts all  first letter mp3 files into capital letter and 
# does the numbering of jpg files you can also use any other file format 

# It will run on python 3.7 as it has f string

import os
from tkinter.filedialog import askdirectory
# with help of tkinter we have the flexiblity to choose the directory without putting file path so it can be also used as a app for
# renaming the file


def choosedir():
    directory=askdirectory()
    os.chdir(directory)   #it helps to change the location of current directory
    k=1
    for i in os.listdir(directory):
        
        if i.endswith(".mp3"):
            os.renames(i,i.capitalize())#It capitilizes mp3
          
        elif i.endswith(".JPG"):
            print(i)
            os.renames(i,f"{k}.JPG")#It renames jpg to corresponding numbers
            k=k+1

if __main__=="__name__" :           
listoffiles=[]
choosedir()
