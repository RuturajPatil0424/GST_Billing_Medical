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
        self.addpartleble = customtkinter.CTkLabel(self, text="Edit Item",font=customtkinter.CTkFont(size=25))
        self.addpartleble.place(x=320,y=20)
        self.itemnameVar=StringVar()
        self.itemhsnVar = StringVar()
        self.itemcatVar = StringVar()
        self.itemcodeVar = StringVar()
        self.itemsaleprVar = StringVar()
        self.itemtax1Var = ["With Tax","Without Tax"]
        self.itemdiscountVar = StringVar()
        self.itemdisctVar = ["Percentage", "Amount"]
        self.itemwholesaleVar = StringVar()
        self.itemtax2Var = ["With Tax","Without Tax"]
        self.itemminwtyVar = StringVar()
        self.itempurchaseVar = StringVar()
        self.itemgsttaxVar = StringVar()
        self.itemopenqtyVar = StringVar()
        self.itematpriceVar = StringVar()
        self.itemdateVar = StringVar()
        self.itemminstockVar = StringVar()
        self.itemlocationVar = StringVar()
        self.itemunitVar = StringVar()



        self.itemname_entry = customtkinter.CTkEntry(self, width=200, height=40,textvariable=self.itemnameVar)
        self.itemname_entry.place(x=50,y=100)

        self.hsn_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.itemhsnVar)
        self.hsn_entry.place(x=280,y=100)

        # self.unit_entry = customtkinter.CTkButton(self, width=200, height=40, text="Select Unit")
        # self.unit_entry.place(x=510,y=100)

        self.categoryr_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.itemcatVar)
        self.categoryr_entry.place(x=50,y=150)

        self.code_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.itemcodeVar)
        self.code_entry.place(x=280,y=150)

        self.savebtn = customtkinter.CTkButton(self, command=self.update, width=80, text="Update", font=customtkinter.CTkFont(size=16))
        self.savebtn.place(x=680,y=560)


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

        self.saleprice_entry = customtkinter.CTkEntry(self.Pricing_frame, width=150, height=40, textvariable=self.itemsaleprVar)
        self.saleprice_entry.place(x=10,y=50)

        self.tax_menu = customtkinter.CTkOptionMenu(self.Pricing_frame,width=120,height=40, dynamic_resizing=False,
                                                        values=self.itemtax1Var)
        self.tax_menu.place(x=165,y=50)

        self.discsaleprice_entry = customtkinter.CTkEntry(self.Pricing_frame, width=150, height=40, textvariable=self.itemdiscountVar)
        self.discsaleprice_entry.place(x=300,y=50)

        self.disc_menu = customtkinter.CTkOptionMenu(self.Pricing_frame,width=120,height=40, dynamic_resizing=False,
                                                    values=self.itemdisctVar)
        self.disc_menu.place(x=455,y=50)


        self.wholsaleprice_lable = customtkinter.CTkLabel(self.Pricing_frame, width=150, height=30,font=customtkinter.CTkFont(size=20), text="Wholesale Price")
        self.wholsaleprice_lable.place(x=5,y=110)


        self.wholesaleprice_entry = customtkinter.CTkEntry(self.Pricing_frame, width=150, height=40, textvariable=self.itemwholesaleVar)
        self.wholesaleprice_entry.place(x=10,y=150)

        self.tax_menu1 = customtkinter.CTkOptionMenu(self.Pricing_frame,width=120,height=40, dynamic_resizing=False,
                                                     values=["With Tax","Without Tax"])
        self.tax_menu1.place(x=165,y=150)

        self.minwholqty_entry = customtkinter.CTkEntry(self.Pricing_frame, width=150, height=40, textvariable=self.itemminwtyVar)
        self.minwholqty_entry.place(x=300,y=150)


        self.Purches_frame = customtkinter.CTkFrame(self.tabview.tab("Pricing"), width=700,height=100)
        self.Purches_frame.place(x=15,y=225)

        self.purchesprice_lable = customtkinter.CTkLabel(self.Purches_frame, width=150, height=20,font=customtkinter.CTkFont(size=20), text="Purchase Price")
        self.purchesprice_lable.place(x=5,y=5)

        self.purchesprice_entry = customtkinter.CTkEntry(self.Purches_frame, width=150, height=40, textvariable=self.itempurchaseVar)
        self.purchesprice_entry.place(x=10,y=30)

        self.tax_menu3 = customtkinter.CTkOptionMenu(self.Purches_frame,width=120,height=40, dynamic_resizing=False,
                                                     values=self.itemtax2Var)
        self.tax_menu3.place(x=165,y=30)
        self.GSTList =["None", "IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%", "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]

        self.item_tax_label = customtkinter.CTkLabel(self.Purches_frame,width=150,height=30,text="TAX",text_color="black")
        self.item_tax_label.place(x=290,y=30)

        self.item_tax_entry = customtkinter.CTkComboBox(self.Purches_frame,width=150,height=30,values=self.GSTList)
        self.item_tax_entry.place(x=400,y=30)

        #todo: Stock

        self.opingqty_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, textvariable=self.itemopenqtyVar)
        self.opingqty_entry.place(x=30,y=30)

        self.atprice_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, textvariable=self.itematpriceVar)
        self.atprice_entry.place(x=260,y=30)

        self.date_entry = DateEntry(self.tabview.tab("Stock"), width=10, height=40, textvariable=self.itemdateVar)
        self.date_entry.place(x=490,y=30)

        self.minstock_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, textvariable=self.itemminstockVar)
        self.minstock_entry.place(x=30,y=80)

        self.location_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, textvariable=self.itemlocationVar)
        self.location_entry.place(x=260,y=80)

        self.unit_entry = customtkinter.CTkEntry(self.tabview.tab("Stock"), width=200, height=40, textvariable=self.itemunitVar)
        self.unit_entry.place(x=490,y=80)

        # self.switch = customtkinter.CTkSwitch(self.tabview.tab("Stock"), text=f"Custom Limit")
        # self.switch.place(x=10,y=90)
        self.add_item_event()


        #todo: Manufacturing

        self.add1_entry = customtkinter.CTkEntry(self.tabview.tab("Manufacturing"), width=200, height=40, placeholder_text="Manufacturing 1")
        self.add1_entry.place(x=30,y=30)

        self.add2_entry = customtkinter.CTkEntry(self.tabview.tab("Manufacturing"), width=200, height=40, placeholder_text="Manufacturing 2")
        self.add2_entry.place(x=260,y=30)

        self.add3_entry = customtkinter.CTkEntry(self.tabview.tab("Manufacturing"), width=200, height=40, placeholder_text="Manufacturing 3")
        self.add3_entry.place(x=490,y=30)


    def add_item_event(self):
        itemdatalist=[]
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:

                cur.execute("select pid,itemname,hsn,category,itemcode,saleprice,tax1,discount,dicst,wholesaleprice,tax2,minqty,purchesprice,gsttax,openqty,atprice,date,minstockmanten,location,unit from edititemdata where pid=?",(1,))
                rows = cur.fetchall()
                for row in rows:
                    for r in row:
                      itemdatalist.append(r)

                self.itemnameVar.set(itemdatalist[1])
                self.itemhsnVar.set(itemdatalist[2])
                self.itemcatVar.set(itemdatalist[3])
                self.itemcodeVar.set(itemdatalist[4])
                self.itemsaleprVar.set(itemdatalist[5])
                self.itemtax1Var.insert(0,itemdatalist[6])
                self.itemdiscountVar.set(itemdatalist[7])
                self.itemdisctVar.insert(0,itemdatalist[8])
                self.itemwholesaleVar.set(itemdatalist[9])
                self.itemtax2Var.insert(0,itemdatalist[10])
                self.itemminwtyVar.set(itemdatalist[11])
                self.itempurchaseVar.set(itemdatalist[12])
                self.GSTList.insert(0,itemdatalist[13])
                self.itemopenqtyVar.set(itemdatalist[14])
                self.itematpriceVar.set(itemdatalist[15])
                self.itemdateVar.set(itemdatalist[16])
                self.itemminstockVar.set(itemdatalist[17])
                self.itemlocationVar.set(itemdatalist[18])
                self.itemunitVar.set(itemdatalist[19])

                self.item_tax_entry.configure(values=self.GSTList)

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





if __name__ == "__main__":
    app = itemClass()
    app.mainloop()