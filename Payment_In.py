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
        self.Partynames = [""]
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
        self.pay_amountVar = StringVar()
        self.pay_amountVar.set("0")


        self.get_party_data()
        self.addpartleble = customtkinter.CTkLabel(self, text="Payment In",font=customtkinter.CTkFont(size=25))
        self.addpartleble.place(x=320,y=40)

        self.party_name_lable = customtkinter.CTkLabel(self, width=200, height=40, text="Party Name :")
        self.party_name_lable.place(x=0, y=80)

        self.party_name_entry = customtkinter.CTkComboBox(self, width=200, height=40, variable=self.party_nameVar,
                                                         values=self.Partynames, command=self.party)
        self.party_name_entry.place(x=50, y=120)
        self.party_nameVar.trace('w', self.updateparty)


        self.gstn_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.party_gstinVar,state="readonly")
        self.gstn_entry.place(x=280,y=120)

        self.party_gstin_lable = customtkinter.CTkLabel(self, width=200, height=40, text="Party GSTIN NO :")
        self.party_gstin_lable.place(x=240, y=80)

        self.number_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.party_noVar,state="readonly")
        self.number_entry.place(x=510,y=120)

        self.party_number_lable = customtkinter.CTkLabel(self, width=200, height=40, text="Party Phone NO :")
        self.party_number_lable.place(x=470, y=80)

        self.savebtn = customtkinter.CTkButton(self, command=self.addpayment, width=80, text="Add Payment", font=customtkinter.CTkFont(size=16))
        self.savebtn.place(x=650,y=560)

        self.pay_amount=customtkinter.CTkLabel(self,text="Recived Amount : ")
        self.pay_amount.place(x=60,y=250)

        self.pay_amount_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.pay_amountVar)
        self.pay_amount_entry.place(x=50, y=280)

        self.date_lable = customtkinter.CTkLabel(self, text="Date : ")
        self.date_lable.place(x=280, y=250)

        self.date_entry = DateEntry(self, selectmode="day", date_pattern="dd/mm/y")
        self.date_entry.place(x=320, y=255, width=100)

    def updateparty(self,*args):
        self.Partynames.clear()
        self.Partynames.append("")
        name=self.party_nameVar.get()

        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:

            cur.execute("select partyname from partydata")
            rows = cur.fetchall()

            for row in rows:
                for i in row:

                    m=str(i)
                    if name.lower() in m.lower():

                        self.Partynames.append(i)
            self.party_name_entry.configure(values=self.Partynames)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def party(self,event):
        self.get_party_data()
        self.get_party_number()
        self.get_party_gstin()

    def get_party_number(self):

        if self.party_name_entry.get() == "":
            self.party_noVar.set("")
        else:
            con = sqlite3.connect(database=r'DataBase/ims.db')
            cur = con.cursor()
            try:

                cur.execute("select phonenumber from partydata where partyname=?", (self.party_name_entry.get(),))
                rows = cur.fetchall()
                # self.productTable.delete(*self.productTable.get_children())

                for row in rows:
                    for i in row:
                        self.party_noVar.set(i)


            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def get_party_gstin(self):

        if self.party_name_entry.get() == "":
            self.party_gstinVar.set("")
        else:
         con = sqlite3.connect(database=r'DataBase/ims.db')
         cur = con.cursor()
         try:

            cur.execute("select gstin from partydata where partyname=?", (self.party_name_entry.get(),))
            rows = cur.fetchall()

            for row in rows:
                for i in row:
                    self.party_gstinVar.set(i)


         except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

         # self.get_party_payamount()
         # self.get_party_reciveamount()

    def get_party_data(self):

        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:

            cur.execute("select partyname from partydata")
            rows = cur.fetchall()
            # self.productTable.delete(*self.productTable.get_children())

            for row in rows:
                for i in row:
                    self.Partynames.append(i)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def addpayment(self):
        print("hi")
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