from Tkinter import *
from tkMessageBox import *
import sqlite3
root1=Tk()
def fun(e):
    root1.destroy()
    root=Tk()
    con=sqlite3.Connection("projecttttttt")
    cur=con.cursor()
    cur.execute("create table if not exists student(roll_no number primary key,name varchar(20),department varchar(6),gender number,dob varchar(10),degree varchar(10))")
    cur.execute("create table if not exists members(roll_no number primary key,member_type number,foreign key(roll_no) references student)")
    cur.execute("create table if not exists quota(member_type number primary key,max_books number,max_duration number)")
    cur.execute("create table if not exists book_issue(roll_no number,isbn_no number,accession_no number,doi varchar(10),foreign key(isbn_no) references book,foreign key(roll_no) references student)")# date of issue should be sysdate
    cur.execute("create table if not exists book(isbn_no number primary key,title varchar(15),author varchar(10),publisher varchar(10),year number)")
    cur.execute("create table if not exists copies(isbn_no number,accession_no number,primary key(isbn_no,accession_no),foreign key(isbn_no) references book)")
    img=PhotoImage(file='old_library_detail.gif')
    Label(root,image=img).place(x=0,y=0)
    root.geometry("2500x1000")
    Label(root,text="  Library Information System  ",font="Algerian 50 bold",bg="wheat",fg="indianred").place(x=120,y=255)
    root.title("Home")
    def student():
        root=Toplevel()
        root.geometry("600x450")
        root.title("Student Page")
        Label(root,text="Students Profile",font="Algerian 30 bold",bg="blue",fg="red").place(x=90,y=10)
        Label(root,text=' Roll No ',font='Algerian',fg='red').place(x=90,y=70)
        roll=Entry(root)
        roll.place(x=350,y=80)
        Label(root,text=' Name ',font='Algerian',fg='red').place(x=90,y=110)
        name=Entry(root)
        name.place(x=350,y=110)
        Label(root,text='Department ',font='Algerian',fg='red',width=10,height=2).place(x=90,y=150)
        dept=Entry(root)
        dept.place(x=350,y=160)
        Label(root,text="Gender",font='Algerian',fg='red',width=10,height=2).place(x=70,y=190)
        g=IntVar()
        Radiobutton(root,text='Male',variable=g,value=1).place(x=350,y=200)
        Radiobutton(root,text='Female',variable=g,value=2).place(x=350,y=220)
        Label(root,text='Date Of Birth ',font='Algerian',fg='red',width=11,height=2).place(x=90,y=250)
        dob=Entry(root)
        dob.place(x=350,y=260)
        Label(root,text='Degree',font='Algerian',fg='red',width=10,height=2).place(x=70,y=290)
        degree=Entry(root)
        degree.place(x=350,y=305)
        Label(root,text='Member Type',font='Algerian',fg='red',width=10,height=2).place(x=90,y=320)
        z=IntVar()
        Radiobutton(root,text='Under Graduate',variable=z,value=1).place(x=350,y=330)
        Radiobutton(root,text='Post Graduate',variable=z,value=2).place(x=350,y=350)
        Radiobutton(root,text='Research Student ',variable=z,value=3).place(x=350,y=370)
        def fun():
            cur.execute("insert into student values(?,?,?,?,?,?)",(roll.get(),name.get(),dept.get(),g.get(),dob.get(),degree.get()))
            cur.execute("insert into members values(?,?)",(int(roll.get()),z.get()))
            con.commit()
        def saw():
            root=Toplevel()
            Label(root,text="Roll No ",font='Algerian',fg='red',width=11,height=2).grid(row=0,column=0)
            roll=Entry(root)
            roll.grid(row=0,column=1)
            Label(root,text='        ').grid(row=1,column=2)
            Label(root,text='       ').grid(row=16,column=0)
            def submit():
                cur.execute("select * from student where roll_no=(?)",(int(roll.get()),))
                x=cur.fetchone()
                if x[3]==1:
                    gender='Male'
                if x[3]==2:
                    gender='Female'
                Label(root,text="Roll No ",font="Algerian 30 bold",fg="blue").grid(row=3,column=0)
                Label(root,text=x[0],font="Algerian 30 bold",fg="red").grid(row=3,column=1)
                
                Label(root,text="Name ",font="Algerian 30 bold",fg="blue").grid(row=4,column=0)
                Label(root,text=x[1],font="Algerian 30 bold",fg="red").grid(row=4,column=1)

                Label(root,text="Department ",font="Algerian 30 bold",fg="blue").grid(row=5,column=0)
                Label(root,text=x[2],font="Algerian 30 bold",fg="red").grid(row=5,column=1)
    
                Label(root,text="Gender ",font="Algerian 30 bold",fg="blue").grid(row=6,column=0)
                Label(root,text=gender,font="Algerian 30 bold",fg="red").grid(row=6,column=1)
    
                Label(root,text="Date of Birth ",font="Algerian 30 bold",fg="blue").grid(row=7,column=0)
                Label(root,text=x[4],font="Algerian 30 bold",fg="red").grid(row=7,column=1)

                Label(root,text="Degree ",font="Algerian 30 bold",fg="blue").grid(row=8,column=0)
                Label(root,text=x[5],font="Algerian 30 bold",fg="red").grid(row=8,column=1)
            Button(root,text="Submit",command=submit,width=10,height=1,bg='lightcoral',font='Algerian').grid(row=2,column=0)
        Button(root,text='Insert',command=fun,width=10,height=1,bg='lightcoral',font='Algerian').place(x=250,y=400)
        Button(root,text="See Student",command=saw,width=10,height=1,bg='lightcoral',font='Algerian').place(x=380,y=400)
    Button(root,text="Add Student",command=student,width=10,height=2,bg='lightcoral',font='Algerian').place(x=400,y=350)
    def quota():
        root=Toplevel()
        root.title('Quota')
        Label(root,text='Member_type',width=30,height=3,font='Algerian',fg='red').grid(row=0,column=0)
        c=IntVar()
        Radiobutton(root,text='Under Graduate',variable=c,value=1).grid(row=0,column=1)
        Radiobutton(root,text='Post Graduate',variable=c,value=2).grid(row=1,column=1)
        Radiobutton(root,text='Research Student ',variable=c,value=3).grid(row=2,column=1)
        Label(root,text='Maximum Books Allowed',width=30,height=3,font='Algerian',fg='red').grid(row=3,column=0)
        mb=Entry(root)
        mb.grid(row=3,column=1)
        Label(root,text='Maximum Duration Allowed',width=30,height=3,font='Algerian',fg='red').grid(row=4,column=0)
        md=Entry(root)
        md.grid(row=4,column=1)
        Label(root,text='        ').grid(row=1,column=2)
        Label(root,text='       ').grid(row=62,column=0)
        def funn():
            cur.execute("update quota set max_books=(?), max_duration=(?) where member_type=(?)",(int(mb.get()),int(md.get()),c.get()))
            con.commit()
        def sett():
            root=Tk()
            Label(root,text="   Member _ Type   ",font="Algerian 20 bold",bg="blue",fg="red").grid(row=0,column=0)
            Label(root,text="   Maximum Books   ",font="Algerian 20 bold",bg="blue",fg="red").grid(row=0,column=1)
            Label(root,text="   Maximum Duration   ",font="Algerian 20 bold",bg="blue",fg="red").grid(row=0,column=2)
            cur.execute("select * from quota")
            x=cur.fetchall()
            Label(root,text="Under Graduate",font="Algerian 15 bold",fg="red").grid(row=1,column=0)
            Label(root,text=str(x[0][1])+" Books",font="Algerian 15 bold",fg="red").grid(row=1,column=1)
            Label(root,text=str(x[0][2])+" Days",font="Algerian 15 bold",fg="red").grid(row=1,column=2)
    
            Label(root,text="Post Graduate",font="Algerian 15 bold",fg="red").grid(row=2,column=0)
            Label(root,text=str(x[1][1])+" Books",font="Algerian 15 bold",fg="red").grid(row=2,column=1)
            Label(root,text=str(x[1][2])+" Days",font="Algerian 15 bold",fg="red").grid(row=2,column=2)
    
            Label(root,text="Research Student",font="Algerian 15 bold",fg="red").grid(row=3,column=0)
            Label(root,text=str(x[2][1])+" Books",font="Algerian 15 bold",fg="red").grid(row=3,column=1)
            Label(root,text=str(x[2][2])+" Days",font="Algerian 15 bold",fg="red").grid(row=3,column=2)
        
        Button(root,text='Insert',command=funn,width=10,height=2,bg='lightcoral',font='Algerian').grid(row=5,column=0)
        Button(root,text="See Quota",command=sett,width=10,height=2,bg='lightcoral',font='Algerian').grid(row=5,column=1)
    Button(root,text='Quota',command=quota,width=10,height=2,bg='lightcoral',font='Algerian').place(x=700,y=350)
    
    def issue():
        root=Toplevel()
        root.title("Book Issue")
        Label(root,text='Roll No ',font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=0,column=0)
        roll=Entry(root)
        roll.grid(row=0,column=1)
        Label(root,text="ISBN No",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=1,column=0)
        isbn=Entry(root)
        isbn.grid(row=1,column=1)
        Label(root,text='Accession No ',font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=2,column=0)
        acc=Entry(root)
        acc.grid(row=2,column=1)
        Label(root,text="Date of issue ",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=3,column=0)
        doi=Entry(root)
        doi.grid(row=3,column=1)
        Label(root,text='        ').grid(row=1,column=2)
        Label(root,text='       ').grid(row=62,column=0)
        def insert():
            cur.execute("select count(*) from copies where isbn_no=(?)",(int(isbn.get()),))
            n=cur.fetchone()
            n=n[0]
            cur.execute("select count(*) from book_issue where roll_no=(?) and isbn_no=(?)",(int(roll.get()),int(isbn.get())))
            co=cur.fetchone()
            co=co[0]
            cur.execute("select count(*) from book_issue where roll_no=(?)",(int(roll.get()),))
            x=cur.fetchone()
            x=x[0]
            cur.execute("select member_type from members where roll_no=(?)",(int(roll.get()),))
            mtype=cur.fetchone()
            mt=mtype[0]
            cur.execute("select max_books from quota where member_type=(?)",(mt,))
            ma=cur.fetchone()
            ma=ma[0]
            if n==0:
                showerror("Alert","No Copies available all are issued")
            elif co:
                showerror("Alert","Book is already issued to you my dear")
            elif x>=ma:
                showerror("Alert","You are exceeding the quota of books provided to you")
            else:
                cur.execute("select accession_no from copies where isbn_no=(?) and accession_no=(?)",(int(isbn.get()),int(acc.get())))
                z=cur.fetchone()
                if not z:
                    showerror("Alert","This book is already issued to some one else")
                else:
                    cur.execute("delete from copies where isbn_no=(?) and accession_no=(?)",(int(isbn.get()),int(acc.get())))
                    con.commit()
                    cur.execute("insert into book_issue values(?,?,?,?)",(int(roll.get()),int(isbn.get()),int(acc.get()),doi.get()))
                    showinfo("Message","Book is issued to you")
                    con.commit()
        Button(root,text='Issue',command=insert,width=10,height=2,bg='lightcoral',font='Algerian').grid(row=4,column=0)
    Button(root,text='Book Issue',command=issue,width=10,height=2,bg='lightcoral',font='Algerian').place(x=400,y=420)
    
    def ibook():
        root=Tk()
        root.title("Book Detail")
        Label(root,text="ISBN NO ",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=0,column=0)
        isbn=Entry(root)
        isbn.grid(row=0,column=1)
        Label(root,text="Title ",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=1,column=0)
        title=Entry(root)
        title.grid(row=1,column=1)
        Label(root,text="Author ",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=2,column=0)
        author=Entry(root)
        author.grid(row=2,column=1)
        Label(root,text="Publisher",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=3,column=0)
        pblsr=Entry(root)
        pblsr.grid(row=3,column=1)
        Label(root,text="Year",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=4,column=0)
        yr=Entry(root)
        yr.grid(row=4,column=1)
        Label(root,text='        ').grid(row=1,column=2)
        Label(root,text='       ').grid(row=16,column=0)
        def ins():
            cur.execute("insert into book values(?,?,?,?,?)",(int(isbn.get()),title.get(),author.get(),pblsr.get(),yr.get()))
            con.commit()
        Button(root,text="Insert",command=ins,width=10,height=2,bg='lightcoral',font='Algerian').grid(row=5,column=0)
    Button(root,text="Insert Book",command=ibook,width=10,height=2,bg='lightcoral',font='Algerian').place(x=700,y=420)

    
    def copy():
        root=Tk()
        Label(root,text="ISBN NO",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=0,column=0)
        isbn=Entry(root)
        isbn.grid(row=0,column=1)
        Label(root,text="ACCESSION NO",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=1,column=0)
        acno=Entry(root)
        acno.grid(row=1,column=1)
        Label(root,text='        ').grid(row=1,column=2)
        Label(root,text='       ').grid(row=16,column=0)
        def inst():
            cur.execute("insert into copies values(?,?)",(isbn.get(),acno.get()))
            con.commit()
        Button(root,text="Update",command=inst,width=10,height=2,bg='lightcoral',font='Algerian').grid(row=2,column=0)
    Button(root,text="Add Copies",command=copy,width=10,height=2,bg='lightcoral',font='Algerian').place(x=400,y=490)

    
    
    def srbk():
        root=Tk()
        Label(root,text="ISBN NO",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=0,column=0)
        isbn=Entry(root)
        isbn.grid(row=0,column=1)
        Label(root,text='        ').grid(row=1,column=2)
        Label(root,text='       ').grid(row=16,column=0)
        def srk():
            cur.execute("select count(*) from copies where isbn_no=(?)",(int(isbn.get()),))
            n=cur.fetchone()
            n=n[0]
            cur.execute("select * from copies where isbn_no=(?)",(int(isbn.get()),))
            z=cur.fetchall()
            cur.execute("select * from book where isbn_no=(?)",(int(isbn.get()),))
            x=cur.fetchall()
            Label(root,text="   ISBN NO   ",font="Algerian 15 bold",bg='blue',fg='red').grid(row=2,column=0)
            Label(root,text="   ACCESSION NO   ",font="Algerian 15 bold",bg='blue',fg='red').grid(row=2,column=1)
            Label(root,text="    TITLE    ",font="Algerian 15 bold",bg='blue',fg='red').grid(row=2,column=2)
            Label(root,text="   AUTHOR   ",font="Algerian 15 bold",bg='blue',fg='red').grid(row=2,column=3)
            Label(root,text="   PUBLISHER   ",font="Algerian 15 bold",bg='blue',fg='red').grid(row=2,column=4)
            Label(root,text="   YEAR   ",font="Algerian 15 bold",bg='blue',fg='red').grid(row=2,column=5)
            i=0
            while i<n:
                Label(root,text=x[0][0],font="Algerian 15 bold",fg='red').grid(row=3+i,column=0)
                Label(root,text=z[i][1],font="Algerian 15 bold",fg='red').grid(row=3+i,column=1)
                Label(root,text=x[0][1],font="Algerian 15 bold",fg='red').grid(row=3+i,column=2)
                Label(root,text=x[0][2],font="Algerian 15 bold",fg='red').grid(row=3+i,column=3)
                Label(root,text=x[0][3],font="Algerian 15 bold",fg='red').grid(row=3+i,column=4)
                Label(root,text=x[0][4],font="Algerian 15 bold",fg='red').grid(row=3+i,column=5)
                i+=1
        Button(root,text="Search",command=srk,width=10,height=2,bg='lightcoral',font='Algerian').grid(row=1,column=0)
    Button(root,text="Search Book",command=srbk,width=10,height=2,bg='lightcoral',font='Algerian').place(x=700,y=490)

    def bib():
        root=Toplevel()
        Label(root,text="ISBN NO ",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=0,column=0)
        isbn=Entry(root)
        isbn.grid(row=0,column=1)
        Label(root,text="Accession no : ",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=1,column=0)
        acc=Entry(root)
        acc.grid(row=1,column=1)
        Label(root,text='        ').grid(row=1,column=2)
        Label(root,text='       ').grid(row=16,column=0)
        def see():
            Label(root,text="   ACCESSION NO     ",font="Algerian 20 bold",bg='blue',fg='red').grid(row=3,column=0)
            Label(root,text="       ROLL NO     ",font="Algerian 20 bold",bg='blue',fg='red').grid(row=3,column=1)
            Label(root,text="   NAME        ",font="Algerian 20 bold",bg='blue',fg='red').grid(row=3,column=2)
            cur.execute("select roll_no from book_issue where accession_no=(?) and isbn_no=(?)",(int(acc.get()),int(isbn.get())))
            x=cur.fetchall()
            x=x[0][0]
            cur.execute("select * from student where roll_no=(?)",(x,))
            det=cur.fetchall()
            Label(root,text=acc.get(),font="Algerian 15 bold",fg="red").grid(row=4,column=0)
            Label(root,text=det[0][0],font="Algerian 15 bold",fg="red").grid(row=4,column=1)
            Label(root,text=det[0][1],font="Algerian 15 bold",fg="red").grid(row=4,column=2)
        Button(root,text="Get Info",command=see,width=10,height=2,bg='lightcoral',font='Algerian').grid(row=2,column=0)
    Button(root,text="Issued Info",command=bib,width=10,height=2,bg='lightcoral',font='Algerian').place(x=400,y=560)

    def ret():
        root=Toplevel()
        Label(root,text="ISBN NO",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=0,column=0)
        isbn=Entry(root)
        isbn.grid(row=0,column=1)
        Label(root,text="ACCESSION NO",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=1,column=0)
        acc=Entry(root)
        acc.grid(row=1,column=1)
        def sut():
            cur.execute("insert into copies values(?,?)",(int(isbn.get()),int(acc.get())))
            cur.execute("delete from book_issue where isbn_no=(?) and accession_no=(?)",(int(isbn.get()),int(acc.get())))
        Label(root,text='        ').grid(row=1,column=2)
        Label(root,text='       ').grid(row=16,column=0)
        Button(root,text="Submit",command=sut,width=10,height=2,bg='lightcoral',font='Algerian').grid(row=2,column=0)
    Button(root,text="Return Book",command=ret,width=10,height=2,bg='lightcoral',font='Algerian').place(x=700,y=560)

    def roll():
        root=Tk()
        Label(root,text="Roll No ",font="Algerian 15 bold",fg="red",width=15,height=2).grid(row=0,column=0)
        e=Entry(root)
        e.grid(row=0,column=1)
        Label(root,text='        ').grid(row=1,column=2)
        Label(root,text='       ').grid(row=16,column=0)
        def sub():
            cur.execute("select isbn_no,accession_no from book_issue where roll_no=(?)",(int(e.get()),))
            x=cur.fetchall()
            cur.execute("select count(*) from book_issue where roll_no=(?)",(int(e.get()),))
            no=cur.fetchone()
            n=no[0]
            Label(root,text="  ISBN NO  ",font="Algerian 40 bold",fg="blue",bg='red').grid(row=2,column=0)
            Label(root,text="   ACCESSION NO  ",font="Algerian 40 bold",fg="blue",bg='red').grid(row=2,column=1)
            i=0
            while i<n:
                Label(root,text=x[i][0],font="Algerian 50 bold",fg='red').grid(row=3+i,column=0)
                Label(root,text=x[i][1],font="Algerian 50 bold",fg='red').grid(row=3+i,column=1)
                i+=1
        Button(root,text="Submit",command=sub,width=10,height=2,bg='lightcoral',font='Algerian').grid(row=1,column=0)
    Button(root,text="Roll No",command=roll,width=10,height=2,bg='lightcoral',font='Algerian').place(x=400,y=630)
    root.mainloop()
photo=PhotoImage(file='image.gif')
lb=Label(root1,image=photo)
lb.bind('<Motion>',fun)
lb.pack()
Label(root1,text=' ').pack()
Label(root1,text=' ').pack()
Label(root1,text="Name : Abhinav Singh Parmar",font="Algerian 20 bold",fg="indianred").pack()
Label(root1,text="Enrollment No : 171B010",font="Algerian 20 bold",fg="indianred").pack()
Label(root1,text="Batch : B1",font="Algerian 20 bold",fg="indianred").pack()
Label(root1,text="Email Id : abhinavparmar147@gmail.com",font="Algerian 20 bold",fg="indianred").pack()
Label(root1,text="Mobile Number : 8718827411",font="Algerian 20 bold",fg="indianred").pack()
root1.mainloop()
