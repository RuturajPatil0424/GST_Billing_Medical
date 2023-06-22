from tkinter import*
from PIL import Image,ImageTk #pip intall
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x800+300+130")
        self.root.title("Inventory Management System | Developed By Ruturaj Patil")
        self.root.config(bg="white")
        self.root.focus_force()
        #==============================================================
        #All Variables
        self.var_searchby=StringVar()
        self.Var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.Var_name=StringVar()
        self.Var_contact=StringVar()


        #===title===
        title=Label(self.root,text="Add Party",font=("times new roman",30),bg="#0f4d7d",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=2)
        #Label(self.root,text="Supplier Details",font=("times new roman",20,"bold"),bg="#0f4d7d",fg="white").place(x=100,y=10,width=1400,height=40)

        #===contnt====

        #===row1======
        lbl_sup_invoice=Label(self.root,text="Party Name",font=("times new roman",15),bg="white").place(x=100,y=80)
        txt_sup_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("times new roman",15),bg="lightyellow").place(x=230,y=80,width=180)


        #=====row2====
        lbl_name=Label(self.root,text="GSTIN",font=("times new roman",15),bg="white").place(x=100,y=120)
        txt_name=Entry(self.root,textvariable=self.Var_name,font=("times new roman",15),bg="lightyellow").place(x=230,y=120,width=180)


        #=====row3====
        lbl_contact=Label(self.root,text="Phone Number",font=("times new roman",15),bg="white").place(x=100,y=160)
        txt_contact=Entry(self.root,textvariable=self.Var_contact,font=("times new roman",15),bg="lightyellow").place(x=230,y=160,width=180)


        #=====row4====
        lbl_desc=Label(self.root,text="Description",font=("times new roman",15),bg="white").place(x=100,y=200)
        self.txt_desc=Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.txt_desc.place(x=230,y=200,width=470,height=90)

        #===button===
        btn_add=Button(self.root,text="Save",command=self.add,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2").place(x=230,y=320,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times new roman",15),bg="#4caf50",fg="white",cursor="hand2").place(x=350,y=320,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15),bg="#f44336",fg="white",cursor="hand2").place(x=470,y=320,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15),bg="#607d8b",fg="white",cursor="hand2").place(x=590,y=320,width=110,height=28)

        #====supplier Details===

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=850,y=150,width=550,height=500)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Invoice No.")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")

        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=100)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)

        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
    #============================================================================================================================================

    def add(self):
        con=sqlite3.connect(database=r'../DataBase/ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice no. already assigned, try different",parent=self.root)
                else :
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.Var_name.get(),
                        self.Var_contact.get(),
                        self.txt_desc.get('1.0',END),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier Addedd Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'../DataBase/ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        self.var_sup_invoice.set(row[0]),
        self.Var_name.set(row[1]),
        self.Var_contact.set(row[2]),
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[3]),


    def update(self):
        con=sqlite3.connect(database=r'../DataBase/ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. Must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
                else :
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(

                        self.Var_name.get(),
                        self.Var_contact.get(),
                        self.txt_desc.get('1.0',END),
                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'../DataBase/ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. Must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
                else :
                    op=messagebox.askyesno("Confirm","Do you really wnat to delelte?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_sup_invoice.set(""),
        self.Var_name.set(""),
        self.Var_contact.set(""),
        self.txt_desc.delete('1.0',END),
        self.Var_searchtxt.set(""),
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'../DataBase/ims.db')
        cur=con.cursor()
        try:

            if self.Var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
            else :
                cur.execute("select * from supplier where invoice=?",(+self.Var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()