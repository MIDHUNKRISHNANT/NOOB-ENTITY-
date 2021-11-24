#!/usr/bin/env python
# coding: utf-8

# In[11]:


from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from tkinter import *
import numpy as np
import pandas as pd
import os


# In[12]:


#Tk class is used to create a root window
root = Tk()
root.configure(background='Ivory')
root.title('Smart Disease Predictor System')
root.resizable(0,0)


# In[13]:


pred1=StringVar()
pred2=StringVar()
pred3=StringVar()
pred4=StringVar()
l1=[]


# In[14]:


#taking first input as symptom
Symptom1 = StringVar()
Symptom1.set("Select Here")

#taking second input as symptom
Symptom2 = StringVar()
Symptom2.set("Select Here")

#taking third input as symptom
Symptom3 = StringVar()
Symptom3.set("Select Here")

#taking fourth input as symptom
Symptom4 = StringVar()
Symptom4.set("Select Here")

#taking fifth input as symptom
Symptom5 = StringVar()
Symptom5.set("Select Here")
Name = StringVar()


# In[15]:


#function to Reset the given inputs to initial position
prev_win=None
def Reset():
    global prev_win

    Symptom1.set("Select Here")
    Symptom2.set("Select Here")
    Symptom3.set("Select Here")
    Symptom4.set("Select Here")
    Symptom5.set("Select Here")
    
    NameEn.delete(first=0,last=100)
    
    pred1.set(" ")
    pred2.set(" ")
    pred3.set(" ")
    pred4.set(" ")
    try:
        prev_win.destroy()
        prev_win=None
    except AttributeError:
        pass


# In[16]:


#Exit button to come out of system
from tkinter import messagebox
def Exit():
    qExit=messagebox.askyesno("System","Do you want to exit the system")
    if qExit:
        root.destroy()
        exit()
        
#Headings for the GUI written at the top of GUI
w2 = Label(root, justify=LEFT, text="DISEASE - SPECIALIST PREDICTION", fg="Black", bg="white")
w2.config(font=("Times",40,"bold"))
w2.grid(row=1, column=0, columnspan=3, padx=100)

#Label for the name of the patient
NameLb = Label(root, text="Name of the Patient", fg="Black", bg="white")
NameLb.config(font=("Times",20,"bold"))
NameLb.grid(row=6, column=0, pady=15, sticky=W)

#Creating Labels for the symtoms of which two symptoms are compulsory
S1Lb = Label(root, text="Symptom 1", fg="Black", bg="white")
S1Lb.config(font=("Times",15,"bold"))
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="Black", bg="white")
S2Lb.config(font=("Times",15,"bold"))
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="Black",bg="white")
S3Lb.config(font=("Times",15,"bold"))
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="Black", bg="white")
S4Lb.config(font=("Times",15,"bold"))
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="Black", bg="white")
S5Lb.config(font=("Times",15,"bold"))
S5Lb.grid(row=11, column=0, pady=10, sticky=W)

#Labels for the Decision Tree algorithm

lrLb = Label(root, text="Disease & Specialist", fg="Black", bg="white", width = 20)
lrLb.config(font=("Times",30,"bold"))
lrLb.grid(row=15, column=0, pady=10,sticky=W)

OPTIONS = sorted(l1)

#Taking name as input from user
NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

#Taking Symptoms as input from the dropdown from the user
S1 = OptionMenu(root, Symptom1,*OPTIONS)
S1.grid(row=7, column=1)

S2 = OptionMenu(root, Symptom2,*OPTIONS)
S2.grid(row=8, column=1)

S3 = OptionMenu(root, Symptom3,*OPTIONS)
S3.grid(row=9, column=1)

S4 = OptionMenu(root, Symptom4,*OPTIONS)
S4.grid(row=10, column=1)

S5 = OptionMenu(root, Symptom5,*OPTIONS)
S5.grid(row=11, column=1)

#Buttons for predicting the disease using DecisionTree algorithm
dst = Button(root, text="Find Your Disease", command=DecisionTree,bg="grey",fg="white")
dst.config(font=("Times",15,"bold"))
dst.grid(row=6, column=3,padx=10)

rs = Button(root,text="Reset Inputs", command=Reset,bg="yellow",fg="Black",width=15)
rs.config(font=("Times",15,"bold"))
rs.grid(row=10,column=3,padx=10)

ex = Button(root,text="Exit System", command=Exit,bg="Red",fg="Black",width=15)
ex.config(font=("Times",15,"bold"))
ex.grid(row=11,column=3,padx=10)

#Showing the output of DecisionTree algorithm
t1=Label(root,font=("Times",15,"bold"),text="Decision Tree",height=1,bg="green"
         ,width=40,fg="Black",textvariable=pred1,relief="sunken").grid(row=15, column=1, padx=10)

#calling this function because the application is ready to run
root.mainloop()

