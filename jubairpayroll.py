from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

#-------------------------------------------DATABASE CONNECTION----------------------------
con=mysql.connector.connect(host='localhost',user='root',password="",database="payrollsystem")
cur=con.cursor(buffered=True)

#try:
 #   cur.execute('use payrollsystem')
#except:
 #   cur.execute('create database payrollsystem')
  #  cur.execute('use payrollsystem')
#try:
 #   cur.execute('describe payrollsys')
#except:
 #   cur.execute("create table payrollsys(employeename varchar(20), address varchar(20),employeeidno int(20),employeeroll varchar(20),jobstatus varchar(20),basicsalary int(20),present int(20),absent int(20),workingdays int(20),Swl int(20),cOff int(20),overtime int(20),deduction int(20),Loan int(20),gst int(20),department varchar(20),age int(20),gender varchar(20),postpin int(20),netpay int(20),grosspay int(20),pensionpay int(20),paydate int(20),totalamount int(20))")    
def save():
     cur.execute(f"insert into payrollsys(employeename,address,employeeidno,employeeroll,jobstatus,basicsalary,present,absent,workingdays,Swl,cOff,overtime,deduction,Loan,gst,department,age,gender,postpin,netpay,grosspay,pensionpay,paydate,totalamount) values('{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{e6.get()}','{e7.get()}','{e8.get()}','{e9.get()}','{e10.get()}','{e11.get()}','{e12.get()}','{e13.get()}','{e14.get()}','{e15.get()}','{e16.get()}','{e17.get()}','{e18.get()}','{e19.get()}','{e20.get()}','{e21.get()}','{e22.get()}','{e23.get()}','{e24.get()}')")
     con.commit()          


parentwin = Tk()
parentwin.geometry("1350x650")
parentwin.title("payroll system")
bg ='white'
#----------------------------------- <Title> -----------------------------------------------------------------------
LblTitle = Label(parentwin,text="Payroll Management System",font = ("arial",30,'bold'),relief="raise",bd=5,fg='Red')
LblTitle.place(x=420,y=20)
#-------------------------------------<TOP PARENT WIN>--------------------------------------------------------------

Lbl = LabelFrame(parentwin,bd=10)
Lbl.place(x=20,y=90,width=680,height=650)


Lbl1 = Label(parentwin,text="Employee Name",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl1.place(x=30,y=110)
e1 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=42)
e1.place(x=200,y=115)

Lbl2 = Label(parentwin,text="Address",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl2.place(x=30,y=170)
e2 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=42)
e2.place(x=200,y=170)

Lbl3 = Label(parentwin,text="Employee id No",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl3.place(x=30,y=230)
e3 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=42)
e3.place(x=200,y=230)

Lbl4 = Label(parentwin,text="Employee Roll",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl4.place(x=30,y=290)
e4 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=42)
e4.place(x=200,y=290)

Lbl5 = Label(parentwin,text="Job Status",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl5.place(x=30,y=350)
e5 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=42)
e5.place(x=200,y=350)



#----------------------------------------<Bottom>-----------------------------------------

Lbl6= Label(parentwin,text="Basic Salary",font = ("arial",10,'bold'),fg='Red',bd=5)
Lbl6.place(x=30,y=450)
e6 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=27)
e6.place(x=130,y=450)

Lbl7 = Label(parentwin,text="Present",font = ("arial",10,'bold'),fg='Red',bd=5)
Lbl7.place(x=30,y=490)
e7 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=27)
e7.place(x=130,y=490)

Lbl8 = Label(parentwin,text="Absent",font = ("arial",10,'bold'),fg='Red',bd=5)
Lbl8.place(x=30,y=530)
e8 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=27)
e8.place(x=130,y=530)

Lbl9 = Label(parentwin,text="Workingdays",font = ("arial",10,'bold'),fg='Red',bd=5)
Lbl9.place(x=30,y=574)
e9 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=27)
e9.place(x=130,y=573)

Lbl10 = Label(parentwin,text="Swl",font = ("arial",10,'bold'),fg='Red',bd=5)
Lbl10.place(x=30,y=626)
e10 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=27)
e10.place(x=130,y=626)

Lbl11 = Label(parentwin,text="C-Off",font = ("arial",10,'bold'),fg='Red',bd=5)
Lbl11.place(x=30,y=677)
e11 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=27)
e11.place(x=130,y=677)

#-----------------------------------<Right Bottom>---------------------------------------

Lbl12 = Label(parentwin,text="OverTime",font = ("arial",10,'bold'),fg='Red',bd=25)
Lbl12.place(x=350,y=430)
e12 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=29)
e12.place(x=460,y=445)

Lbl13 = Label(parentwin,text="Deduction",font = ("arial",10,'bold'),fg='Red',bd=25)
Lbl13.place(x=350,y=470)
e13 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=29)
e13.place(x=460,y=490)

Lbl14 = Label(parentwin,text="Loan",font = ("arial",10,'bold'),fg='Red',bd=25)
Lbl14.place(x=350,y=510)
e14 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=29)
e14.place(x=460,y=530)

Lbl15 = Label(parentwin,text="GST",font = ("arial",10,'bold'),fg='Red',bd=25)
Lbl15.place(x=350,y=554)
e15 = Entry(parentwin,font = ("arial",10,'bold'),bg='Red',bd=5,width=29)
e15.place(x=460,y=573)

#--------------------------------------<Button>------------------------------------------
Lblbu = Label(parentwin,text=">>",font = ("arial",10,'bold'),fg='Red',bd=5)
Lblbu.place(x=373,y=630)
b1=Button(parentwin,text='Attendence Correction',font=('arial',10,'bold'),fg='Blue',bd=5,width =25)
b1.place(x=460,y=630)

Lblbu = Label(parentwin,text=">>",font = ("arial",10,'bold'),fg='Red',bd=5)
Lblbu.place(x=373,y=685)
b2=Button(parentwin,text='Apply Leave',font=('arial',10,'bold'),fg='Blue',bd=5,width=25)
b2.place(x=460,y=680)

#-------------------------------------------<RightSide>----------------------------------

Lblb = LabelFrame(parentwin,bd=10)
Lblb.place(x=710,y=95,width=620,height=280)

Lbl16 = Label(parentwin,text="Department",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl16.place(x=730,y=120)
e16 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=38)
e16.place(x=880,y=120)

Lbl17 = Label(parentwin,text="Age",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl17.place(x=730,y=180)
e17 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=38)
e17.place(x=880,y=180)

Lbl18 = Label(parentwin,text="Gender",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl18.place(x=730,y=245)
e18 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=38)
e18.place(x=880,y=245)

Lbl19 = Label(parentwin,text="Post Pin",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl19.place(x=730,y=310)
e19 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=38)
e19.place(x=880,y=310)



#-----------------------------------------<Right Bottom>-----------------------------------

Lblb = LabelFrame(parentwin,bd=10)
Lblb.place(x=710,y=400,width=620,height=337)


Lbl20 = Label(parentwin,text="Net pay",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl20.place(x=730,y=425)
e20 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=22)
e20.place(x=880,y=425)

Lbl21 = Label(parentwin,text="Gross pay",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl21.place(x=730,y=480)
e21 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=22)
e21.place(x=880,y=480)

Lbl22 = Label(parentwin,text="Pension pay",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl22.place(x=730,y=540)
e22 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=22)
e22.place(x=880,y=540)

Lbl23 = Label(parentwin,text="Pay Date",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl23.place(x=730,y=600)
e23 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=22)
e23.place(x=880,y=600)

Lbl24 = Label(parentwin,text="Total Amount",font = ("arial",15,'bold'),fg='Red',bd=5)
Lbl24.place(x=730,y=660)
e24 = Entry(parentwin,font = ("arial",15,'bold'),bg='Red',bd=5,width=22)
e24.place(x=880,y=660)

#----------------------------------------------------------------------------------------

Lblb = LabelFrame(parentwin,bd=5)
Lblb.place(x=1145,y=450,width=170,height=220)

b3=Button(parentwin,text='Save',command=save,font=('arial',10,'bold'),fg='Blue',bd=5,width =15)
b3.place(x=1160,y=480)

b4=Button(parentwin,text='Rest',font=('arial',10,'bold'),fg='Blue',bd=5,width =15)
b4.place(x=1160,y=540)

b5=Button(parentwin,text='Exit',font=('arial',10,'bold'),fg='Blue',bd=5,width =15)
b5.place(x=1160,y=600)

parentwin.mainloop()
