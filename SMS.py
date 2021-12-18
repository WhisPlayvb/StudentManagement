from ast import Index
from os import path
from typing import Tuple


def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addedtime,addeddate))
            con.commit()
            res = messagebox.askyesnocancel('Notification','ID {} Name {} Added sucessfully and want to clean the form'.format(id,name),parent=addroot)
            if(res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
                dateval.set('')
        except:
            messagebox.showerror('Notification','ID Already Exist try another id',parent=addroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()     
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('510x530+30+100')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('valo.ico')
    addroot.register(False,False)
    #---------- add student lable ----------#
    idLable = Label(addroot,text='Enter ID :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idLable.place(x=10,y=10)

    nameLable = Label(addroot,text='Enter Name :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    nameLable.place(x=10,y=70)

    mobileLable = Label(addroot,text='Enter Mobile :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobileLable.place(x=10,y=130)

    emailLable = Label(addroot,text='Enter Email :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emailLable.place(x=10,y=190)

    addressLable = Label(addroot,text='Enter Address :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addressLable.place(x=10,y=250)

    genderLable = Label(addroot,text='Enter Gender :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderLable.place(x=10,y=310)
  
    dobLable = Label(addroot,text='Enter D.O.B :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    dobLable.place(x=10,y=370)

    dateLable = Label(addroot,text='Enter Date :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    dateLable.place(x=10,y=430)

    #---------- add student entry ----------#
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()


    identry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobilentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=mobileval)
    mobilentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    #---------- add student entry ----------#
    submitbtn = Button(addroot,text='Submit',font=('arial',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=submitadd)
    submitbtn.place(x=150,y=480)





    addroot.mainloop()

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%y")
        if(id != ''):
            strr = 'select *from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(name != ''):
            strr = 'select *from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(mobile != ''):
            strr = 'select *from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(email != ''):
            strr = 'select *from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(address != ''):
            strr = 'select *from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(gender != ''):
            strr = 'select *from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(dob != ''):
            strr = 'select *from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select *from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('510x530+30+100')#('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='blue')
    searchroot.iconbitmap('valo.ico')
    searchroot.register(False,False)
    #---------- add search lable ----------#
    idLable = Label(searchroot,text='Enter ID :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idLable.place(x=10,y=10)

    nameLable = Label(searchroot,text='Enter Name :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    nameLable.place(x=10,y=70)

    mobileLable = Label(searchroot,text='Enter Mobile :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobileLable.place(x=10,y=130)

    emailLable = Label(searchroot,text='Enter Email :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emailLable.place(x=10,y=190)

    addressLable = Label(searchroot,text='Enter Address :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addressLable.place(x=10,y=250)

    genderLable = Label(searchroot,text='Enter ID :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderLable.place(x=10,y=310)
  
    dobLable = Label(searchroot,text='Enter D.O.B :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    dobLable.place(x=10,y=370)
    
    dateLable = Label(searchroot,text='Enter Date :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    dateLable.place(x=10,y=430)

    #---------- add search entry ----------#
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()


    identry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobilentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=mobileval)
    mobilentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)


    #---------- add button ----------#
    submitbtn = Button(searchroot,text='Submit',font=('arial',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=search)
    submitbtn.place(x=150,y=480)





    search.mainloop()


def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()
        

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'ID {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('560x600+30+80')
    updateroot.title('Student Management System')
    updateroot.config(bg='blue')
    updateroot.iconbitmap('valo.ico')
    updateroot.register(False,False)
    #---------- add update lable ----------#
    idLable = Label(updateroot,text='Enter ID :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idLable.place(x=10,y=10)

    nameLable = Label(updateroot,text='Enter Name :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    nameLable.place(x=10,y=70)

    mobileLable = Label(updateroot,text='Enter Mobile :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobileLable.place(x=10,y=130)

    emailLable = Label(updateroot,text='Enter Email :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emailLable.place(x=10,y=190)

    addressLable = Label(updateroot,text='Enter Address :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addressLable.place(x=10,y=250)

    genderLable = Label(updateroot,text='Enter Gender :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderLable.place(x=10,y=310)
  
    dobLable = Label(updateroot,text='Enter D.O.B :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    dobLable.place(x=10,y=370)
    
    dateLable = Label(updateroot,text='Enter Date :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    dateLable.place(x=10,y=430)

    timeLable = Label(updateroot,text='Enter Time :',bg = 'gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timeLable.place(x=10,y=500)

    #---------- add update entry ----------#
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()


    identry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobilentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=mobileval)
    mobilentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=500)


    #---------- add button ----------#
    submitbtn = Button(updateroot,text='Submit',font=('arial',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=update)
    submitbtn.place(x=150,y=550)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0 ):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()

def showstudent():
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))


def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res==True):
        root.destroy()
   

##########  Connecation of Database ##########
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        # host = 'localhost'
        # user = 'root'
        # password = 'Vinayak@123'
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsysytem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsysytem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(20),email varchar(30),address varchar(100),gender varchar(10),dob varchar(15),date varchar(10),time varchar(10)'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and Now you are connected to the database',parent=dbroot)
        except:
            strr = 'use studentmanagementsysytem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database',parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('valo.ico')
    dbroot.resizable(False,False)
    root.config(bg='blue')
    
    #---------- connectdb lables ----------#
    hostlabel = Label(dbroot,text="Enter Host : ",bg='gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='gold2',font=('arial',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #----------  connectdb entery ----------#
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar() 

    hostentry = Entry(dbroot,font=('arial',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('arial',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('arial',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    
    #----------  connectdb button ----------#
    submitbutton = Button(dbroot,text='Submit',font=('arial',15,'bold'),bg='red',bd=5,width=20,activebackground='blue', activeforeground='white',
                            command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

    

##########  tick ##########
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m%y")
    clock.config(text='Date :'+ date_string +"\n" + "Time :" + time_string)
    clock.after(200,tick)
##########  Intro Slider ##########
import random
from tkinter import font, ttk
colors= ['red','green','blue']
def IntroLableColorTick():
    fg = random.choice(colors)
    SliderLable.config(fg=fg)
    SliderLable.after(2,IntroLableColorTick)
    
def IntroLableTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLable.config(text=text)
    else:
        text = text+ss[count]
        SliderLable.config(text=text)
        count += 1
    SliderLable.after(200,IntroLableTick)
#############################pip 
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Style, Treeview
from tkinter import ttk
import pandas
import pymysql 
import time
root = Tk()
root.title('Student Management System')
root.config(bg='gold2')
root.geometry('3000x700+10+10') #root.geometry('1174x700+200+50')
root.iconbitmap('Gpp logo.ico')
#root.resizable(False,False) 

##########  Frames ##########
#---------- dataentery frame ----------#
DataEntryFrame = Frame(root, bg='white', relief=GROOVE ,borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=600)
frontlable = Label(DataEntryFrame,text='Welcome',width=30,font=('arial',22,'bold'),bg="gold2")
frontlable.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add student',width=25,font=('arial',20,'bold'),bd=6,bg='skyblue3',activebackground='skyblue3',relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('arial',20,'bold'),bd=6,bg='skyblue3',activebackground='skyblue3',relief=RIDGE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('arial',20,'bold'),bd=6,bg='skyblue3',activebackground='skyblue3',relief=RIDGE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('arial',20,'bold'),bd=6,bg='skyblue3',activebackground='skyblue3',relief=RIDGE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('arial',20,'bold'),bd=6,bg='skyblue3',activebackground='skyblue3',relief=RIDGE,
                activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export data',width=25,font=('arial',20,'bold'),bd=6,bg='skyblue3',activebackground='skyblue3',relief=RIDGE,
                activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7.  Exit',width=25,font=('arial',20,'bold'),bd=6,bg='skyblue3',activebackground='skyblue3',relief=RIDGE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)
#---------- show data frame ----------#
ShowDataFrame = Frame(root, bg='white', relief=GROOVE ,borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=620, height=600)

#---------- show data frame ----------#
style = ttk.Style()
style.configure('Treeview.Heading',font=('arial',20,'bold'),foreground='blue')
style.configure('Treeview',font=('arial',15,'bold'),background= 'cyan',foreground='black')
Scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
Scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('ID','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added time'),
                        yscrollcommand=Scroll_y.set,xscrollcommand=Scroll_x.set)

Scroll_x.pack(side=BOTTOM,fill=X)
Scroll_y.pack(side=RIGHT,fill=Y)
Scroll_x.config(command=studenttable.xview)
Scroll_y.config(command=studenttable.yview)
studenttable.heading('ID',text='ID ')
studenttable.heading('Name',text='Name ')
studenttable.heading('Mobile No',text='Mobile No ')
studenttable.heading('Email',text='Email ')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added time',text='Added time')
studenttable['show'] = 'headings'
studenttable.column('ID',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=200)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=300)
studenttable.column('Added time',width=300)

studenttable.pack(fill=BOTH,expand=1)
##########  Slider ##########
ss =  'Welcome to student management system'
count = 0
text = ''
SliderLable = Label(root, text= ss,font = ('arial',30 ,'bold'), relief=GROOVE, borderwidth=4, width=35, bg='cyan')
SliderLable.place(x=260, y=0)
IntroLableTick()
IntroLableColorTick()


##########  Clock ##########
clock = Label(root, font = ('arial',14 ,'bold'), relief=RIDGE, borderwidth=4, bg='lawn green')
clock.place(x=0, y=0)
tick()
##########  ConnectDatabaseButton ##########
connectbutton = Button(root,text='Connect To Database',width=23,font = ('arial',19 ,'bold'), relief=GROOVE, borderwidth=4,bg='green2',
activebackground='blue', activeforeground='white',command=Connectdb)
connectbutton.place(x=1050,y=0)

root.mainloop()