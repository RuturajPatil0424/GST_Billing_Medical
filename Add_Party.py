from tkinter import messagebox, END
import customtkinter
from tkcalendar import DateEntry
import sqlite3
import re
class supplierClass(customtkinter.CTk):


    def __init__(self):
        super().__init__()

        self.geometry("780x600+300+130")
        self.title("GST Management System | Developed By Ruturaj Patil")
        #self.config(bg="white")
        self.focus_force()
        self.get_appearance_mode_event()
        #==============================================================

        self.addpartleble = customtkinter.CTkLabel(self, text="Add Party",font=customtkinter.CTkFont(size=25))
        self.addpartleble.place(x=320,y=40)

        self.party_name_lable = customtkinter.CTkLabel(self, width=200, height=40, text="Party Name :")
        self.party_name_lable.place(x=0, y=80)

        self.partyname_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Party Name")
        self.partyname_entry.place(x=50,y=120)

        self.party_gstin_lable = customtkinter.CTkLabel(self, width=200, height=40, text="Party GSTIN NO :")
        self.party_gstin_lable.place(x=240, y=80)

        self.party_number_lable = customtkinter.CTkLabel(self, width=200, height=40, text="Party Phone NO :")
        self.party_number_lable.place(x=470, y=80)

        self.gstn_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="GSTIN")
        self.gstn_entry.place(x=280,y=120)

        self.number_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Phone Number")
        self.number_entry.place(x=510,y=120)

        self.savebtn = customtkinter.CTkButton(self, command=self.add_party_event, width=80, text="Save", font=customtkinter.CTkFont(size=16))
        self.savebtn.place(x=680,y=560)

        self.cancelbtn = customtkinter.CTkButton(self, command=self.cancel_party_event, width=80, text="Cancel",
                                               font=customtkinter.CTkFont(size=16))
        self.cancelbtn.place(x=590, y=560)

        self.paybalence=0
        self.recivebalence = 0
        self.customlimit = 0




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

        self.party_entry_lable = customtkinter.CTkLabel(self.tabview.tab("GST & Address"), width=200, height=40,
                                                        text="Email ID :")
        self.party_entry_lable.place(x=0, y=150)

        self.billingaddress_lable = customtkinter.CTkLabel(self.tabview.tab("GST & Address"),
                                                           text="Billing  Address : ")
        self.billingaddress_lable.place(x=290, y=30)

        self.shipingaddress_lable = customtkinter.CTkLabel(self.tabview.tab("GST & Address"),
                                                           text="Shipping  Address : ")
        self.shipingaddress_lable.place(x=290, y=150)



        self.date_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=10, height=40,
                                                 text="As Of Date :")
        self.date_lable.place(x=40, y=100)

        self.email_entry = customtkinter.CTkEntry(self.tabview.tab("GST & Address"), width=200, height=40, placeholder_text="Email ID")
        self.email_entry.place(x=20,y=180)

        self.billingaddress_entry = customtkinter.CTkTextbox(self.tabview.tab("GST & Address"), width=300, height=100)
        self.billingaddress_entry.place(x=410,y=30)

        self.shipingadd_entry = customtkinter.CTkTextbox(self.tabview.tab("GST & Address"), width=300, height=100)
        self.shipingadd_entry.place(x=410,y=150)

        self.billingaddress_lable= customtkinter.CTkLabel(self.tabview.tab("GST & Address"), text="Billing Address : ")
        self.billingaddress_lable.place(x=290,y=30)

        self.shipingaddress_lable= customtkinter.CTkLabel(self.tabview.tab("GST & Address"), text="Shipping Address : ")
        self.shipingaddress_lable.place(x=290,y=150)

        #todo: Credit & Balance

        self.party_opingbalance_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=200,
                                                               height=40,
                                                               text="Pay  Balance :")
        self.party_opingbalance_lable.place(x=0, y=10)

        self.party_recivebalance_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=200,
                                                                height=40,
                                                                text="Receive  Balance :")
        self.party_recivebalance_lable.place(x=240, y=10)

        self.party_customlimit_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=200,
                                                              height=40,
                                                              text="Custom Limit  Balance :")
        self.party_customlimit_lable.place(x=490, y=10)

        self.opingbalance_entry = customtkinter.CTkEntry(self.tabview.tab("Credit & Balance"), width=200, height=40, placeholder_text="Pay Balance")
        self.opingbalance_entry.place(x=30,y=40)

        self.recivebalance_entry = customtkinter.CTkEntry(self.tabview.tab("Credit & Balance"), width=200, height=40,
                                                         placeholder_text="Receive Balance")
        self.recivebalance_entry.place(x=260, y=40)

        self.date_entry = DateEntry(self.tabview.tab("Credit & Balance"), width=10, height=40, selectmode="day",date_pattern="dd/mm/y")
        self.date_entry.place(x=120,y=100)

        self.date_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=10, height=40, text="As Of Date  : ")
        self.date_lable.place(x=40, y=90)

        self.customlimit_entry = customtkinter.CTkEntry(self.tabview.tab("Credit & Balance"), width=200, height=40, placeholder_text="Custom Limit")
        self.customlimit_entry.place(x=490,y=40)

        # self.switch = customtkinter.CTkSwitch(self.tabview.tab("Credit & Balance"), text=f"Custom Limit")
        # self.switch.place(x=10,y=90)


        #todo: Credit & Balance

        self.add1_entry = customtkinter.CTkEntry(self.tabview.tab("Additional Fields"), width=200, height=40, placeholder_text="Additional Fields 1")
        self.add1_entry.place(x=30,y=30)

        self.add2_entry = customtkinter.CTkEntry(self.tabview.tab("Additional Fields"), width=200, height=40, placeholder_text="Additional Fields 2")
        self.add2_entry.place(x=260,y=30)

        self.add3_entry = customtkinter.CTkEntry(self.tabview.tab("Additional Fields"), width=200, height=40, placeholder_text="Additional Fields 3")
        self.add3_entry.place(x=490,y=30)


    def add_party_event(self):
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        gstinnoo=self.gstn_entry.get()
        shipadd=self.shipingadd_entry.get('1.0',END)
        billadd=self.billingaddress_entry.get('1.0',END)

        try:
            if self.partyname_entry.get() == "":
                messagebox.showerror("Error", "Party Name must be required!" , parent=self)
            elif self.gsttype_menu.get() == "Registered Business - Regular" or self.gsttype_menu.get() == "Registered Business - Composition" :
                if gstinnoo == "":
                   messagebox.showerror("Error", "GSTIN must be required!" , parent=self)
                elif len(gstinnoo) != 15:
                   messagebox.showerror("Error", "Please enter valid GSTIN!" , parent=self)
                elif self.validate_gstin(gstinnoo) == False:
                   messagebox.showerror("Error", "Please enter valid GSTIN!", parent=self)
                elif self.number_entry.get() == "":
                   messagebox.showerror("Error", "Phone No. must be required!" , parent=self)
            elif len(self.number_entry.get()) != 10:
                messagebox.showerror("Error", "Please enter valid Phone No.!" , parent=self)
            elif self.state_menu.get() == "None":
                messagebox.showerror("Error", "Please select State!" , parent=self)
            elif self.email_entry.get() != "":
                if self.validate_email(self.email_entry.get()) == False:
                    messagebox.showerror("Error", "Please enter valid Email ID!", parent=self)

            else:
                if self.opingbalance_entry.get() == "":
                    self.paybalence = 0
                else:
                    self.paybalence = self.opingbalance_entry.get()
                if self.recivebalance_entry.get() == "":
                    self.recivebalence = 0
                else:
                    self.recivebalence = self.recivebalance_entry.get()
                if self.customlimit_entry.get() == "":
                    self.customlimit = 0
                else:
                    self.customlimit = self.customlimit_entry.get()
                if self.gstn_entry.get() == "":
                    self.gstinn = "None"
                else:
                    self.gstinn = self.gstn_entry.get()
                cur.execute("Select * from partydata where gstin=?",(self.gstn_entry.get(),))
                row = cur.fetchone()
                # if row != None:
                #     messagebox.showerror("Error","This GSTIN no. already assigned, try different",parent=self)

                cur.execute("Select * from partydata where phonenumber=?", (self.number_entry.get(),))
                rowf = cur.fetchone()
                if rowf != None:
                    messagebox.showerror("Error","This Phone no. already assigned, try different",parent=self)
                cur.execute("Select * from partydata where partyname=?", (self.partyname_entry.get(),))
                rowm = cur.fetchone()
                if rowm != None:
                    messagebox.showerror("Error", "This Party Name is already assigned, try different", parent=self)
                else:

                    cur.execute("Insert into partydata (pid,partyname,gstin,phonenumber,gsttype,state,emailid,billaddress,shipaddress,paybalence,recivebalence,date,creditlim,add1,add2,add3,add4) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.number_entry.get(),
                        self.partyname_entry.get(),
                        self.gstinn,
                        self.number_entry.get(),
                        self.gsttype_menu.get(),
                        self.state_menu.get(),
                        self.email_entry.get(),
                        self.billingaddress_entry.get('1.0',END),
                        self.shipingadd_entry.get('1.0',END),
                        self.paybalence,
                        self.recivebalence,
                        self.date_entry.get(),
                        self.customlimit,
                        self.add1_entry.get(),
                        self.add2_entry.get(),
                        self.add3_entry.get(),
                        self.add3_entry.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Party Added Successfully",parent=self)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self)

    def get_appearance_mode_event(self):
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select theme from appearance where no=1")
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                    customtkinter.set_appearance_mode(r)
            cur.execute("select scelling from appearance where no=1")
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                    new_scaling_float = int(r.replace("%", "")) / 100
                    customtkinter.set_widget_scaling(new_scaling_float)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def validate_email(self,email):
        # Regular expression pattern for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if the email matches the pattern
        if re.match(pattern, email):
            return True
        else:
            return False
    def validate_gstin(self,gstin):
        # Regular expression pattern for GSTIN validation
        pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Za-z]{1}[Z]{1}[0-9A-Z]{1}$'

        # Check if the GSTIN matches the pattern
        if re.match(pattern, gstin):
            return True
        else:
            return False

    def cancel_party_event(self):
        app.destroy()

if __name__ == "__main__":
    app = supplierClass()
    app.mainloop()