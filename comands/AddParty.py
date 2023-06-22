from tkinter import StringVar
import sqlite3
from tkinter import messagebox, END
import customtkinter
from PIL import Image,ImageTk #pip intall
from tkcalendar import Calendar, DateEntry
import sqlite3
class supplierClass(customtkinter.CTk):


    def __init__(self):
        super().__init__()

        self.geometry("780x600+300+130")
        self.title("GST Management System | Developed By Ruturaj Patil")
        #self.config(bg="white")
        self.focus_force()
        #==============================================================

        self.addpartleble = customtkinter.CTkLabel(self, text="Add Party",font=customtkinter.CTkFont(size=25))
        self.addpartleble.place(x=320,y=40)

        self.partyname_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Party Name")
        self.partyname_entry.place(x=50,y=120)

        self.gstn_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="GSTIN")
        self.gstn_entry.place(x=280,y=120)

        self.number_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Phone Number")
        self.number_entry.place(x=510,y=120)

        self.savebtn = customtkinter.CTkButton(self, command=self.add_party_event, width=80, text="Save", font=customtkinter.CTkFont(size=16))
        self.savebtn.place(x=680,y=560)


        #todo: create tabview
        self.tabview = customtkinter.CTkTabview(self, width=740,height=350)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(200, 0), sticky="nsew")
        self.tabview.add("GST & Address")
        self.tabview.add("Credit & Balance")
        self.tabview.add("Additional Fields")
        #todo: configure grid of individual tabs
        self.tabview.tab("GST & Address").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Credit & Balance").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Additional Fields").grid_columnconfigure(0, weight=1)


        #todo: GST & Address

        self.gsttype_menu = customtkinter.CTkOptionMenu(self.tabview.tab("GST & Address"),width=200,height=40, dynamic_resizing=False,
                                                        values=["Unregistered/Consumer", "Registered Business - Regular", "Registered Business - Composition"])
        self.gsttype_menu.place(x=20,y=30)

        self.state_menu = customtkinter.CTkOptionMenu(self.tabview.tab("GST & Address"),width=200,height=40, dynamic_resizing=False,
                                                        values=["None", "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"])
        self.state_menu.place(x=20,y=100)

        self.email_entry = customtkinter.CTkEntry(self.tabview.tab("GST & Address"), width=200, height=40, placeholder_text="Email ID")
        self.email_entry.place(x=20,y=170)

        self.billingaddress_entry = customtkinter.CTkTextbox(self.tabview.tab("GST & Address"), width=300, height=100)
        self.billingaddress_entry.place(x=410,y=30)

        self.shipingadd_entry = customtkinter.CTkTextbox(self.tabview.tab("GST & Address"), width=300, height=100)
        self.shipingadd_entry.place(x=410,y=150)

        self.billingaddress_lable= customtkinter.CTkLabel(self.tabview.tab("GST & Address"), text="Billing Address : ")
        self.billingaddress_lable.place(x=290,y=30)

        self.shipingaddress_lable= customtkinter.CTkLabel(self.tabview.tab("GST & Address"), text="Shipping Address : ")
        self.shipingaddress_lable.place(x=290,y=150)

        #todo: Credit & Balance

        self.opingbalance_entry = customtkinter.CTkEntry(self.tabview.tab("Credit & Balance"), width=200, height=40, placeholder_text="Pay Balance")
        self.opingbalance_entry.place(x=30,y=30)

        self.recivebalance_entry = customtkinter.CTkEntry(self.tabview.tab("Credit & Balance"), width=200, height=40,
                                                         placeholder_text="Receive Balance")
        self.recivebalance_entry.place(x=260, y=30)

        self.date_entry = DateEntry(self.tabview.tab("Credit & Balance"), width=10, height=40, selectmode="day",date_pattern="dd/mm/y")
        self.date_entry.place(x=120,y=90)

        self.date_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=10, height=40, text="As Of Date")
        self.date_lable.place(x=40, y=80)

        self.customlimit_entry = customtkinter.CTkEntry(self.tabview.tab("Credit & Balance"), width=200, height=40, placeholder_text="Custom Limit")
        self.customlimit_entry.place(x=490,y=30)

        # self.switch = customtkinter.CTkSwitch(self.tabview.tab("Credit & Balance"), text=f"Custom Limit")
        # self.switch.place(x=10,y=90)


        #todo: Credit & Balance

        self.add1_entry = customtkinter.CTkEntry(self.tabview.tab("Additional Fields"), width=200, height=40, placeholder_text="Additional Fields 1")
        self.add1_entry.place(x=30,y=30)

        self.add2_entry = customtkinter.CTkEntry(self.tabview.tab("Additional Fields"), width=200, height=40, placeholder_text="Additional Fields 2")
        self.add2_entry.place(x=260,y=30)

        self.add3_entry = customtkinter.CTkEntry(self.tabview.tab("Additional Fields"), width=200, height=40, placeholder_text="Additional Fields 3")
        self.add3_entry.place(x=490,y=30)

        # def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode("light")


    def add_party_event(self):
        print(self.state_menu.get())
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.gstn_entry.get() == "":
                messagebox.showerror("Error" , "GSTIN must be required" , parent=self)
            else:
                cur.execute("Select * from partydata where pid=?",(self.gstn_entry.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This GSTIN no. already assigned, try different",parent=self)
                else :
                    cur.execute("Insert into partydata (pid,partyname,gstin,phonenumber,gsttype,state,emailid,billaddress,shipaddress,paybalence,recivebalence,date,creditlim,add1,add2,add3,add4) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.gstn_entry.get(),
                        self.partyname_entry.get(),
                        self.gstn_entry.get(),
                        self.number_entry.get(),
                        self.gsttype_menu.get(),
                        self.state_menu.get(),
                        self.email_entry.get(),
                        self.billingaddress_entry.get('1.0',END),
                        self.shipingadd_entry.get('1.0',END),
                        self.opingbalance_entry.get(),
                        self.recivebalance_entry.get(),
                        self.date_entry.get(),
                        self.customlimit_entry.get(),
                        self.add1_entry.get(),
                        self.add2_entry.get(),
                        self.add3_entry.get(),
                        self.add3_entry.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier Addedd Successfully",parent=self)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self)


    def change_appearance_mode_event(self, new_appearance_mode):
       print(new_appearance_mode)





if __name__ == "__main__":
    app = supplierClass()
    app.mainloop()