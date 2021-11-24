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

