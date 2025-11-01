from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import mysql.connector
import cv2

conn = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Mangement System")

        #==========Variables==========
        self.serchTxt_var=StringVar()
        self.search_var=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar() #for later uses
        self.var_year=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_semester=StringVar()



        #first image
        img=Image.open(r"img1.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        f_labl=Label(self.root,image=self.photoimage)
        f_labl.place(x=0,y=0,width=500,height=130)

        #sec image
        img1=Image.open(r"img1.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_labl=Label(self.root,image=self.photoimage1)
        f_labl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"img1.jpeg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_labl=Label(self.root,image=self.photoimage2)
        f_labl.place(x=1000,y=0,width=500,height=130)

         #backgroun image
        img3=Image.open(r"bg11.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="red",fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=100,width=1500,height=500)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=470)

        #current label frame
        curcourse_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Currrent Course Information",font=("times new roman",12,"bold"))
        curcourse_frame.place(x=10,y=10,width=700,height=120)
        
        #department
        dep_label=Label(curcourse_frame,text="Department",font=("times new roman",12,"bold"),bg='white')
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(curcourse_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Mechanical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label=Label(curcourse_frame,text="Course",font=("times new roman",12,"bold"),bg='white')
        course_label.grid(row=0,column=2)

        course_combo=ttk.Combobox(curcourse_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","SE","FE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10)

        #year
        year_label=Label(curcourse_frame,text="Year",font=("times new roman",12,"bold"),bg='white')
        year_label.grid(row=1,column=0)

        year_combo=ttk.Combobox(curcourse_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)

        #semester
        sem_label=Label(curcourse_frame,text="Semester",font=("times new roman",12,"bold"),bg='white')
        sem_label.grid(row=1,column=2)

        sem_combo=ttk.Combobox(curcourse_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        sem_combo["values"]=("Select Semester","SEM-1","SEM-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10)
        
         #class student info
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=160,width=700,height=280)

        studentid_label=Label(class_student_frame,text="Student ID",font=("times new roman",12,"bold"),bg='white')
        studentid_label.grid(row=0,column=0)

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5)

        #student name
        stname_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg='white')
        stname_label.grid(row=0,column=2,padx=10,pady=5)

        stname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        stname_entry.grid(row=0,column=3,padx=10,pady=5)
        #class division
        class_label=Label(class_student_frame,text="Class Division",font=("times new roman",12,"bold"),bg='white')
        class_label.grid(row=1,column=0,padx=10,pady=5)

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman", 12, "bold"),width=10,state = "readonly")
        div_combo["values"]=("Select Diviosn","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10, pady=5, sticky = W)

        #roll no
        roll_label=Label(class_student_frame,text="Roll no",font=("times new roman",12,"bold"),bg='white')
        roll_label.grid(row=1,column=2,padx=10,pady=5)

        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5)
       
       
       
        #gender
        roll_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg='white')
        roll_label.grid(row=2,column=0,padx=10,pady=5)
        
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman", 12, "bold"),width=13,state = "readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10, pady=5, sticky = W)


        #dob
        roll_label=Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"),bg='white')
        roll_label.grid(row=2,column=2,padx=10,pady=5)

        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=2,column=3,padx=10,pady=5)
        #email
        roll_label=Label(class_student_frame,text="E Mail",font=("times new roman",12,"bold"),bg='white')
        roll_label.grid(row=3,column=0,padx=10,pady=5)

        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=3,column=1,padx=10,pady=5)
        #phoneno
        roll_label=Label(class_student_frame,text="Phone No",font=("times new roman",12,"bold"),bg='white')
        roll_label.grid(row=3,column=2,padx=10,pady=5)

        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=3,column=3,padx=10,pady=5)

        #address
        roll_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg='white')
        roll_label.grid(row=4,column=0,padx=10,pady=5)

        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=4,column=1,padx=10,pady=5)
        #teacher name
        roll_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg='white')
        roll_label.grid(row=4,column=2,padx=10,pady=5)

        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=4,column=3,padx=10,pady=5)

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=6,column=0)
        #hbuttons frame

        
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No Photo Sample", value="No") 
        radionbtn2.grid(row=6,column=1)
        self.var_radio1.set("No")  # Default selection





        
        btn_frame=Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place (x=0,y=200, width=715,height=70)
        
        save_btn=Button(btn_frame, text="Save",width=16, font=("times new roman", 13, "bold"), bg="blue",fg="white",command=self.add_data)
        save_btn.grid(row=0,column=0)

        #up del reset
        save_btn=Button(btn_frame, text="Update",command=self.update_data, width=16, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        save_btn.grid(row=0,column=1)


        save_btn=Button(btn_frame, text="Delete",command=self.delete_Data, width=16, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        save_btn.grid(row=0,column=2)

        save_btn=Button(btn_frame, text="Reset",command=self.reset_data, width=16, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        save_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place (x=0,y=229, width=715,height=70)

        save_btn=Button(btn_frame1, text="Take Photo Sample",command=self.generate_dataset, width=32, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        save_btn.grid(row=1,column=0)

        save_btn=Button(btn_frame1, text="Update Photo Sample", width=32, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        save_btn.grid(row=1,column=1)



        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=740,y=10,width=700,height=470)

         #=======SEARCH SYSTEM=======
        search_frame = LabelFrame(right_frame, relief=RIDGE,text="Search System",font=("times new roman", 12, "bold"),bg="white")
        search_frame.place(x=10,y=10,width=680,height = 120)

        search_label = Label(search_frame, text="Search By:",font=("times new roman", 12, "bold"), fg="red",bg="white")
        search_label.grid(row=0,column=0,padx=3,pady=5, sticky = W)

        search_combo = ttk.Combobox(search_frame,font=("times new roman", 12, "bold"),width=17,state = "readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3, pady=5, sticky = W)

        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman", 12, "bold"))
        search_entry.grid(row=0,column=2,padx=10, pady=5, sticky =W)


        search_btn = Button(search_frame,text="Search",width=10,font=("times new roman", 12, "bold"), fg="white",bg="red")
        search_btn.grid(row=0,column=3,padx=3,pady=4,sticky = W)

        showAll_btn = Button(search_frame,text="Show All",width=10,font=("times new roman", 12, "bold"), fg="white",bg="red")
        showAll_btn.grid(row=0,column=4,padx=3,pady=4,sticky = W)
        
         #table frame
        table_frame = Frame(right_frame,relief=RIDGE)
        table_frame.place(x=5,y=150,width=615,height=250)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","ID","Name","Division","Roll No","Gender","DOB","Email","Phone","Address","Teacher","Photo Sample Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo Sample Status",text="Photo Sample Status")
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    
    #=============Function Declaration==============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO Student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)
    
     #==========Fetch Data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM Student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
     #=============Get Cursor==============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    #Update Function
    def update_data(self): #ERROR
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this data", parent = self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update Student SET Department=%s,Course=%s, Year=%s , Semester=%s, Name=%s , Division=%s, RollNo=%s , Gender=%s , DOB=%s , Email=%s , Phone=%s , Address=%s , Teacher=%s , PhotoSample=%s where ID=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)
       

    #Delete Function
    def delete_Data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="DELETE FROM Student WHERE ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Successfully Deleted",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)

    #Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("") 



    #Take Photo Sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute('''SELECT * FROM Student''')
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update Student SET Department=%s,Course=%s, Year=%s , Semester=%s , Name=%s , Division=%s , RollNo=%s , Gender=%s , DOB=%s , Email=%s , Phone=%s , Address=%s , Teacher=%s , PhotoSampleStatus=%s where ID=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()==id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=======Load predefined data on face frontals from open cv=========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Minimum Neighbour = 5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap= cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450), fx=0.5, fy=0.5)
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root) 
if __name__=="__main__":
    root=Tk()
    obj=Student(root)

    root.mainloop()
