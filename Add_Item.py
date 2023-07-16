from tkinter import StringVar
import sqlite3
from tkinter import messagebox, END
import customtkinter
from PIL import Image,ImageTk #pip intall
import sqlite3
from tkcalendar import Calendar, DateEntry
class itemClass(customtkinter.CTk):


    def __init__(self):
        super().__init__()

        self.geometry("780x600+300+130")
        self.title("GST Management System | Developed By Ruturaj Patil")
        self.focus_force()

        #==============================================================

        self.get_appearance_mode_event()
        self.ik1 = [""]

        self.iuno1var = StringVar()
        self.iuno1var.set("Unit")


        self.addpartleble = customtkinter.CTkLabel(self, text="Add Item",font=customtkinter.CTkFont(size=25))
        self.addpartleble.place(x=320,y=20)

        self.itemname_labl= customtkinter.CTkLabel(self, width=70, height=40, text="Item Name  : ")
        self.itemname_labl.place(x=70, y=100)

        self.itemname_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Item Name")
        self.itemname_entry.place(x=170,y=100)

        self.hsn_labl = customtkinter.CTkLabel(self, width=70, height=40, text="Item HSN  : ")
        self.hsn_labl.place(x=390, y=100)

        self.hsn_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Item HSN")
        self.hsn_entry.place(x=470,y=100)

        # self.unit_entry = customtkinter.CTkButton(self, width=200, height=40, text="Select Unit")
        # self.unit_entry.place(x=510,y=100)

        self.itemcategoryr_labl = customtkinter.CTkLabel(self, width=70, height=40, text="Item Category  : ")
        self.itemcategoryr_labl.place(x=70, y=150)

        self.categoryr_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Category")
        self.categoryr_entry.place(x=170,y=150)

        self.itemcode_labl = customtkinter.CTkLabel(self, width=70, height=40, text="Item Code  : ")
        self.itemcode_labl.place(x=390, y=150)

        self.code_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Item Code")
        self.code_entry.place(x=470,y=150)



        self.savebtn = customtkinter.CTkButton(self, command=self.add_item_event, width=80, text="Save", font=customtkinter.CTkFont(size=16))
        self.savebtn.place(x=680,y=560)

        self.cancelbtn = customtkinter.CTkButton(self, command=self.distoryedityitem, width=80, text="Cancel",
                                                 font=customtkinter.CTkFont(size=16))
        self.cancelbtn.place(x=590, y=560)



        #todo: create tabview
        self.tabview = customtkinter.CTkTabview(self, width=740,height=350)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(200, 0), sticky="nsew")
        self.tabview.add("Pricing")
        self.tabview.add("Stock")
        self.tabview.add("Manufacturing")
        #todo: configure grid of individual tabs
        self.tabview.tab("Pricing").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Stock").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Manufacturing").grid_columnconfigure(0, weight=1)


        #todo: Pricing


        self.Pricing_frame = customtkinter.CTkFrame(self.tabview.tab("Pricing"), width=700,height=200)
        self.Pricing_frame.place(x=15,y=20)

        self.saleprice_lable = customtkinter.CTkLabel(self.Pricing_frame, width=150, height=30,font=customtkinter.CTkFont(size=20), text="Sale Price")
        self.saleprice_lable.place(x=5,y=10)

        self.saleprice_entry = customtkinter.CTkEntry(self.Pricing_frame, width=150, height=40, placeholder_text="Sale Price")
        self.saleprice_entry.place(x=10,y=50)

        self.tax_menu = customtkinter.CTkOptionMenu(self.Pricing_frame,width=120,height=40, dynamic_resizing=False,
                                                        values=["With Tax","Without Tax"])
        self.tax_menu.place(x=165,y=50)

        self.discsaleprice_entry = customtkinter.CTkEntry(self.Pricing_frame, width=150, height=40, placeholder_text="Disc.On Sale Price")
        self.discsaleprice_entry.place(x=300,y=50)

        self.disc_menu = customtkinter.CTkOptionMenu(self.Pricing_frame,width=120,height=40, dynamic_resizing=False,
                                                    values=["Percentage", "Amount"])
        self.disc_menu.place(x=455,y=50)


        self.wholsaleprice_lable = customtkinter.CTkLabel(self.Pricing_frame, width=150, height=30,font=customtkinter.CTkFont(size=20), text="Wholesale Price")
        self.wholsaleprice_lable.place(x=5,y=110)


        self.wholesaleprice_entry = customtkinter.CTkEntry(self.Pricing_frame, width=150, height=40, placeholder_text="Wholesale Price")
        self.wholesaleprice_entry.place(x=10,y=150)

        self.tax_menu1 = customtkinter.CTkOptionMenu(self.Pricing_frame,width=120,height=40, dynamic_resizing=False,
                                                     values=["With Tax","Without Tax"])
        self.tax_menu1.place(x=165,y=150)

        self.minwholqty_entry = customtkinter.CTkEntry(self.Pricing_frame, width=150, height=40, placeholder_text="Minimum Wholesale Qty")
        self.minwholqty_entry.place(x=300,y=150)


        self.Purches_frame = customtkinter.CTkFrame(self.tabview.tab("Pricing"), width=700,height=100)
        self.Purches_frame.place(x=15,y=225)

        self.purchesprice_lable = customtkinter.CTkLabel(self.Purches_frame, width=150, height=20,font=customtkinter.CTkFont(size=20), text="Purchase Price")
        self.purchesprice_lable.place(x=5,y=5)

        self.purchesprice_entry = customtkinter.CTkEntry(self.Purches_frame, width=150, height=40, placeholder_text="Purchase Price")
        self.purchesprice_entry.place(x=10,y=30)

        self.tax_menu3 = customtkinter.CTkOptionMenu(self.Purches_frame,width=120,height=40, dynamic_resizing=False,
                                                     values=["With Tax","Without Tax"])
        self.tax_menu3.place(x=165,y=30)
        self.GSTList =["None", "IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%", "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]

        self.item_tax_label = customtkinter.CTkLabel(self.Purches_frame,width=150,height=30,text="TAX",text_color="black")
        self.item_tax_label.place(x=290,y=30)

        self.item_tax_entry = customtkinter.CTkComboBox(self.Purches_frame,width=150,height=30,values=self.GSTList)
        self.item_tax_entry.place(x=400,y=30)

        #todo: Stock

        self.opingqt_labl = customtkinter.CTkLabel(self.tabview.tab("Stock"), width=70, height=40, text="Opening Quantity  : ")
        self.opingqt_labl.place(x=30, y=30)

        self.opingqty_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, placeholder_text="Opening Quantity")
        self.opingqty_entry.place(x=150,y=30)

        self.atprice_labl = customtkinter.CTkLabel(self.tabview.tab("Stock"), width=70, height=40,
                                                   text="At Price  : ")
        self.atprice_labl.place(x=360, y=30)

        self.atprice_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, placeholder_text="At Price")
        self.atprice_entry.place(x=440,y=30)

        self.date_labl = customtkinter.CTkLabel(self.tabview.tab("Stock"), width=70, height=40,
                                                   text="As of Date  : ")
        self.date_labl.place(x=30, y=80)

        self.date_entry = DateEntry(self.tabview.tab("Stock"), width=10, height=40, placeholder_text="As of Date")
        self.date_entry.place(x=150,y=90)

        self.minstock_labl = customtkinter.CTkLabel(self.tabview.tab("Stock"), width=70, height=40,
                                                text="Min Stock  : ")
        self.minstock_labl.place(x=360, y=80)

        self.minstock_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, placeholder_text="Min Stock To Maintain")
        self.minstock_entry.place(x=440,y=80)

        self.location__labl = customtkinter.CTkLabel(self.tabview.tab("Stock"), width=70, height=40,
                                                text="Location  : ")
        self.location__labl.place(x=30, y=130)

        self.location_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, placeholder_text="Location")
        self.location_entry.place(x=150,y=130)

        self.unit__labl = customtkinter.CTkLabel(self.tabview.tab("Stock"), width=70, height=40,
                                                     text="Unit  : ")
        self.unit__labl.place(x=360, y=130)

        self.unit_entry = customtkinter.CTkComboBox(self.tabview.tab("Stock"), width=200, height=40, variable=self.iuno1var,
                                                        values=self.ik1)
        self.unit_entry.place(x=440,y=130)
        self.iuno1var.trace('w', self.itemunit_update1)

        # self.unit_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, placeholder_text="Unit")
        # self.unit_entry.place(x=440,y=130)

        # self.switch = customtkinter.CTkSwitch(self.tabview.tab("Stock"), text=f"Custom Limit")
        # self.switch.place(x=10,y=90)
        self.get_Unit_combobox()

        #todo: Manufacturing

        self.add1_entry = customtkinter.CTkEntry(self.tabview.tab("Manufacturing"), width=200, height=40, placeholder_text="Manufacturing 1")
        self.add1_entry.place(x=30,y=30)

        self.add2_entry = customtkinter.CTkEntry(self.tabview.tab("Manufacturing"), width=200, height=40, placeholder_text="Manufacturing 2")
        self.add2_entry.place(x=260,y=30)

        self.add3_entry = customtkinter.CTkEntry(self.tabview.tab("Manufacturing"), width=200, height=40, placeholder_text="Manufacturing 3")
        self.add3_entry.place(x=490,y=30)


    def add_item_event(self):
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            if self.itemname_entry.get() == "":
                messagebox.showerror("Error", "Item name must be required!" , parent=self)
            elif self.hsn_entry.get() == "":
                messagebox.showerror("Error", "HSN must be required!" , parent=self)
            elif self.saleprice_entry.get() == "":
                messagebox.showerror("Error", "Sale price must be required!" , parent=self)
            elif self.purchesprice_entry.get() == "":
                messagebox.showerror("Error", "Purches price must be required!" , parent=self)
            elif self.opingqty_entry.get() == "":
                messagebox.showerror("Error", "Oping Qty must be required!" , parent=self)
            else:
                cur.execute("Select * from itemdata where pid=?",(self.hsn_entry.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This GSTIN no. already assigned, try different",parent=self)
                else :
                    cur.execute("Insert into itemdata (pid,itemname,hsn,category,itemcode,saleprice,tax1,discount,dicst,wholesaleprice,tax2,minqty,purchesprice,gsttax,openqty,atprice,date,minstockmanten,location,unit) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.hsn_entry.get(),
                        self.itemname_entry.get(),
                        self.hsn_entry.get(),
                        self.categoryr_entry.get(),
                        self.code_entry.get(),
                        self.saleprice_entry.get(),
                        self.tax_menu.get(),
                        self.discsaleprice_entry.get(),
                        self.disc_menu.get(),
                        self.wholesaleprice_entry.get(),
                        self.tax_menu1.get(),
                        self.minwholqty_entry.get(),
                        self.purchesprice_entry.get(),
                        self.item_tax_entry.get(),
                        self.opingqty_entry.get(),
                        self.atprice_entry.get(),
                        self.date_entry.get(),
                        self.minstock_entry.get(),
                        self.location_entry.get(),
                        self.unit_entry.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Item Added Successfully",parent=self)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self)

    def update(self):
        con=sqlite3.connect(database=r'DataBase/ims.db')
        cur=con.cursor()
        try:
            if self.itemname_entry.get() == "":
                messagebox.showerror("Error", "Item name must be required!", parent=self)
            elif self.hsn_entry.get() == "":
                messagebox.showerror("Error", "HSN must be required!", parent=self)
            elif self.saleprice_entry.get() == "":
                messagebox.showerror("Error", "Sale price must be required!", parent=self)
            elif self.purchesprice_entry.get() == "":
                messagebox.showerror("Error", "Purches price must be required!", parent=self)
            elif self.opingqty_entry.get() == "":
                messagebox.showerror("Error", "Oping Qty must be required!", parent=self)
            else:
                cur.execute("Select * from itemdata where pid=?",(self.hsn_entry.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product HSN",parent=self)
                else :
                    cur.execute("Update itemdata set itemname=?,hsn=?,category=?,itemcode=?,saleprice=?,tax1=?,discount=?,dicst=?,wholesaleprice=?,tax2=?,minqty=?,purchesprice=?,gsttax=?,openqty=?,atprice=?,date=?,minstockmanten=?,location=?,unit=? where pid=?",(

                        self.itemname_entry.get(),
                        self.hsn_entry.get(),
                        self.categoryr_entry.get(),
                        self.code_entry.get(),
                        self.saleprice_entry.get(),
                        self.tax_menu.get(),
                        self.discsaleprice_entry.get(),
                        self.disc_menu.get(),
                        self.wholesaleprice_entry.get(),
                        self.tax_menu1.get(),
                        self.minwholqty_entry.get(),
                        self.purchesprice_entry.get(),
                        self.tax_menu3.get(),
                        self.opingqty_entry.get(),
                        self.atprice_entry.get(),
                        self.date_entry.get(),
                        self.minstock_entry.get(),
                        self.location_entry.get(),
                        self.unit_entry.get(),
                        self.hsn_entry.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Item Updated Successfully",parent=self)

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

    def distoryedityitem(self):
        app.destroy()

    def itemunit_update1(self,event,*args):
        self.update_Unit_combobox(self.unit_entry,self.ik1)

    def update_Unit_combobox(self,entery,list):
        type=entery.get()
        list.clear()
        list.append("")
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select unit from itemdata")
            rows = cur.fetchall()
            for items in rows:
              for i in items:
                m=str(i)
                if type.lower() in m.lower():
                  list.append(i)
            mlis=[*set(list)]
            entery.configure(values=mlis)
            # self.itemshowunit()
        except Exception as ex:
              print("Error", f"Error due to : {str(ex)}")

    def get_Unit_combobox(self):
        self.ik1.clear()
        self.ik1.append("")
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select unit from itemdata")
            rows = cur.fetchall()
            for items in rows:
              for i in items:
                m=str(i)
                self.ik1.append(m)
            mlis=[*set(self.ik1)]
            self.unit_entry.configure(values=mlis)
        except Exception as ex:
              print("Error", f"Error due to : {str(ex)}")




if __name__ == "__main__":
    app = itemClass()
    app.mainloop()