from cgitb import text
from re import template
from tkinter import *
from tkinter import messagebox
import cv2
root=Tk()
root.state('zoomed')
name=StringVar()
def generate():
    template=cv2.imread('template.jpg')
    n=name.get()
    cv2.putText(template,n,(550,620),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2,cv2.LINE_AA)
    cv2.imwrite(f'F:\SFSEC\Certificate Generate Trial\Cert\{n}.jpg',template)
    messagebox.showinfo("Successful","Certificate generated successfully ... ")
l=Label(root,text="Name of the Student : ")
l.place(x=50,y=50)
e=Entry(root,textvariable=name)
e.place(x=250,y=50)
b=Button(root,text="Generate Certificate",command=generate)
b.place(x=50,y=100)

root.mainloop()