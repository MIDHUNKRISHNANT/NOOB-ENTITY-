#!/usr/bin/env python
# coding: utf-8

# # IMPORTING LIBRARIES

# In[1]:


from mpl_toolkits.mplot3d import Axes3D            # To plot 3D objects on a 2D matplotlib figure.     
from sklearn.preprocessing import StandardScaler   # To standardizes a feature
import matplotlib.pyplot as plt                    # To plot  
from tkinter import *                              # for creating the GUI
import numpy as np                                 # For array functions
import pandas as pd                                #  For cleaning, transforming, manipulating and analyzing data
import os


# # DATA ACQUISITION AND PROCESSING

# In[2]:


# List of the symptoms is listed here in list "l1".

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']


# In[3]:


# List of Diseases with the specialist to be consulted is listed in list "disease".

disease=['Fungal infection - Dermatologist', 'Allergy - Allergist', 'GERD - Gastroentrologist', 'Chronic cholestasis - Hepatologist',
       'Drug Reaction - Allergist', 'Peptic ulcer disease - Gastroentrologist', 'AIDS - General Physician', 'Diabetes - Endocrinologist',
       'Gastroenteritis - Gastroentrologist', 'Bronchial Asthma - Pulmonologist', 'Hypertension - Cardiologist', 'Migraine - Neurologist',
       'Cervical spondylosis - Orthopedic', 'Paralysis (brain hemorrhage) - Neurologist', 'Jaundice - Gastroentrologist',
       'Malaria - General Physician', 'Chicken pox - General Physician', 'Dengue - General Physician', 'Typhoid - General Physician', 'hepatitis A - Hepatologist',
       'Hepatitis B - Hepatologist', 'Hepatitis C - Hepatologist', 'Hepatitis D - Hepatologist', 'Hepatitis E - Hepatologist',
       'Alcoholic hepatitis - Hepatologist', 'Tuberculosis - Pulmonologist', 'Common Cold - General Physician', 'Pneumonia - Pulmonologist',
       'Dimorphic hemmorhoids(piles)', 'Heart attack - Cardiologist', 'Varicose veins - Phlebologist',
       'Hypothyroidism - Endocrinologist', 'Hyperthyroidism - Endocrinologist', 'Hypoglycemia - Endocrinologist',
       'Osteoarthristis - Rheumatologist', 'Arthritis - Rheumatologist',
       '(vertigo) Paroymsal  Positional Vertigo - Neurologist', 'Acne - Dermatologist',
       'Urinary tract infection - Urologist', 'Psoriasis - Dermatologist', 'Impetigo - Dermatologist']

#disease = [df['prognosis'].unique()]
#print(disease)


# In[4]:


# List to Store the Input Symptoms (Zero padded)
l2=[]
for i in range(0,len(l1)):
    l2.append(0)
print(l2)


# In[5]:


# Reading training.csv

df=pd.read_csv("C:/Users/ABHIJITH/Desktop/IBM/training.csv")
DF= pd.read_csv("C:/Users/ABHIJITH/Desktop/IBM/training.csv", index_col='prognosis')

# Replace the values in the imported file by pandas by the inbuilt function replace in pandas.


# Replacing string into integer for smooth processing

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)

#df.head()

# first 5 elements from DF dataframe
DF.head()


# ## ANALYSING TRAINING DATA THORUGH DISTRIBUTION GRAPHS

# In[6]:


# Distribution graphs (histogram/bar graph) of column data

def plotPerColumnDistribution(df1, nGraphShown, nGraphPerRow):
    nunique = df1.nunique()
    df1 = df1[[col for col in df if nunique[col] > 1 and nunique[col] < 50]]  # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df1.shape
    columnNames = list(df1)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()


# In[7]:


# Scatter and density plots

def plotScatterMatrix(df1, plotSize, textSize):
    df1 = df1.select_dtypes(include =[np.number])           # keep only numerical columns
    
    
    # Remove rows and columns that would lead to df being singular
    
    df1 = df1.dropna('columns')
    df1 = df1[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    columnNames = list(df)
    if len(columnNames) > 10:                               # reduce the number of columns for matrix inversion of kernel density plots
        columnNames = columnNames[:10]
    df1 = df1[columnNames]
    ax = pd.plotting.scatter_matrix(df1, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df1.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k = 1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
    
    plt.suptitle('Scatter and Density Plot')
    plt.show()


# In[8]:


# plot histograph/bar graph

plotPerColumnDistribution(df, 10, 5)


# In[9]:


# Plot Scatter and density plot

plotScatterMatrix(df, 20, 10)


# In[10]:


X= df[l1]
y = df[["prognosis"]]

np.ravel(y)            # Return 1-D array containing the elements of y

print(X)               # Print the symptoms in the training dataset


# In[11]:


print(y)       # Print the Prognosis in the training dataset


# ## ANALYSING TESTING DATA THROUGH DISTRIBUTION GRAPHS

# In[12]:


#Reading the  testing.csv file

tr=pd.read_csv(r"C:\Users\ABHIJITH\Desktop\IBM\testing.csv")


#Using inbuilt function replace in pandas for replacing the values

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)
tr.head()


# In[13]:


# Plot histogram/bar pgraph

plotPerColumnDistribution(tr, 10, 5)


# In[14]:


plotScatterMatrix(tr, 20, 10)


# In[15]:


X_test= tr[l1]
y_test = tr[["prognosis"]]

np.ravel(y_test)     # Return 1-D array containing the elements of y_test

print(X_test)        # Print the symptoms in testing dataset


# In[16]:


print(y_test)       # Print the prognosis in the testing dataset


# In[17]:


#list1 = DF['prognosis'].unique()

def scatterplt(disease):
    x = ((DF.loc[disease]).sum())          #total sum of symptom reported for given disease
    x.drop(x[x==0].index,inplace=True)     #droping symptoms with values 0
    print(x.values)
    y = x.keys()                           #storing name of symptoms in y
    print(len(x))
    print(len(y))
    plt.title(disea)
    plt.scatter(y,x.values)
    plt.show()

def scatterinp(sym1,sym2,sym3,sym4,sym5):
    x = [sym1,sym2,sym3,sym4,sym5]         #storing input symptoms in y
    y = [0,0,0,0,0]                        #creating and giving values to the input symptoms
    if(sym1!='Select Here'):
        y[0]=1
    if(sym2!='Select Here'):
        y[1]=1
    if(sym3!='Select Here'):
        y[2]=1
    if(sym4!='Select Here'):
        y[3]=1
    if(sym5!='Select Here'):
        y[4]=1
    print(x)
    print(y)
    plt.scatter(x,y)
    plt.show()


# # TKINTER MODULE INSTANCE

# In[18]:


root = Tk()


# # ML MODEL - DECISION TREE ANALYSIS

# In[19]:


#Decision Tree Algorithm

pred1=StringVar()
def DecisionTree():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp=messagebox.askokcancel("System","Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif((Symptom1.get()=="Select Here") or (Symptom2.get()=="Select Here")):
        pred1.set(" ")
        sym=messagebox.askokcancel("System","Kindly Fill atleast first two Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn import tree                # Import Decision Tree Algorithm from sklearn library
        
        
        # Creating ML model using Decision tree Classifier and training the model usinf training data
        clf3 = tree.DecisionTreeClassifier() 
        clf3 = clf3.fit(X,y)

        # Importing features to find the efficiency of the model
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        
        # Predicting using the ML model
        y_pred=clf3.predict(X_test)
        
        # Print the accuracy score and confusion matrix for effiency analysis
        print("Decision Tree")
        print("Accuracy")
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred,normalize=False))
        print("Confusion matrix")
        conf_matrix=confusion_matrix(y_test,y_pred)
        print(conf_matrix)

        # Reading the input symptoms
        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]   

        # Input symptoms in checked in the symptom list L1
        for k in range(0,len(l1)):
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        # Input symptoms is given to the ML Model for prediction
        inputtest = [l2]
        predict = clf3.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(predicted == a):
                h='yes'
                break

    
        if (h=='yes'):
            pred1.set(" ")
            pred1.set(disease[a])
        else:
            pred1.set(" ")
            pred1.set("Not Found")
         
        
        
        #Creating the database if not exists named as database.db and creating table if not exists named as DecisionTree using sqlite3 
        
        import sqlite3 
        conn = sqlite3.connect(r"C:\Users\ABHIJITH\Downloads\database.db") 
        c = conn.cursor() 
        c.execute("CREATE TABLE IF NOT EXISTS DecisionTree(Name StringVar,Symtom1 StringVar,Symtom2 StringVar,Symtom3 StringVar,Symtom4 TEXT,Symtom5 TEXT,Disease StringVar)")
        c.execute("INSERT INTO DecisionTree(Name,Symtom1,Symtom2,Symtom3,Symtom4,Symtom5,Disease) VALUES(?,?,?,?,?,?,?)",(NameEn.get(),Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get(),pred1.get()))
        conn.commit()  
        c.close() 
        conn.close()
        
        
        #printing scatter plot of input symptoms
        #printing scatter plot of disease predicted vs its symptoms
        scatterinp(Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get())
        scatterplt(pred1.get())


# In[20]:


#Tk class is used to create a root window

root.configure(background='White')
root.title('Smart Disease - Specialist Prediction System')
root.resizable(0,0)


# In[21]:


#for selecting the symptoms from the drop down list

Symptom1 = StringVar()
Symptom1.set("Select Here")

Symptom2 = StringVar()
Symptom2.set("Select Here")

Symptom3 = StringVar()
Symptom3.set("Select Here")

Symptom4 = StringVar()
Symptom4.set("Select Here")

Symptom5 = StringVar()
Symptom5.set("Select Here")
Name = StringVar()


# In[22]:


#reset function

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
    try:
        prev_win.destroy()
        prev_win=None
    except AttributeError:
        pass


# In[23]:


#system pop-up for exit button

from tkinter import messagebox
def Exit():
    qExit=messagebox.askyesno("System","Do you want to exit the system")
    
    if qExit:
        root.destroy()
        exit()


# In[24]:


#Headings for the GUI written at the top of GUI (PROJECT NAME)

w2 = Label(root, justify=LEFT, text="DISEASE - SPECIALIST PREDICTION", fg="Black", bg="White")
w2.config(font=("Times",40,"bold"))
w2.grid(row=1, column=0, columnspan=3, padx=100)


# In[25]:


#Label for the name of the patient

NameLb = Label(root, text="Name of the Patient *", fg="Black", bg="White")
NameLb.config(font=("Times",20,"bold"))
NameLb.grid(row=6, column=0, pady=15, sticky=W)


# In[26]:


#Creating Labels for the symptoms of which two symptoms are compulsory

S1Lb = Label(root, text="Symptom 1 *", fg="Black", bg="White")
S1Lb.config(font=("Times",15,"bold"))
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2 *", fg="Black", bg="White")
S2Lb.config(font=("Times",15,"bold"))
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="Black",bg="White")
S3Lb.config(font=("Times",15,"bold"))
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="Black", bg="White")
S4Lb.config(font=("Times",15,"bold"))
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="Black", bg="White")
S5Lb.config(font=("Times",15,"bold"))
S5Lb.grid(row=11, column=0, pady=10, sticky=W)


# In[27]:


#Labels for the Decision Tree algorithm

lrLb = Label(root, text="Disease & Specialist", fg="Black", bg="white", width = 20)
lrLb.config(font=("Times",30,"bold"))
lrLb.grid(row=15, column=0, pady=10,sticky=W)

OPTIONS = sorted(l1)


# In[28]:


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


# In[29]:


#Buttons for predicting the disease using DecisionTree algorithm

dst = Button(root, text="Find Your Disease", command=DecisionTree,bg="Grey",fg="White")
dst.config(font=("Times",15,"bold"))
dst.grid(row=7, column=3,padx=10)

rs = Button(root,text="Reset Inputs", command=Reset,bg="yellow",fg="Black",width=15)
rs.config(font=("Times",15,"bold"))
rs.grid(row=9,column=3,padx=10)

ex = Button(root,text="Exit", command=Exit,bg="Red",fg="Black",width=15)
ex.config(font=("Times",15,"bold"))
ex.grid(row=11,column=3,padx=10)


# In[30]:


#Showing the output of DecisionTree algorithm

t1=Label(root,font=("Times",15,"bold"),text="Decision Tree",height=1,bg="green"
         ,width=40,fg="Black",textvariable=pred1,relief="sunken").grid(row=15, column=1, padx=10)



# In[31]:


#calling this function because the application is ready to run

root.mainloop()


# # END
