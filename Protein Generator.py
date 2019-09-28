#import all required libraries and modules
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox
protien=""

root=Tk()

my_font = Font(family="Times New Roman", size=22, weight="bold",slant="italic")
label = Label(root, text="Welcome To Protein Generator",font=my_font).pack()
root.geometry("1366x768+0+0")

canvas=Canvas(width=480,height=265, bg='blue')
canvas.pack(expand=YES,side=LEFT)
photo2=PhotoImage(file='F:\\Python\\giphy.gif')
canvas.create_image(0,0,image=photo2, anchor=NW)

canvas=Canvas(width=500,height=250, bg='blue')
canvas.pack(expand=YES,side=TOP)
photo1=PhotoImage(file='F:\\Python\\dna_loop.gif')
canvas.create_image(0,0,image=photo1, anchor=NW)

canvas=Canvas(width=498,height=262, bg='blue')
canvas.pack(expand=YES,side=RIGHT)
photo3=PhotoImage(file='F:\\Python\\protein_.png')
canvas.create_image(0,0,image=photo3, anchor=NW)

sequ=""

def opendna():
     file1 = filedialog.askopenfile(initialdir="F:\Python\MP",title="Select DNA File",filetypes=[("Text Files","*txt files")])
     
fi=open("DNASequence.txt","r")
sequ=fi.read()
sequ=sequ.upper()
sequ=str(sequ)
fi.close()

sequ=sequ.replace("\n","")
sequ=sequ.replace("\r","")
sequ=sequ.replace(" ","")
sequ=sequ.upper()
sequ=str(sequ)

button=Button(root, text="Browse DNA File",command=opendna).place(x=124,y=550)

print(sequ)

def convert(sequ):
     protien=""
     
     print(sequ)
     
     codontable={
         'ATT':'I','ATC':'I','ATA':'I',

         'CTT':'L','CTC':'L','CTA':'L','CTG':'L','TTA':'L','TTG':'L',

         'GTT':'V','GTC':'V','GTA':'V','GTG':'V',

         'TTT':'F','TTC':'F',

         'ATG':'M',

         'TGT':'C','TGC':'C',

         'GCT':'A','GCC':'A','GCA':'A','GCG':'A',

         'GGT':'G','GGC':'G','GGA':'G','GGG':'G',

         'CCT':'P','CCC':'P','CCA':'P','CCG':'P',

         'ACT':'T','ACC':'T','ACA':'T','ACG':'T',

         'TCT':'S','TCC':'S','TCA':'S','TCG':'S','AGT':'S','AGC':'S',

         'TAT':'Y','TAC':'Y',

         'TGG':'W',

         'CAA':'Q','CAG':'Q',

         'AAT':'N','AAC':'N',

         'CAT':'H','CAC':'H',

         'GAA':'E','GAG':'E',

         'GAT':'D','GAC':'D',

         'AAA':'K','AAG':'K',

         'CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R',

         'TAA':'Stop','TAG':'Stop','TGA':'Stop'
     }
     
     if (len(sequ)%3==0) :
         for i in range(0,len(sequ),3) :
            protien=protien+codontable[sequ[i:i+3]]
            
         protien=str(protien)
         fo=open("ProteinSequence.txt","w+")
         fo.write(protien)
         fo.close()
         messagebox.showinfo("Success","Conversion Done")
         print(protien)
         
     else :
         sequ=sequ[:-1]
         convert(sequ) 


button=Button(root, text="Start Conversion",command=lambda:convert(sequ))
button.pack(side=BOTTOM)
button.place(x=124,y=600)

def openpro():
     from os import startfile
     startfile("F:\Mini Project\ProteinSequence.txt")

Button(root, text="Open Protein File",command=openpro).place(x=124,y=650)
w = Label(root, text="*The text should be in the form of a,c,g and t only")
w.place(x=280,y=650)
root.mainloop()
