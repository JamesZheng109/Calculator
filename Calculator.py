#Imports
from tkinter import Tk,Text,Button
#Functions
def write(text=None):
    Input.config(state='normal')
    if text!=None:
        Input.insert(index='end',chars=text)
    elif text==None:
        Input.delete('1.0','end')
    Input.config(state='disabled')
def outcome():
    info=Input.get('1.0','end')
    try:
        #Solves equation if there is something
        if info!='\n':
            write();write(eval(info))
    except:
        #Error Message
        write();write('Listen here you little shit.')
def decimalandpercent(num=''):
    info=Input.get('1.0','end')
    try:
        #Check to see if there is something
        if info!='\n':
            #To decimal
            if num=='decimal':
                write();write(float(info)/100)
            #To percent
            elif num=='percent':
                write();write(float(info)*100)
    except:
        #Error Message
        write();write('Listen here you little shit.')
#Window info
window=Tk();window.title('Calculator');window.geometry('200x310');window.config(bg='black');window.wm_attributes('-toolwindow',True)
#Textbox
Input=Text(window,width=13,height=2,font=('Times New Roman',20),state='disabled');Input.place(x=7,y=10)
#Buttons
Button(window,text=1,width=5,height=2,bg='orange',command=lambda:(write(1))).place(x=10,y=100)
Button(window,text=2,width=5,height=2,bg='orange',command=lambda:(write(2))).place(x=55,y=100)
Button(window,text=3,width=5,height=2,bg='orange',command=lambda:(write(3))).place(x=100,y=100)
Button(window,text='+',width=5,height=2,bg='orange',command=lambda:(write('+'))).place(x=145,y=100)
Button(window,text=4,width=5,height=2,bg='orange',command=lambda:(write(4))).place(x=10,y=140)
Button(window,text=5,width=5,height=2,bg='orange',command=lambda:(write(5))).place(x=55,y=140)
Button(window,text=6,width=5,height=2,bg='orange',command=lambda:(write(6))).place(x=100,y=140)
Button(window,text='-',width=5,height=2,bg='orange',command=lambda:(write('-'))).place(x=145,y=140)
Button(window,text=7,width=5,height=2,bg='orange',command=lambda:(write(7))).place(x=10,y=180)
Button(window,text=8,width=5,height=2,bg='orange',command=lambda:(write(8))).place(x=55,y=180)
Button(window,text=9,width=5,height=2,bg='orange',command=lambda:(write(9))).place(x=100,y=180)
Button(window,text='*',width=5,height=2,bg='orange',command=lambda:(write('*'))).place(x=145,y=180)
Button(window,text=0,width=5,height=2,bg='orange',command=lambda:(write(0))).place(x=10,y=220)
Button(window,text='.',width=5,height=2,bg='orange',command=lambda:(write('.'))).place(x=55,y=220)
Button(window,text='=',width=5,height=2,bg='orange',command=lambda:(outcome())).place(x=100,y=220)
Button(window,text='/',width=5,height=2,bg='orange',command=lambda:(write('/'))).place(x=145,y=220)
Button(window,text='CLEAR',width=5,height=2,bg='orange',command=lambda:(write())).place(x=10,y=260)
Button(window,text='PER',width=5,height=2,bg='orange',command=lambda:(decimalandpercent('percent'))).place(x=55,y=260)
Button(window,text='DEC',width=5,height=2,bg='orange',command=lambda:(decimalandpercent('decimal'))).place(x=100,y=260)
Button(window,text='**(^)',width=5,height=2,bg='orange',command=lambda:(write('**'))).place(x=145,y=260)
#Mainloop
window.mainloop()

