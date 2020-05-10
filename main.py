from tkinter import *
from tkcalendar import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import tkinter.messagebox as tmsg
from aboutme import Mydetails
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd="##########", database="testdb")
mycursor = mydb.cursor()
try:
	mycursor.execute("CREATE TABLE student (name VARCHAR(120), class INTEGER(6) ,gname VARCHAR(120), gph VARCHAR(14), go VARCHAR(100), blood VARCHAR(3), gender VARCHAR(10),sibling VARCHAR(4), address VARCHAR(250), email VARCHAR(170), hobby VARCHAR(200), dob VARCHAR(50), mt VARCHAR(150), id INTEGER(10))")
except:
	pass

class Stdb:
	width  = 720
	height = 510
	def __init__(self, root):
		self.root= root
		self.root.geometry(f"{self.width}x{self.height}")
		self.root.resizable(width = False,height = False)
		self.root.title("Student Database Management System")
		self.gender =StringVar()
		self.sibling =StringVar()
		self.Class = StringVar()

		self.main_page()
	def show_my_info(self):
		inf = Mydetails()
		inf.show("My Details")

	def intro_pic(self):
		top1 = Image.open("top1.jpg")
		newtop1 = top1.resize((600,200))
		newtop1 = ImageTk.PhotoImage(newtop1)
		t1 =Label(self.mf,image =newtop1)
		t1.place(relx =0,rely =0, relheight =0.51, relwidth =1)	
		t1.image = newtop1

		top2 = Image.open("top2.png")
		newtop2 = top2.resize((700,200))
		newtop2 = ImageTk.PhotoImage(newtop2)
		t2 =Label(self.mf,image =newtop2)
		t2.place(relx =0,rely =0.51, relheight =0.49, relwidth =1)	
		t2.image = newtop2

		top3 = Image.open("top3.jpg")
		newtop3 = top3.resize((300,200))
		newtop3 = ImageTk.PhotoImage(newtop3)
		t3 =Label(self.mf,image =newtop3)
		t3.place(relx =0.5,rely =0.51, relheight =0.49, relwidth =0.5)	
		t3.image = newtop3
		
	def sel_date(self):
		def get_date():
			self.dob.delete(0,END)
			self.dob.insert(1,cal.get_date())
			ds.destroy()
		ds= Toplevel(self.root)
		ds.title("Select date")
		cal = Calendar(ds, month = 1 ,year = 2000)
		cal.pack()
		Button(ds,text = "Select", command = get_date).pack()
	def submit(self):
		name = self.name.get()
		cl = self.cl.get()
		gname = self.gname.get()
		gph = self.gph.get()
		blood = self.blood.get()
		gender = self.gender.get()
		address = self.add.get("1.0",END)
		email =self.email.get()
		dob = self.dob.get()
		sibling = self.sibling.get()
		mt = self.mt.get()
		hobby= self.hobby.get()
		go = self.go.get()
		ID = self.stud_id.get()
		n=1 
		if name =="" or cl=="" or gname =="" or gph =="" or blood == "" or gender=="" or address == "" or email =="" or dob=="" or sibling==""  or mt=="" or hobby == "" or go=="" or ID =="":
			tmsg.showinfo("Failed !", "Please enter all the fields")
			n=0
		else:	
			try:
				check = int(gph)
			except:
				tmsg.showerror("Error!","Please enter a valid phone no.")
				n=0
			if n==1:	
				try:
					cl = int(cl)
				except:
					tmsg.showerror("Error!","Please enter a valid Class")
					n=0	
			if n==1:		
				if(len(str(ID))==5 and str(ID)[0]!='0'):	
					try:
						ID = int(ID)
					except:
						tmsg.showerror("Error!","Please Enter a valid ID")
						n=0
				else:
					tmsg.showerror("Error!","ID must be of 5 digits")	
					n=0
			if n==1:	
				try:
					mycursor.execute("SELECT id FROM student")
					fetched = mycursor.fetchall()
					for ids in fetched:
						if ids[0]==ID:
							tmsg.showerror("Error!","This ID is already in use")
							n=0
				except:
					pass		
						
		if n==1:
			sqlcommand = "INSERT INTO student(name, class, gname , gph, go, blood, gender,sibling, address, email, hobby, dob, mt, id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			mycursor.execute(sqlcommand,(name,cl,gname,gph,go,blood,gender,sibling,address,email,hobby,dob,mt,ID))	
			mydb.commit()
			tmsg.showinfo("Success!","Student data has been successfully added.")	
			self.empty_them()
			self.stud_id.delete(0,END)	
			
	def update_values(self):
		name = self.name.get()
		cl = self.cl.get()
		gname = self.gname.get()
		gph = self.gph.get()
		blood = self.blood.get()
		gender = self.gender.get()
		address = self.add.get("1.0",END)
		email =self.email.get()
		dob = self.dob.get()
		sibling = self.sibling.get()
		mt = self.mt.get()
		hobby= self.hobby.get()
		go = self.go.get()
		ID = self.stud_id.get()
		n=1 
		if name =="" or cl=="" or gname =="" or gph =="" or blood == "" or gender=="" or address == "" or email =="" or dob=="" or sibling==""  or mt=="" or hobby == "" or go=="" or ID =="":
			tmsg.showinfo("Failed !", "Please enter all the fields")
			n=0
		else:	
			try:
				check = int(gph)
			except:
				tmsg.showerror("Error!","Please enter a valid phone no.")
				n=0
			if n==1:	
				try:
					cl = int(cl)
				except:
					tmsg.showerror("Error!","Please enter a valid Class")
					n=0	
			if n==1:		
				if(len(str(ID))==5):	
					try:
						ID = int(ID)
					except:
						tmsg.showerror("Error!","Please Enter a valid ID")
						n=0
				else:
					tmsg.showerror("Error!","ID must be of 5 digits")	
					n=0	
			if n==1:
				if self.superid!= ID:
					tmsg.showerror("Error!","Cant Update details into that id.")
					n=0					
		if n==1: 
			mycursor.execute("UPDATE student SET name=%s, class=%s, gname=%s , gph=%s, go=%s, blood=%s, gender=%s,sibling=%s, address=%s, email=%s, hobby=%s, dob=%s, mt=%s WHERE id= %s" ,(name,cl,gname,gph,go,blood,gender,sibling,address,email,hobby,dob,mt,ID))	
			mydb.commit()
			tmsg.showinfo("Success!","Student data has been successfully Updated")	
			self.empty_them()
			self.stud_id.delete(0,END)
			self.superid =0

	def empty_them(self):			
			self.name.delete(0,END)
			self.cl.delete(0,END)
			self.gname.delete(0,END)
			self.gph.delete(0,END)
			self.go.delete(0,END)
			self.blood.delete(0,END)
			self.add.delete("1.0",END)
			self.email.delete(0,END)
			self.hobby.delete(0,END)
			self.dob.delete(0,END)
			self.mt.delete(0,END)
			self.gender.set("")
			self.sibling.set("")

	def setvalues(self):
		ID = self.stud_id.get()
		if ID =="":
			tmsg.showinfo("ID Required..","Enter the ID")
			return
		try:
			ID = int(ID)
			self.superid = ID
			mycursor.execute("SELECT * FROM student WHERE id = %s",(ID,))
			result = mycursor.fetchone()
			self.empty_them()
			self.name.insert(1,result[0])
			self.cl.insert(1,result[1])
			self.gname.insert(1,result[2])
			self.gph.insert(1,result[3])
			self.go.insert(1,result[4])
			self.blood.insert(1,result[5])
			self.add.insert(END,result[8])
			self.email.insert(1,result[9])
			self.hobby.insert(1,result[10])
			self.dob.insert(1,result[11])
			self.mt.insert(1,result[12])
			self.gender.set(result[6])
			self.sibling.set(result[7])
		except:
			tmsg.showinfo("Don't Exist!","The ID you entered doesnot exist.")	

	def remove_student(self):
		n = 0
		ID = self.remid.get()
		if ID=="":
			tmsg.showinfo("ID required !","Enter the ID")
		else:
			mycursor.execute("SELECT id FROM student")
			fetched = mycursor.fetchall()
			for z in fetched:
				if str(z[0])==ID:
					n = 1
			if n==1:		
				mycursor.execute("DELETE FROM student WHERE id = %s",(int(ID),))
				mydb.commit()
				tmsg.showinfo("Removed!","Student data has been successfully removed !")
				self.remid.delete(0,END)
			else:
				tmsg.showerror("Error!","Enter a valid ID")

						



	def main_page(self):
		mainframe = Frame(self.root,bg = "black" ,borderwidth = 5,relief = RIDGE)
		mainframe.place(relx = 0 ,rely = 0,relwidth = 1, relheight = 1)
		up_frame = Frame(mainframe,bg = "gray",borderwidth = 5,relief = RAISED)
		up_frame.place(relx = 0.01,rely =0.01 ,relwidth = 0.98,relheight = 0.16)
		img = Image.open("james.png")
		newim =img.resize((80,80))
		print(newim.size)
		self.logo = ImageTk.PhotoImage(newim)
		la=Label(up_frame,image= self.logo, bg= "gray")
		la.place(relx =0 ,rely =0 ,relheight= 1 ,relwidth = 0.13)	
		la.image = self.logo
		Label(up_frame ,text = "ST. JAMES SCHOOL",bg = "gray",anchor ="nw",justify = "left",fg= "brown", font =("lucida", 28 ,"bold")).place(relx =0.15, rely = 0 ,relwidth= 0.8, relheight =0.75)
		Frame(up_frame,bg ="black").place(relx=0.16, rely=0.6 ,relwidth =0.84  ,relheight = 0.05)
		Label(up_frame ,text = " STUDENT DATA MANAGEMENT APPLICATION",bg = "gray",anchor ="nw",justify = "left",fg= "black", font =("arial", 10 ,"bold")).place(relx =0.15, rely = 0.66 ,relwidth= 0.8, relheight =0.34)
		Button(up_frame,text ="Home", bg= "gray",fg ="white", bd = 3,command = self.intro_pic).place(relx = 0.915,rely=0.16, relheight =0.4,relwidth =0.08)
		Button(up_frame,text ="About Developer", bg= "gray",fg ="white", bd = 3,command = self.show_my_info).place(relx = 0.75,rely=0.16, relheight =0.4,relwidth =0.16)
		left_frame = Frame(mainframe,bg = "gray",borderwidth = 5,relief = RAISED)
		left_frame.place(relx = 0.01,rely =0.18 ,relwidth = 0.15,relheight = 0.81)
		right_frame = Frame(mainframe,bg = "gray",borderwidth = 5,relief = RAISED)
		right_frame.place(relx = 0.17,rely= 0.18,relheight =0.81,relwidth = 0.82)
		self.mf = right_frame
		self.intro_pic()
		insert_button = Button(left_frame, text = "Insert\nnew student\ndetails",anchor ="nw",justify = "left",overrelief = GROOVE,font = ("lucida",10,"underline","bold"),bg = "gray", fg = "black",bd = 5 ,command = self.insert_new)
		insert_button.place(relx = 0 ,rely =0 ,relheight = 0.2, relwidth =1)
		update_button = Button(left_frame, text = "Update\nstudent\ndetails",anchor ="nw",justify = "left",overrelief = GROOVE,font = ("lucida",10,"underline", "bold"),bg = "gray", bd = 5, command =self.update_page)
		update_button.place(relx = 0 ,rely =0.2 ,relheight = 0.2, relwidth =1)
		remove_button = Button(left_frame, text = "Remove\nstudent",anchor ="nw",justify = "left",overrelief = GROOVE,font = ("lucida",10,"underline","bold"),bg = "gray", bd = 5,command = self.remove_page)
		remove_button.place(relx = 0 ,rely =0.4 ,relheight = 0.2, relwidth =1)
		view_one_button = Button(left_frame, text = "View\nparticular\ndetails",anchor ="nw",justify = "left",overrelief = GROOVE,font = ("lucida",10,"underline","bold"),bg = "gray", bd = 5, command = self.particular_view)
		view_one_button.place(relx = 0 ,rely =0.6 ,relheight = 0.2, relwidth =1)
		view_all_button = Button(left_frame, text = "View\nall student\ndetails",anchor ="nw",justify = "left",overrelief = GROOVE,font = ("lucida",10,"underline","bold"),bg = "gray", bd = 5, command = self.all_view)
		view_all_button.place(relx = 0 ,rely =0.8 ,relheight = 0.2, relwidth =1)


	def insert_new(self):
		insert_frame = Frame(self.mf,bg = "gray",borderwidth = 5,relief = SUNKEN)
		insert_frame.place(relx = 0.015 ,rely =0.02, relheight = 0.96, relwidth = 0.97)
		Label(insert_frame ,text = "Enter new student details:",anchor = "w", fg = "black", bg = "grey", font = ("Arial",15)).place(relx= 0 ,rely =0 ,relwidth= 0.9 ,relheight = 0.083)
		Frame(insert_frame,bg ="black").place(relx=0, rely=0.085 ,relwidth = 1 ,relheight = 0.005)
		Frame(insert_frame,bg ="black").place(relx=0.5, rely=0.085 ,relwidth = 0.005 ,relheight = 0.915)
		Label(insert_frame ,text = "Name:",anchor = "w", fg = "black", bg = "grey", font = ("Arial",10)).place(relx= 0 ,rely =0.09 ,relwidth= 0.2 ,relheight = 0.1)
		self.name =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.name.place(relx= 0.13 ,rely =0.1 ,relwidth= 0.34 ,relheight = 0.07)
		Label(insert_frame ,text = "Class:",anchor = "w", fg = "black", bg = "grey", font = ("Arial",10)).place(relx= 0 ,rely =0.19 ,relwidth= 0.2 ,relheight = 0.1)
		self.cl =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.cl.place(relx= 0.13 ,rely =0.2 ,relwidth= 0.15 ,relheight = 0.07)
		Label(insert_frame ,text = "Guardian's\nName:",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",9)).place(relx= 0 ,rely =0.29 ,relwidth= 0.2 ,relheight = 0.1)
		self.gname =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.gname.place(relx= 0.13 ,rely =0.3 ,relwidth= 0.34 ,relheight = 0.07)
		Label(insert_frame ,text = "Guardian's\nPhone No.:",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",9)).place(relx= 0 ,rely =0.39 ,relwidth= 0.2 ,relheight = 0.1)
		self.gph =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.gph.place(relx= 0.13 ,rely =0.4 ,relwidth= 0.34 ,relheight = 0.07)
		Label(insert_frame ,text = "Blood\nGroup",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",9)).place(relx= 0 ,rely =0.50 ,relwidth= 0.1 ,relheight = 0.1)
		self.blood =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.blood.place(relx= 0.09 ,rely =0.51 ,relwidth= 0.08 ,relheight = 0.07)
		Label(insert_frame ,text = "Gender:",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",10)).place(relx= 0.2 ,rely =0.50 ,relwidth= 0.1 ,relheight = 0.1)
		self.gender= StringVar()
		self.ge = OptionMenu(insert_frame,self.gender,"Male","Female","Others")
		self.ge.place(relx= 0.3 ,rely =0.51 ,relwidth= 0.17 ,relheight = 0.07)
		Label(insert_frame ,text = "Address:",anchor = "nw",justify = "left", fg = "black", bg = "grey", font = ("Arial",10)).place(relx= 0 ,rely =0.60 ,relwidth= 0.1 ,relheight = 0.1)
		self.add =Text(insert_frame, bd= 3)
		self.add.place(relx= 0.01 ,rely =0.66 ,relwidth= 0.48 ,relheight = 0.13)
		Label(insert_frame ,text = "Email:",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",10)).place(relx= 0 ,rely =0.80 ,relwidth= 0.1 ,relheight = 0.1)
		self.email =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.email.place(relx= 0.01 ,rely =0.88 ,relwidth= 0.48 ,relheight = 0.08)
		Label(insert_frame ,text = "DOB:",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",10)).place(relx= 0.52 ,rely =0.09 ,relwidth= 0.1 ,relheight = 0.1)
		self.dob =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.dob.place(relx= 0.6 ,rely =0.1 ,relwidth= 0.23 ,relheight = 0.07)
		db_sel = Button(insert_frame,text = "Select", bg = "gray", bd  =3 ,command = self.sel_date)
		db_sel.place(relx= 0.84 ,rely =0.103 ,relwidth= 0.13 ,relheight = 0.07)
		Label(insert_frame ,text = "Sibling(s)",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",10)).place(relx= 0.52 ,rely =0.19 ,relwidth= 0.15 ,relheight = 0.1)
		self.sibling.set("")
		self.sib = OptionMenu(insert_frame, self.sibling,"No","Yes")
		self.sib.place(relx= 0.65 ,rely =0.2 ,relwidth= 0.11 ,relheight = 0.07) 
		Label(insert_frame ,text = "Mother\nTongue:",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",9)).place(relx= 0.52 ,rely =0.29 ,relwidth= 0.1 ,relheight = 0.1)
		self.mt =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.mt.place(relx= 0.62 ,rely =0.3 ,relwidth= 0.23 ,relheight = 0.07)
		Label(insert_frame ,text = "Hobby(s):",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",10)).place(relx= 0.52 ,rely =0.39 ,relwidth= 0.12 ,relheight = 0.1)
		self.hobby =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.hobby.place(relx= 0.63 ,rely =0.4 ,relwidth= 0.25 ,relheight = 0.07)
		Label(insert_frame ,text = "Guardian's\nOccupation:",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",9)).place(relx= 0.52 ,rely =0.49 ,relwidth= 0.13 ,relheight = 0.1)
		self.go =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.go.place(relx= 0.67 ,rely =0.5 ,relwidth= 0.25 ,relheight = 0.07)
		Label(insert_frame ,text = "New Student ID:",anchor = "w",justify = "left", fg = "black", bg = "grey", font = ("Arial",10)).place(relx= 0.52 ,rely =0.59 ,relwidth= 0.20 ,relheight = 0.1)
		self.stud_id =Entry(insert_frame, font =("arial",10) ,bd = 3)
		self.stud_id.place(relx= 0.52 ,rely =0.67 ,relwidth= 0.25 ,relheight = 0.07)
		Button(insert_frame, text = "Submit",font =("lucida",15), bg = "gray", bd=4, command = self.submit).place(relx= 0.65 ,rely =0.80 ,relwidth= 0.20 ,relheight = 0.1)


	def update_page(self):
		self.superid =0
		update_frame = Frame(self.mf,bg = "pink",borderwidth = 7,relief = GROOVE)
		update_frame.place(relx = 0.015 ,rely =0.02, relheight = 0.96, relwidth = 0.97)
		Label(update_frame,text = "Enter ID of the student to be updated:", bg  = "pink",fg = "red",font = ("arial",13), anchor= "w").place(relx = 0, rely =0.01, relwidth =0.55, relheight =0.08)
		self.stud_id = Entry(update_frame,bd = 4, font =("Arial",13))
		self.stud_id.place(relx = 0.52, rely =0, relwidth =0.2, relheight =0.09)
		Button(update_frame,text ="Get Details", bg ="pink", bd= "4", command = self.setvalues).place(relx = 0.73, rely =0, relwidth =0.2, relheight =0.09)
		Frame(update_frame,bg ="black",bd = 5 ,relief = SUNKEN).place(relx=0, rely=0.1 ,relwidth = 1 ,relheight = 0.01)
		Label(update_frame,text = "Name:", bg  = "pink",fg = "black",font = ("arial",13), anchor= "w").place(relx = 0, rely =0.11, relwidth =0.2, relheight =0.08)
		self.name = Entry(update_frame,bd = 4, font =("arial",9))
		self.name.place(relx = 0.12, rely =0.11, relwidth =0.45, relheight =0.08)
		Label(update_frame,text = "Class:", bg  = "pink",fg = "black",font = ("arial",13), anchor= "w").place(relx = 0.58, rely =0.11, relwidth =0.2, relheight =0.08)
		self.cl = Entry(update_frame,bd = 4, font =("arial",9))
		self.cl.place(relx = 0.68, rely =0.11, relwidth =0.13, relheight =0.08)
		Label(update_frame,text = "DOB:", bg  = "pink",fg = "black",font = ("arial",13), anchor= "w").place(relx = 0, rely =0.21, relwidth =0.1, relheight =0.08)
		self.dob = Entry(update_frame,bd = 4, font =("arial",9))
		self.dob.place(relx = 0.12, rely =0.21, relwidth =0.13, relheight =0.08)
		db_sel = Button(update_frame,text = "Select", bg = "pink", bd  =3 ,command = self.sel_date)
		db_sel.place(relx= 0.26 ,rely =0.21 ,relwidth= 0.13 ,relheight = 0.08)
		Label(update_frame,text = "Blood grp.:", bg  = "pink",fg = "black",font = ("arial",10), anchor= "w").place(relx = 0.4, rely =0.21, relwidth =0.13, relheight =0.08)
		self.blood = Entry(update_frame,bd = 4, font =("arial",9))
		self.blood.place(relx = 0.53, rely =0.21, relwidth =0.1, relheight =0.08)
		Label(update_frame ,text = "Gender:",anchor = "w",justify = "left", fg = "black", bg = "pink", font = ("Arial",10)).place(relx= 0.64 ,rely =0.21 ,relwidth= 0.1 ,relheight = 0.08)
		self.ge = OptionMenu(update_frame,self.gender,"Male","Female","Others")
		self.ge.place(relx= 0.75 ,rely =0.21 ,relwidth= 0.17 ,relheight = 0.08)
		Frame(update_frame,bg ="black").place(relx=0, rely=0.31 ,relwidth = 1 ,relheight = 0.005)
		Label(update_frame,text = "Sibling(s):", bg  = "pink",fg = "black",font = ("arial",10), anchor= "w").place(relx = 0, rely =0.33, relwidth =0.2, relheight =0.08)
		self.sib = OptionMenu(update_frame, self.sibling,"No","Yes")
		self.sib.place(relx= 0.12 ,rely =0.33 ,relwidth= 0.11 ,relheight = 0.08) 
		Label(update_frame,text = "Mother\nTongue:", bg  = "pink",fg = "black",font = ("arial",9), anchor= "w").place(relx = 0.25, rely =0.33, relwidth =0.2, relheight =0.08)
		self.mt = Entry(update_frame,bd = 4, font =("arial",9))
		self.mt.place(relx = 0.35, rely =0.33, relwidth =0.22, relheight =0.08)
		Label(update_frame,text = "Hobby:", bg  = "pink",fg = "black",font = ("arial",10), anchor= "w").place(relx = 0.58, rely =0.33, relwidth =0.15, relheight =0.08)
		self.hobby = Entry(update_frame,bd = 4, font =("arial",9))
		self.hobby.place(relx = 0.67, rely =0.33, relwidth =0.31, relheight =0.08)
		Label(update_frame,text = "Guardian's\nName:", bg  = "pink",fg = "black",font = ("arial",9), anchor= "w").place(relx = 0, rely =0.45, relwidth =0.15, relheight =0.08)
		self.gname = Entry(update_frame,bd = 4, font =("arial",9))
		self.gname.place(relx = 0.12, rely =0.45, relwidth =0.4, relheight =0.08)
		Label(update_frame,text = "Guardian's\nPhone no.:", bg  = "pink",fg = "black",font = ("arial",9), anchor= "w").place(relx = 0.54, rely =0.45, relwidth =0.15, relheight =0.08)
		self.gph = Entry(update_frame,bd = 4, font =("arial",9))
		self.gph.place(relx = 0.67, rely =0.45, relwidth =0.31, relheight =0.08)
		Label(update_frame,text = "Guardian's\nOccupation:", bg  = "pink",fg = "black",font = ("arial",9), anchor= "w").place(relx = 0, rely =0.56, relwidth =0.15, relheight =0.08)
		self.go = Entry(update_frame,bd = 4, font =("arial",9))
		self.go.place(relx = 0.15, rely =0.56, relwidth =0.4, relheight =0.08)
		Frame(update_frame,bg ="black").place(relx=0, rely=0.66 ,relwidth = 1 ,relheight = 0.005)
		Label(update_frame,text = "Address:", bg  = "pink",fg = "black",font = ("arial",10), anchor= "w").place(relx = 0, rely =0.68, relwidth =0.15, relheight =0.08)
		self.add = Text(update_frame,bd = 4)
		self.add.place(relx = 0.12, rely =0.68, relwidth =0.86, relheight =0.14)
		Label(update_frame,text = "Email:", bg  = "pink",fg = "black",font = ("arial",12), anchor= "w").place(relx = 0, rely =0.84, relwidth =0.15, relheight =0.08)
		self.email = Entry(update_frame,bd = 4, font =("arial",9))
		self.email.place(relx = 0.12, rely =0.84, relwidth =0.55, relheight =0.09)
		Button(update_frame,text = "Update Details",bd = 4 ,bg ="pink", font=("arial",14), command = self.update_values).place(relx = 0.70, rely =0.84 ,relwidth = 0.28, relheight=0.11)
	def view_details(self):
		ID = self.getid.get()
		if ID =="":
			tmsg.showinfo("ID Required..","Enter the ID")
			return
		try:
			ID = int(ID)
			mycursor.execute("SELECT * FROM student WHERE id = %s",(ID,))
			result = mycursor.fetchone()
			name =result[0]
			cl =result[1]
			gname = result[2]
			gph =result[3]
			go = result[4]
			blood = result[5]
			add =result[8]
			email  = result[9]
			hobby  = result[10]
			dob =result[11]
			mt = result[12]
			gender = result[6]
			sibling =result[7]
			template = Frame(self.part_frame, bg = "yellow", bd = 5 ,relief = RAISED)
			template.place(relx = 0.05,rely = 0.2, relheight =0.76, relwidth=0.9)	
			piclabel = Label(template,image = self.logo,bg ="black")
			piclabel.place(relx =0.06,rely =0.06, relheight =0.44, relwidth =0.23)
			piclabel.image = self.logo
			Label(template,text =f"Name: {name}",bg = "yellow",font =("lucida",11), anchor ="nw").place(relx =0.3,rely =0.05, relwidth =0.7, relheight =0.08)	
			Label(template,text =f"ID:  {ID}             Class:  {cl}",bg = "yellow",font =("lucida",11), anchor ="nw").place(relx =0.3,rely =0.14, relwidth =0.7, relheight =0.08)
			Label(template,text =f"Guardian: {gname}         Occup: {go}",bg = "yellow",font =("lucida",9), anchor ="nw").place(relx =0.3,rely =0.23, relwidth =0.7, relheight =0.08)	
			Label(template,text =f"Phone no:   {gph}",bg = "yellow",font =("lucida",10), anchor ="nw").place(relx =0.3,rely =0.32, relwidth =0.7, relheight =0.08)
			Label(template,text =f"Mother Tongue:   {mt}",bg = "yellow",font =("lucida",10), anchor ="nw").place(relx =0.3,rely =0.41, relwidth =0.7, relheight =0.08)
			Label(template,text =f"Gender: {gender}       Sibling: {sibling}        Blood Grp: {blood}",bg = "yellow",font =("lucida",10), anchor ="nw").place(relx =0.05,rely =0.50, relwidth =0.7, relheight =0.08)
			Label(template,text =f"Date of birth:   {dob}",bg = "yellow",font =("lucida",10), anchor ="nw").place(relx =0.05,rely =0.59, relwidth =0.7, relheight =0.08)
			Label(template,text =f"Hobby:    {hobby}",bg = "yellow",font =("lucida",10), anchor ="nw").place(relx =0.05,rely =0.68, relwidth =0.7, relheight =0.08)
			Label(template,text =f"Address:    {add} ",bg = "yellow",font =("lucida",10), anchor ="nw").place(relx =0.05,rely =0.77, relwidth =0.9, relheight =0.08)
			Label(template,text =f"Email ID:    {email}",bg = "yellow",font =("lucida",10), anchor ="nw").place(relx =0.05,rely =0.86, relwidth =0.9, relheight =0.08)
		except:
			tmsg.showinfo("Don't Exist!","The ID you entered doesnot exist.")	

	def remove_page(self):
		self.remove_frame = Frame(self.mf,bg = "light blue", borderwidth = 10 ,relief = SUNKEN)
		self.remove_frame.place(relx = 0.015 ,rely =0.02,relheight = 0.96,relwidth =0.97)
		Label(self.remove_frame,text = "(Note: the student details will be permanently removed from dataset)",font = ("arial",10),bg = "light blue",fg = "black", anchor = "w").place(relx = 0.1, rely =0.24 ,relwidth = 0.8, relheight=0.06)
		Label(self.remove_frame,text = "Enter ID of the student to be removed :",font = ("arial",17),bg = "light blue",fg = "red", anchor = "w").place(relx = 0.1, rely =0.3 ,relwidth = 0.8, relheight=0.15)
		self.remid = Entry(self.remove_frame,bd = 4, font =('lucida',15))
		self.remid.place(relx = 0.32,rely =0.44, relheight =0.1, relwidth = 0.2) 
		Button(self.remove_frame,text= "Remove student details", font =("arial",12), bg = "red",fg ="white", bd = 6, command = self.remove_student).place(relx = 0.25,rely =0.6, relheight =0.1, relwidth = 0.34)

	def particular_view(self):
		self.part_frame = Frame(self.mf,bg ="orange", bd= 5 ,relief = GROOVE)
		self.part_frame.place(relx = 0.015 ,rely =0.02, relheight = 0.96, relwidth = 0.97)
		Label(self.part_frame,text = "Enter student ID:",font = ("arial",14),bg = "orange",fg = "black", anchor = "w").place(relx = 0.1, rely =0.05 ,relwidth = 0.8, relheight=0.06)
		self.getid = Entry(self.part_frame,bd = 4, font =('lucida',10))
		self.getid.place(relx = 0.4,rely =0.05, relheight =0.06, relwidth = 0.15) 
		Button(self.part_frame,text = "View",bd ="3", command = self.view_details).place(relx =0.56, rely =0.05, relheight =0.07, relwidth = 0.1)

	def all_view(self):
		all_frame = Frame(self.mf,bg = "light green",borderwidth = 7,relief = RAISED)
		all_frame.place(relx = 0.015 ,rely =0.02, relheight = 0.96, relwidth = 0.97)
		Label(all_frame,text="Filter by class:", bg = "lightgreen", fg = "brown", font =("lucida",15,"italic")).place(relx =0.1, rely = 0.03, relwidth = 0.5, relheight =0.1)
		self.Class.set("all")
		self.cl_op =OptionMenu(all_frame,self.Class,"all","1","2","3","4","5","6","7","8","9","10","11","12")
		self.cl_op.place(relx =0.5, rely = 0.03, relwidth = 0.2, relheight =0.1)
		Button(all_frame,text ="Filter",bd=5, bg="blue",fg ="white", font=("arial",12,"bold"), command = self.place_all).place(relx =0.72, rely = 0.03, relwidth = 0.16, relheight =0.09)
		self.tree = ttk.Treeview(all_frame, selectmode = "browse")
		scrollbary = Scrollbar(all_frame ,bg = "gray" ,orient =VERTICAL)
		scrollbarx = Scrollbar(all_frame, orient = HORIZONTAL)
		self.tree.place(relx =0.02, rely =0.15, relwidth = 0.95,relheight =0.8)
		self.tree.config(yscrollcommand = scrollbary.set)
		self.tree.config(xscrollcommand = scrollbarx.set)
		scrollbary.config(command = self.tree.yview)
		scrollbarx.config(command = self.tree.xview)
		scrollbary.place(relx =0.97,rely =0.16,relheight = 0.80,relwidth =0.03)
		scrollbarx.pack(side = BOTTOM,fill=X,padx = 10)

		self.tree["columns"] = ("id","name","class", "gender","g_name","g_ph","g_o","mt","dob","address","email")
		self.tree["show"] = "headings"
		self.tree.column("id", width = 60, minwidth = 60 ,stretch = NO)
		self.tree.column("name", width = 150)
		self.tree.column("class", width = 50, minwidth = 50 ,stretch = NO)
		self.tree.column("gender", width = 50, minwidth = 50 ,stretch = NO)
		self.tree.column("g_name", width = 150)
		self.tree.column("g_ph", width = 150, minwidth = 100 ,stretch = NO)
		self.tree.column("g_o", width = 150)
		self.tree.column("mt", width = 90, minwidth = 90 ,stretch = NO)
		self.tree.column("dob", width = 90, minwidth = 90 ,stretch = NO)
		self.tree.column("address", width = 250)
		self.tree.column("email", width = 200)

		self.tree.heading("id" ,text = "ID.",anchor = "w")
		self.tree.heading("name" ,text = "Name",anchor = "w")
		self.tree.heading("class" ,text = "Class",anchor = "w")
		self.tree.heading("gender" ,text = "Gender",anchor = "w")
		self.tree.heading("g_name" ,text = "Guardian's Name",anchor = "nw")
		self.tree.heading("g_ph" ,text = "Guardian's Phone No.",anchor = "nw")
		self.tree.heading("g_o" ,text = "Guardian's Occupation",anchor = "nw")
		self.tree.heading("mt" ,text = "Mother Tongue",anchor = "w")
		self.tree.heading("dob" ,text = "Date of Birth",anchor = "w")
		self.tree.heading("address" ,text = "Address",anchor = "w")
		self.tree.heading("email" ,text = "Email",anchor = "w")
		self.place_all()

	def place_all(self):
		tup =[]
		self.tree.delete(*self.tree.get_children())
		if self.Class.get()=="all":
			mycursor.execute("SELECT * from student")
			fetched = mycursor.fetchall()
		else:
			get_class = self.Class.get()
			mycursor.execute("SELECT * from student WHERE class = %s",(int(get_class),))	
			fetched = mycursor.fetchall()
		for z in fetched:
			tup.append((z[13],z[0],z[1],z[6],z[2],z[3],z[4],z[12],z[11],z[8],z[9]))
		index = 0
		for row in tup:
			self.tree.insert("",index,iid=None,values = row)	
			index+=1

root= Tk()
stud = Stdb(root)
root.mainloop()	
