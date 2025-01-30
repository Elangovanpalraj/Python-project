
from tkinter import *

root = Tk()

root.title('student info')

root.configure (bg='cyan')

root.geometry ('800x700')

# Label

L_name = Label (root, text='Student Name',bg='yellow', font=('Arial',10))

L_name.grid(row=0,column=0)

b_city = Label (root, text= 'Student City',bg='yellow', font=('Arial',10))

b_city.grid(row=1,column=0)

c_gender = Label (root, text='Student Gender',bg='yellow', font=('Arial',10))

c_gender.grid(row=2,column=0)

d_degree = Label (root, text='Student Degree',bg='yellow', font=('Arial',10))

d_degree.grid(row=3,column=0)

e_doc = Label (root, text='Student KYC Doc', bg='yellow',font=('Arial',10))

e_doc.grid(row=4,column=0)

f_age = Label (root, text='Student age', bg='yellow', font=('Arial', 10))

f_age.grid(row=5,column=0)

g_comment = Label (root, text='Student description', bg='yellow', font=('Arial',10))

g_comment.grid(row=6,column=0)

# Button

def info():
    name = el.get()

    city = e2.get()

    gender = select.get()

    degree = combo.get()

    L_name.config(text=" student name: "+ name)

    b_city.config (text=" student city: "+ city)

    c_gender.config(text=" student gender: "+ gender)

    d_degree.config(text='Student degree: '+degree)

bl = Button (root, text="get details", bg='green', fg='white', command = info)

bl.place (x=100,y=500)

b2 = Button (root, text="quit", bg='green',fg='white')

b2.place (x=250,y=500)

# Entry

el = Entry (root, width=30)

el.grid(row=0,column=1)

e2 = Entry (root, width=30)

e2.grid(row=1,column=1)

#e3 = Entry (root, width=10)

#e3.grid(row=2,column=1)

#Radiobutton

select = stringVar()

rl = Radiobutton (root, text='male', value="male", var = select)

r2 = Radiobutton (root, text='female', value="female", var = select)

r1.grid(row=2, column=1)

r2.grid(row=2, column=2)

#Combobox

from tkinter.ttk import *

combo = Combobox(root)

combo ['values']=('BE', 'BBA', 'BCA', 'BCom', 'MBA', 'MCA', 'Mcom')

combo.grid(row=3,column=1)

#Checkbutton

S = BooleanVar()

s.set(True)

s1=  BooleanVar()

sl.set(False)

s2 = Booleanvar ()

s2.set(False)

cl = Checkbutton (root, text='Aadhar', var=s)

cl.grid(row=4, column=1)

c2 = Checkbutton (root, text='VoterID', var=s1)

c2.grid(row=4, column=2)

c3 = Checkbutton (root, text='PAN', var=s2)

c3.grid(row=4, column=3)


#SCROLLEDTEXT:-

from tkinter import scrolledtext

st=scrolledtext.ScrolledText (root, width=30,height=5)

st.insert(INSERT, 'type your opinion about student')

st.grid(row=6,column=1)

# SPINBOX:-

spin = Spinbox (root,from_= 5,to=30,width=5)

spin.grid(row=5,column=1)



root.mainloop()
