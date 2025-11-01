from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #first image
        img=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\img1.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        f_labl=Label(self.root,image=self.photoimage)
        f_labl.place(x=0,y=0,width=500,height=130)

        #sec image
        img1=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\img1.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_labl=Label(self.root,image=self.photoimage1)
        f_labl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\img1.jpeg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_labl=Label(self.root,image=self.photoimage2)
        f_labl.place(x=1000,y=0,width=500,height=130)

         #backgroun image
        img3=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\bg11.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\stuimg.jpeg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimage4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",14,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face
        img5=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\scan.webp")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimage5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Detect Face",cursor="hand2",font=("times new roman",14,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #mark attendanec
        img6=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\rec.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimage6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Mark Attendance",cursor="hand2",font=("times new roman",14,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #help button
        img7=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\helpimg.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimage7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",14,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #train data
        img8=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\img2.webp")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimage8,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train tha data",cursor="hand2",font=("times new roman",14,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)

        #phtots
        img9=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\ph.jpeg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimage9,cursor="hand2")
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",14,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)
        
        
        #developer
        img10=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\dev.webp")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimage10,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",14,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)
        
        #exit
        img11=Image.open(r"C:\Users\goyal\Desktop\fase_recognition system\images for\exitimg.png")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimage11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimage11,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",14,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)


        #===============FUNCTIONS BUTTONS=================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)





if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()
