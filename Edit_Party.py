from tkinter import StringVar
from tkinter import messagebox, END
import customtkinter
from tkcalendar import Calendar, DateEntry
import sqlite3
class supplierClass(customtkinter.CTk):


    def __init__(self):
        super().__init__()

        self.geometry("780x600+300+130")
        self.title("GST Management System | Developed By Ruturaj Patil")
        #self.config(bg="white")
        self.focus_force()
        self.get_appearance_mode_event()
        #==============================================================

        self.party_nameVar = StringVar()
        self.party_gstinVar = StringVar()
        self.party_noVar = StringVar()
        self.party_gsttypeVar = ["Unregistered/Consumer", "Registered Business - Regular", "Registered Business - Composition"]
        self.party_steateVar = ["None", "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
        self.party_emailVar = StringVar()
        self.party_payBalanceVar = StringVar()
        self.party_ReceiveVar = StringVar()
        self.party_customlismitVar = StringVar()
        self.party_add1Var = StringVar()
        self.party_add2Var = StringVar()
        self.party_add3Var = StringVar()


        self.addpartleble = customtkinter.CTkLabel(self, text="Edit party_",font=customtkinter.CTkFont(size=25))
        self.addpartleble.place(x=320,y=40)

        self.party_name_lable = customtkinter.CTkLabel(self, width=200, height=40, text="Party Name :")
        self.party_name_lable.place(x=0, y=80)

        self.party_name_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.party_nameVar)
        self.party_name_entry.place(x=50,y=120)

        self.gstn_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.party_gstinVar)
        self.gstn_entry.place(x=280,y=120)

        self.party_gstin_lable = customtkinter.CTkLabel(self, width=200, height=40, text="Party GSTIN NO :")
        self.party_gstin_lable.place(x=240, y=80)

        self.number_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.party_noVar)
        self.number_entry.place(x=510,y=120)

        self.party_number_lable = customtkinter.CTkLabel(self, width=200, height=40, text="Party Phone NO :")
        self.party_number_lable.place(x=470, y=80)

        self.savebtn = customtkinter.CTkButton(self, command=self.add_party__event, width=80, text="Update", font=customtkinter.CTkFont(size=16))
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
                                                        values=self.party_gsttypeVar)
        self.gsttype_menu.place(x=20,y=30)

        self.state_menu = customtkinter.CTkOptionMenu(self.tabview.tab("GST & Address"),width=200,height=40, dynamic_resizing=False,
                                                        values=self.party_steateVar)
        self.state_menu.place(x=20,y=100)

        self.party_entry_lable = customtkinter.CTkLabel(self.tabview.tab("GST & Address"), width=200, height=40, text="Email ID :")
        self.party_entry_lable.place(x=0, y=150)

        self.email_entry = customtkinter.CTkEntry(self.tabview.tab("GST & Address"), width=200, height=40, textvariable=self.party_emailVar)
        self.email_entry.place(x=20,y=185)

        self.billingaddress_entry = customtkinter.CTkTextbox(self.tabview.tab("GST & Address"), width=300, height=100)
        self.billingaddress_entry.place(x=410,y=30)

        self.shipingadd_entry = customtkinter.CTkTextbox(self.tabview.tab("GST & Address"), width=300, height=100)
        self.shipingadd_entry.place(x=410,y=150)

        self.billingaddress_lable= customtkinter.CTkLabel(self.tabview.tab("GST & Address"), text="Billing  Address : ")
        self.billingaddress_lable.place(x=290,y=30)

        self.shipingaddress_lable= customtkinter.CTkLabel(self.tabview.tab("GST & Address"), text="Shipping  Address : ")
        self.shipingaddress_lable.place(x=290,y=150)

        #todo: Credit & Balance

        self.party_opingbalance_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=200, height=40,
                                                        text="Pay  Balance :")
        self.party_opingbalance_lable.place(x=0, y=10)

        self.opingbalance_entry = customtkinter.CTkEntry(self.tabview.tab("Credit & Balance"), width=200, height=40, textvariable=self.party_payBalanceVar)
        self.opingbalance_entry.place(x=30,y=50)

        self.party_recivebalance_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=200,
                                                               height=40,
                                                               text="Recive  Balance :")
        self.party_recivebalance_lable.place(x=240, y=10)

        self.recivebalance_entry = customtkinter.CTkEntry(self.tabview.tab("Credit & Balance"), width=200, height=40,
                                                         textvariable=self.party_ReceiveVar)
        self.recivebalance_entry.place(x=260, y=50)

        self.party_customlimit_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=200,
                                                                height=40,
                                                                text="Custom Limit  Balance :")
        self.party_customlimit_lable.place(x=490, y=10)

        self.date_entry = DateEntry(self.tabview.tab("Credit & Balance"), width=10, height=40, selectmode="day",date_pattern="dd/mm/y")
        self.date_entry.place(x=120,y=110)

        self.date_lable = customtkinter.CTkLabel(self.tabview.tab("Credit & Balance"), width=10, height=40, text="As Of Date :")
        self.date_lable.place(x=40, y=100)

        self.customlimit_entry = customtkinter.CTkEntry(self.tabview.tab("Credit & Balance"), width=200, height=40, textvariable=self.party_customlismitVar)
        self.customlimit_entry.place(x=490,y=50)

        # self.switch = customtkinter.CTkSwitch(self.tabview.tab("Credit & Balance"), text=f"Custom Limit")
        # self.switch.place(x=10,y=90)


        #todo: Credit & Balance

        self.add1_entry = customtkinter.CTkEntry(self.tabview.tab("Additional Fields"), width=200, height=40, textvariable=self.party_add1Var)
        self.add1_entry.place(x=30,y=30)

        self.add2_entry = customtkinter.CTkEntry(self.tabview.tab("Additional Fields"), width=200, height=40, textvariable=self.party_add2Var)
        self.add2_entry.place(x=260,y=30)

        self.add3_entry = customtkinter.CTkEntry(self.tabview.tab("Additional Fields"), width=200, height=40, textvariable=self.party_add3Var)
        self.add3_entry.place(x=490,y=30)

        self.edit_party__event()

    def edit_party__event(self):
        party_datalist=[]
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:

                cur.execute("select pid,partyname,gstin,phonenumber,gsttype,state,emailid,billaddress,shipaddress,paybalence,recivebalence,date,creditlim,add1,add2,add3,add4 from editpartydata where pid=?",(1,))
                rows = cur.fetchall()
                for row in rows:
                    for r in row:
                      party_datalist.append(r)
                      print(r)


                self.party_nameVar.set(party_datalist[1])
                self.party_gstinVar.set(party_datalist[2])
                self.party_noVar.set(party_datalist[3])
                self.party_gsttypeVar.insert(0,party_datalist[4])
                self.gsttype_menu.configure(values=self.party_gsttypeVar)
                self.gsttype_menu.set(party_datalist[4])
                self.party_steateVar.insert(0,party_datalist[5])
                self.state_menu.configure(values=self.party_steateVar)
                self.state_menu.set(party_datalist[5])
                self.party_emailVar.set(party_datalist[6])
                self.billingaddress_entry.insert(0.0,party_datalist[7])
                self.shipingadd_entry.insert(0.0,party_datalist[7])
                self.party_payBalanceVar.set(party_datalist[9])
                self.party_ReceiveVar.set(party_datalist[10])
                self.party_customlismitVar.set(party_datalist[12])
                self.party_add1Var.set(party_datalist[12])
                self.party_add2Var.set(party_datalist[13])
                self.party_add3Var.set(party_datalist[14])


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self)

    def add_party__event(self):
        print(self.state_menu.get())
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        # try:
        if self.gstn_entry.get() == "":
                messagebox.showerror("Error" , "GSTIN must be required" , parent=self)
        else:
                cur.execute("Select * from partydata where gstin=?", (self.gstn_entry.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Party GSTIN", parent=self)
                else :
                    cur.execute(f"Update partydata set partyname=?,gstin=?,phonenumber=?,gsttype=?,state=?,emailid=?,billaddress=?,shipaddress=?,paybalence=?,recivebalence=?,date=?,creditlim=?,add1=?,add2=?,add3=? where gstin={self.gstn_entry.get()}",(

                        self.party_name_entry.get(),
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


                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier Addedd Successfully",parent=self)
        # except Exception as ex:
        #     messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self)

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





if __name__ == "__main__":
    app = supplierClass()
    app.mainloop()