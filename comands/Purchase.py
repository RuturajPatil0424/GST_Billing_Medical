from tkinter import StringVar
import sqlite3
from tkinter import messagebox, END
import customtkinter
from PIL import Image, ImageTk  # pip intall
from tkcalendar import Calendar, DateEntry
import sqlite3
from subprocess import call
class saleClass(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("1920x1080+-10+-3")
        self.title("GST Management System | Developed By Ruturaj Patil")
        # self.config(bg="white")
        self.focus_force()
        # ==============================================================

        self.Partynames = [""]
        self.gstin = StringVar()
        self.partynumber=StringVar()
        self.payamount=StringVar()
        self.reciveamount = StringVar()
        self.resultam = StringVar()


        self.Saleleble = customtkinter.CTkLabel(self, text="Purchase", font=customtkinter.CTkFont(size=25))
        self.Saleleble.place(x=20, y=40)

        self.gstinleble = customtkinter.CTkLabel(self, text="GSTIN : ", font=customtkinter.CTkFont(size=15))
        self.gstinleble.place(x=650, y=125)

        self.gstin_entry = customtkinter.CTkEntry(self, width=150, height=40, textvariable=self.gstin)
        self.gstin_entry.place(x=710, y=120)

        self.phonenumber_entry = customtkinter.CTkEntry(self, width=200, height=40, textvariable=self.partynumber)
        self.phonenumber_entry.place(x=280, y=120)

        self.cash_lable = customtkinter.CTkLabel(self, font=customtkinter.CTkFont(size=15), text="Cash")
        self.cash_lable.place(x=500, y=125)

        self.cash_switch = customtkinter.CTkSwitch(master=self, font=customtkinter.CTkFont(size=15), text="Credit")
        self.cash_switch.place(x=540, y=125)

        self.invocie_lable = customtkinter.CTkLabel(self, text="Invoice No.")
        self.invocie_lable.place(x=900, y=50)

        self.invo=StringVar()
        self.invoice_entry = customtkinter.CTkEntry(self, width=150, height=30,textvariable=self.invo)
        self.invoice_entry.place(x=1000, y=50)

        self.invoice_genrator()

        self.date_label = customtkinter.CTkLabel(self, text="Invoice Date")
        self.date_label.place(x=900, y=90)

        self.date_entry = DateEntry(self,selectmode="day",date_pattern="dd/mm/y")
        self.date_entry.place(x=1000, y=90,width=100)


        self.ste_lable = customtkinter.CTkLabel(self, text="State of Supply")
        self.ste_lable.place(x=900, y=130)

        self.statelist=["None", "Andhra Pradesh", "Arunachal Pradesh", "Assam",
                                                              "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
                                                              "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
                                                              "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
                                                              "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
                                                              "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
                                                              "Uttar Pradesh", "Uttarakhand", "West Bengal"]
        self.state_menu = customtkinter.CTkOptionMenu(self, width=150, height=30, dynamic_resizing=False,
                                                      values=self.statelist)
        self.state_menu.place(x=1000, y=130)

        self.Payment_type_lable = customtkinter.CTkLabel(self, font=customtkinter.CTkFont(size=15), text="Payment Type")
        self.Payment_type_lable.place(x=50, y=720)

        self.Payment_type_entry = customtkinter.CTkComboBox(self, width=100, values=["Cash", "Cheque"],command=self.refrance)
        self.Payment_type_entry.place(x=50, y=750)

        self.Cheque_entry = customtkinter.CTkEntry(self, width=150, height=30, placeholder_text="Reference No.")
        # self.Cheque_entry.place(x=50, y=790)

        self.roundoff_check = customtkinter.CTkCheckBox(self, text="Round off", onvalue=1, offvalue=0,command=self.finalamount)
        self.roundoff_check.place(x=900, y=750)

        self.roundoff=StringVar()
        self.totalam=StringVar()
        self.recvam=StringVar()
        self.recvam.set("0")
        # self.roundoff.set("0")
        # self.totalam.set("0")

        self.roundoff_entry = customtkinter.CTkEntry(self, width=150, height=30, textvariable=self.roundoff)
        self.roundoff_entry.place(x=1000, y=750)
        self.roundoff.trace('w',self.amountupdate)

        self.Total_lable = customtkinter.CTkLabel(self, text="Total")
        self.Total_lable.place(x=900, y=790)

        self.Total_entry = customtkinter.CTkEntry(self, width=150, height=30, textvariable=self.totalam)
        self.Total_entry.place(x=1000, y=790)
        self.totalam.trace('w', self.amountupdate)

        self.Received_lable = customtkinter.CTkLabel(self, text="Received")
        self.Received_lable.place(x=900, y=840)

        self.Received_entry = customtkinter.CTkEntry(self, width=150, height=30, textvariable=self.recvam)
        self.Received_entry.place(x=1000, y=840)
        self.recvam.trace('w', self.amountupdate)

        self.Balance_lable = customtkinter.CTkLabel(self, text="Balance")
        self.Balance_lable.place(x=900, y=880)

        self.balence = StringVar()
        self.balence="0"

        self.Balance_entry = customtkinter.CTkLabel(self, text=self.balence)
        self.Balance_entry.place(x=1070, y=880)

        self.savebtn = customtkinter.CTkButton(self, command=self.savedata, width=80, text="Purchase",
                                               font=customtkinter.CTkFont(size=16))
        self.savebtn.place(x=1100, y=950)

        # self.table_frame = customtkinter.CTkFrame(self,width=1020,height=300 ,corner_radius=0)
        # self.table_frame.place(x=20,y=200)


        TaxList = ["With Tax", "Without Tax"]


        self.navigation_frame = customtkinter.CTkFrame(self, width=1900, height=300, border_width=1, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(11)
        self.navigation_frame.place(x=20, y=200)

        self.no_lable = customtkinter.CTkLabel(self.navigation_frame, text="No.")
        self.no_lable.grid(row=0, column=0, padx=5, pady=5)

        self.no1_lable = customtkinter.CTkLabel(self.navigation_frame, text="1.")
        self.no1_lable.grid(row=2, column=0, padx=5, pady=5)

        self.no2_lable = customtkinter.CTkLabel(self.navigation_frame, text="2.")
        self.no2_lable.grid(row=3, column=0, padx=5, pady=5)

        self.no3_lable = customtkinter.CTkLabel(self.navigation_frame, text="3.")
        self.no3_lable.grid(row=4, column=0, padx=5, pady=5)

        self.no4_lable = customtkinter.CTkLabel(self.navigation_frame, text="4.")
        self.no4_lable.grid(row=5, column=0, padx=5, pady=5)

        self.no5_lable = customtkinter.CTkLabel(self.navigation_frame, text="5.")
        self.no5_lable.grid(row=6, column=0, padx=5, pady=5)

        self.no6_lable = customtkinter.CTkLabel(self.navigation_frame, text="6.")
        self.no6_lable.grid(row=7, column=0, padx=5, pady=5)

        self.no7_lable = customtkinter.CTkLabel(self.navigation_frame, text="7.")
        self.no7_lable.grid(row=8, column=0, padx=5, pady=5)

        self.no8_lable = customtkinter.CTkLabel(self.navigation_frame, text="8.")
        self.no8_lable.grid(row=9, column=0, padx=5, pady=5)

        self.no9_lable = customtkinter.CTkLabel(self.navigation_frame, text="9.")
        self.no9_lable.grid(row=10, column=0, padx=5, pady=5)

        self.no10_lable = customtkinter.CTkLabel(self.navigation_frame, text="10.")
        self.no10_lable.grid(row=11, column=0, padx=5, pady=5)

        self.ItemList = [""]

        self.get_item_name()

        self.Item_lable = customtkinter.CTkLabel(self.navigation_frame, text="ITEM")
        self.Item_lable.grid(row=0, column=1, padx=5, pady=5)

        self.no1var=StringVar()
        self.no2var = StringVar()
        self.no3var = StringVar()
        self.no4var = StringVar()
        self.no5var = StringVar()
        self.no6var = StringVar()
        self.no7var = StringVar()
        self.no8var = StringVar()
        self.no9var = StringVar()
        self.no10var = StringVar()

        self.no1_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no1var, values=list(self.ItemList),command=self.itm1)
        self.no1_item_entry.grid(row=2, column=1, padx=5, pady=5)
        self.no1var.trace('w',self.itemlist_update1)


        self.no2_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no2var, values=self.ItemList,command=self.itm2)
        self.no2_item_entry.grid(row=3, column=1, padx=5, pady=5)
        self.no2var.trace('w', self.itemlist_update2)


        self.no3_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no3var, values=self.ItemList,command=self.itm3)
        self.no3_item_entry.grid(row=4, column=1, padx=5, pady=5)
        self.no3var.trace('w', self.itemlist_update3)

        self.no4_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no4var, values=self.ItemList,command=self.itm4)
        self.no4_item_entry.grid(row=5, column=1, padx=5, pady=5)
        self.no4var.trace('w', self.itemlist_update4)

        self.no5_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no5var, values=self.ItemList,command=self.itm5)
        self.no5_item_entry.grid(row=6, column=1, padx=5, pady=5)
        self.no5var.trace('w', self.itemlist_update5)

        self.no6_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no6var, values=self.ItemList,command=self.itm6)
        self.no6_item_entry.grid(row=7, column=1, padx=5, pady=5)
        self.no6var.trace('w', self.itemlist_update6)

        self.no7_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no7var, values=self.ItemList,command=self.itm7)
        self.no7_item_entry.grid(row=8, column=1, padx=5, pady=5)
        self.no7var.trace('w', self.itemlist_update7)

        self.no8_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no8var, values=self.ItemList,command=self.itm8)
        self.no8_item_entry.grid(row=9, column=1, padx=5, pady=5)
        self.no8var.trace('w', self.itemlist_update8)

        self.no9_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no9var, values=self.ItemList,command=self.itm9)
        self.no9_item_entry.grid(row=10, column=1, padx=5, pady=5)
        self.no9var.trace('w', self.itemlist_update9)

        self.no10_item_entry = customtkinter.CTkComboBox(self.navigation_frame, width=250,variable=self.no10var, values=self.ItemList,command=self.itm10)
        self.no10_item_entry.grid(row=11, column=1, padx=5, pady=5)
        self.no10var.trace('w', self.itemlist_update10)

        self.Total_lable = customtkinter.CTkLabel(self.navigation_frame, text="Total")
        self.Total_lable.grid(row=12, column=1, padx=5, pady=5)

        self.iq1 = StringVar()
        self.iq2 = StringVar()
        self.iq3 = StringVar()
        self.iq4 = StringVar()
        self.iq5 = StringVar()
        self.iq6 = StringVar()
        self.iq7 = StringVar()
        self.iq8 = StringVar()
        self.iq9 = StringVar()
        self.iq10 = StringVar()

        self.iqt()

        self.qty_lable = customtkinter.CTkLabel(self.navigation_frame, text="QTY")
        self.qty_lable.grid(row=0, column=2, padx=5, pady=5)

        self.no1_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq1)
        self.no1_qty_entry.grid(row=2, column=2, padx=5, pady=5)
        self.iq1.trace('w', self.update_qtye1)

        self.no2_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq2)
        self.no2_qty_entry.grid(row=3, column=2, padx=5, pady=5)
        self.iq2.trace('w', self.update_qtye2)

        self.no3_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq3)
        self.no3_qty_entry.grid(row=4, column=2, padx=5, pady=5)
        self.iq3.trace('w', self.update_qtye3)

        self.no4_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq4)
        self.no4_qty_entry.grid(row=5, column=2, padx=5, pady=5)
        self.iq4.trace('w', self.update_qtye4)

        self.no5_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq5)
        self.no5_qty_entry.grid(row=6, column=2, padx=5, pady=5)
        self.iq5.trace('w', self.update_qtye5)

        self.no6_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq6)
        self.no6_qty_entry.grid(row=7, column=2, padx=5, pady=5)
        self.iq6.trace('w', self.update_qtye6)

        self.no7_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq7)
        self.no7_qty_entry.grid(row=8, column=2, padx=5, pady=5)
        self.iq7.trace('w', self.update_qtye7)

        self.no8_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq8)
        self.no8_qty_entry.grid(row=9, column=2, padx=5, pady=5)
        self.iq8.trace('w', self.update_qtye8)

        self.no9_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq9)
        self.no9_qty_entry.grid(row=10, column=2, padx=5, pady=5)
        self.iq9.trace('w', self.update_qtye9)

        self.no10_qty_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iq10)
        self.no10_qty_entry.grid(row=11, column=2, padx=5, pady=5)
        self.iq10.trace('w', self.update_qtye10)

        self.allqty=StringVar()
        self.allqty="0"
        self.Item_unit_List = [""]
        self.get_item_unit_list()

        self.total_qty_lable = customtkinter.CTkLabel(self.navigation_frame, text=self.allqty)
        self.total_qty_lable.grid(row=12, column=2, padx=5, pady=5)

        self.unit_lable = customtkinter.CTkLabel(self.navigation_frame, text="UNIT")
        self.unit_lable.grid(row=0, column=3, padx=5, pady=5)

        self.no1_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no1_unit_entry.grid(row=2, column=3, padx=5, pady=5)

        self.no2_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no2_unit_entry.grid(row=3, column=3, padx=5, pady=5)

        self.no3_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no3_unit_entry.grid(row=4, column=3, padx=5, pady=5)

        self.no4_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no4_unit_entry.grid(row=5, column=3, padx=5, pady=5)

        self.no5_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no5_unit_entry.grid(row=6, column=3, padx=5, pady=5)

        self.no6_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no6_unit_entry.grid(row=7, column=3, padx=5, pady=5)

        self.no7_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no7_unit_entry.grid(row=8, column=3, padx=5, pady=5)

        self.no8_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no8_unit_entry.grid(row=9, column=3, padx=5, pady=5)

        self.no9_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no9_unit_entry.grid(row=10, column=3, padx=5, pady=5)

        self.no10_unit_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.Item_unit_List,command=self.itemshow)
        self.no10_unit_entry.grid(row=11, column=3, padx=5, pady=5)

        self.ip1 = StringVar()
        self.ip2 = StringVar()
        self.ip3 = StringVar()
        self.ip4 = StringVar()
        self.ip5 = StringVar()
        self.ip6 = StringVar()
        self.ip7 = StringVar()
        self.ip8 = StringVar()
        self.ip9 = StringVar()
        self.ip10 = StringVar()

        self.itpri()

        self.unit_lable = customtkinter.CTkLabel(self.navigation_frame, text="PRICE/UNIT")
        self.unit_lable.grid(row=0, column=4, padx=5, pady=5)

        self.tax_unit_box = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=TaxList,command=self.tax)
        self.tax_unit_box.grid(row=1, column=4, padx=5, pady=5)

        self.no1_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip1)
        self.no1_unitprice_entry.grid(row=2, column=4, padx=5, pady=5)
        self.ip1.trace('w',self.itprientery)

        self.no2_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip2)
        self.no2_unitprice_entry.grid(row=3, column=4, padx=5, pady=5)
        self.ip2.trace('w', self.itprientery)

        self.no3_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip3)
        self.no3_unitprice_entry.grid(row=4, column=4, padx=5, pady=5)
        self.ip3.trace('w', self.itprientery)

        self.no4_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip4)
        self.no4_unitprice_entry.grid(row=5, column=4, padx=5, pady=5)
        self.ip4.trace('w', self.itprientery)

        self.no5_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip5)
        self.no5_unitprice_entry.grid(row=6, column=4, padx=5, pady=5)
        self.ip5.trace('w', self.itprientery)

        self.no6_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip6)
        self.no6_unitprice_entry.grid(row=7, column=4, padx=5, pady=5)
        self.ip6.trace('w', self.itprientery)

        self.no7_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip7)
        self.no7_unitprice_entry.grid(row=8, column=4, padx=5, pady=5)
        self.ip7.trace('w', self.itprientery)

        self.no8_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip8)
        self.no8_unitprice_entry.grid(row=9, column=4, padx=5, pady=5)
        self.ip8.trace('w', self.itprientery)

        self.no9_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip9)
        self.no9_unitprice_entry.grid(row=10, column=4, padx=5, pady=5)
        self.ip9.trace('w', self.itprientery)

        self.no10_unitprice_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ip10)
        self.no10_unitprice_entry.grid(row=11, column=4, padx=5, pady=5)
        self.ip10.trace('w', self.itprientery)

        self.DISCOUN_lable = customtkinter.CTkLabel(self.navigation_frame, text="DISCOUNT")
        self.DISCOUN_lable.grid(row=0, column=5, padx=5, pady=5)

        self.percentage_lable = customtkinter.CTkLabel(self.navigation_frame, text="%")
        self.percentage_lable.grid(row=1, column=5, padx=5, pady=5)

        self.Amount_lable = customtkinter.CTkLabel(self.navigation_frame, text="Amount")
        self.Amount_lable.grid(row=1, column=6, padx=5, pady=5)

        self.id1 = StringVar()
        self.id2 = StringVar()
        self.id3 = StringVar()
        self.id4 = StringVar()
        self.id5 = StringVar()
        self.id6 = StringVar()
        self.id7 = StringVar()
        self.id8 = StringVar()
        self.id9 = StringVar()
        self.id10 = StringVar()

        self.secper()
        self.kk=StringVar()
        self.kk="0"

        self.Totaldic_lable = customtkinter.CTkLabel(self.navigation_frame, text=self.kk)
        self.Totaldic_lable.grid(row=12, column=6, padx=5, pady=5)

        self.no1_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.id1)
        self.no1_dec_percentagee_entry.grid(row=2, column=5, padx=5, pady=5)
        self.id1.trace('w', self.itprientery)

        self.no2_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.id2)
        self.no2_dec_percentagee_entry.grid(row=3, column=5, padx=5, pady=5)
        self.id2.trace('w', self.itprientery)

        self.no3_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.id3)
        self.no3_dec_percentagee_entry.grid(row=4, column=5, padx=5, pady=5)
        self.id3.trace('w', self.itprientery)

        self.no4_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.id4)
        self.no4_dec_percentagee_entry.grid(row=5, column=5, padx=5, pady=5)
        self.id4.trace('w', self.itprientery)

        self.no5_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.id5)
        self.no5_dec_percentagee_entry.grid(row=6, column=5, padx=5, pady=5)
        self.id5.trace('w', self.itprientery)

        self.no6_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.id6)
        self.no6_dec_percentagee_entry.grid(row=7, column=5, padx=5, pady=5)
        self.id6.trace('w', self.itprientery)

        self.no7_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.id7)
        self.no7_dec_percentagee_entry.grid(row=8, column=5, padx=5, pady=5)
        self.id7.trace('w', self.itprientery)

        self.no8_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.id8)
        self.no8_dec_percentagee_entry.grid(row=9, column=5, padx=5, pady=5)
        self.id8.trace('w', self.itprientery)

        self.no9_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.id9)
        self.no9_dec_percentagee_entry.grid(row=10, column=5, padx=5, pady=5)
        self.id9.trace('w', self.itprientery)

        self.no10_dec_percentagee_entry = customtkinter.CTkEntry(self.navigation_frame, width=100,
                                                                 textvariable=self.id10)
        self.no10_dec_percentagee_entry.grid(row=11, column=5, padx=5, pady=5)
        self.id10.trace('w', self.itprientery)

        self.ida1 = StringVar()
        self.ida2 = StringVar()
        self.ida3 = StringVar()
        self.ida4 = StringVar()
        self.ida5 = StringVar()
        self.ida6 = StringVar()
        self.ida7 = StringVar()
        self.ida8 = StringVar()
        self.ida9 = StringVar()
        self.ida10 = StringVar()

        self.no1_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida1,state="readonly")
        self.no1_dec_amount_entry.grid(row=2, column=6, padx=5, pady=5)

        self.no2_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida2,state="readonly")
        self.no2_dec_amount_entry.grid(row=3, column=6, padx=5, pady=5)

        self.no3_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida3,state="readonly")
        self.no3_dec_amount_entry.grid(row=4, column=6, padx=5, pady=5)

        self.no4_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida4,state="readonly")
        self.no4_dec_amount_entry.grid(row=5, column=6, padx=5, pady=5)

        self.no5_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida5,state="readonly")
        self.no5_dec_amount_entry.grid(row=6, column=6, padx=5, pady=5)

        self.no6_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida6,state="readonly")
        self.no6_dec_amount_entry.grid(row=7, column=6, padx=5, pady=5)

        self.no7_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida7,state="readonly")
        self.no7_dec_amount_entry.grid(row=8, column=6, padx=5, pady=5)

        self.no8_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida8,state="readonly")
        self.no8_dec_amount_entry.grid(row=9, column=6, padx=5, pady=5)

        self.no9_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida9,state="readonly")
        self.no9_dec_amount_entry.grid(row=10, column=6, padx=5, pady=5)

        self.no10_dec_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ida10,state="readonly")
        self.no10_dec_amount_entry.grid(row=11, column=6, padx=5, pady=5)


        self.DISCOUN_lable = customtkinter.CTkLabel(self.navigation_frame, text="TAX")
        self.DISCOUN_lable.grid(row=0, column=7, padx=5, pady=5)

        self.percentage_lable = customtkinter.CTkLabel(self.navigation_frame, text="%")
        self.percentage_lable.grid(row=1, column=7, padx=5, pady=5)

        self.Amount_lable = customtkinter.CTkLabel(self.navigation_frame, text="Amount")
        self.Amount_lable.grid(row=1, column=8, padx=5, pady=5)

        self.itax1 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                      "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]
        self.itax2 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                      "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]
        self.itax3 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                      "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]
        self.itax4 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                      "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]
        self.itax5 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                      "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]
        self.itax6 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                      "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]
        self.itax7 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                      "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]
        self.itax8 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                      "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]
        self.itax9 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                      "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]
        self.itax10 = ["IGST@0%", "GST@0%", "IGST@0.25%", "GST@0.25%", "IGST@3%", "GST@3%", "IGST@5%", "GST@5%",
                       "IGST@12%", "GST@12%", "IGST@18%", "GST@18%", "IGST@28%", "GST@28%", "EXEMPTED"]

        self.itx()
        self.diccc=StringVar()
        self.diccc="0"

        self.no1_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.itax1,command=self.tax)
        self.no1_tax_percentagee_entry.grid(row=2, column=7, padx=5, pady=5)

        self.no2_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.itax2,command=self.tax)
        self.no2_tax_percentagee_entry.grid(row=3, column=7, padx=5, pady=5)

        self.no3_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.itax3,command=self.tax)
        self.no3_tax_percentagee_entry.grid(row=4, column=7, padx=5, pady=5)

        self.no4_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.itax4,command=self.tax)
        self.no4_tax_percentagee_entry.grid(row=5, column=7, padx=5, pady=5)

        self.no5_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.itax5,command=self.tax)
        self.no5_tax_percentagee_entry.grid(row=6, column=7, padx=5, pady=5)

        self.no6_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.itax6,command=self.tax)
        self.no6_tax_percentagee_entry.grid(row=7, column=7, padx=5, pady=5)

        self.no7_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.itax7,command=self.tax)
        self.no7_tax_percentagee_entry.grid(row=8, column=7, padx=5, pady=5)

        self.no8_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.itax8,command=self.tax)
        self.no8_tax_percentagee_entry.grid(row=9, column=7, padx=5, pady=5)

        self.no9_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100, values=self.itax9,command=self.tax)
        self.no9_tax_percentagee_entry.grid(row=10, column=7, padx=5, pady=5)

        self.no10_tax_percentagee_entry = customtkinter.CTkComboBox(self.navigation_frame, width=100,values=self.itax10,command=self.tax)
        self.no10_tax_percentagee_entry.grid(row=11, column=7, padx=5, pady=5)

        self.ita1 = StringVar()
        self.ita2 = StringVar()
        self.ita3 = StringVar()
        self.ita4 = StringVar()
        self.ita5 = StringVar()
        self.ita6 = StringVar()
        self.ita7 = StringVar()
        self.ita8 = StringVar()
        self.ita9 = StringVar()
        self.ita10 = StringVar()

        self.no1_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita1)
        self.no1_tax_amount_entry.grid(row=2, column=8, padx=5, pady=5)

        self.no2_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita2)
        self.no2_tax_amount_entry.grid(row=3, column=8, padx=5, pady=5)

        self.no3_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita3)
        self.no3_tax_amount_entry.grid(row=4, column=8, padx=5, pady=5)

        self.no4_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita4)
        self.no4_tax_amount_entry.grid(row=5, column=8, padx=5, pady=5)

        self.no5_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita5)
        self.no5_tax_amount_entry.grid(row=6, column=8, padx=5, pady=5)

        self.no6_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita6)
        self.no6_tax_amount_entry.grid(row=7, column=8, padx=5, pady=5)

        self.no7_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita7)
        self.no7_tax_amount_entry.grid(row=8, column=8, padx=5, pady=5)

        self.no8_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita8)
        self.no8_tax_amount_entry.grid(row=9, column=8, padx=5, pady=5)

        self.no9_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita9)
        self.no9_tax_amount_entry.grid(row=10, column=8, padx=5, pady=5)

        self.no10_tax_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.ita10)
        self.no10_tax_amount_entry.grid(row=11, column=8, padx=5, pady=5)

        self.Totaltax_lable = customtkinter.CTkLabel(self.navigation_frame, text=self.diccc)
        self.Totaltax_lable.grid(row=12, column=8, padx=5, pady=5)

        self.iam1 = StringVar()
        self.iam2 = StringVar()
        self.iam3 = StringVar()
        self.iam4 = StringVar()
        self.iam5 = StringVar()
        self.iam6 = StringVar()
        self.iam7 = StringVar()
        self.iam8 = StringVar()
        self.iam9 = StringVar()
        self.iam10 = StringVar()

        self.iam1.set("0")
        self.iam2.set("0")
        self.iam3.set("0")
        self.iam4.set("0")
        self.iam5.set("0")
        self.iam6.set("0")
        self.iam7.set("0")
        self.iam8.set("0")
        self.iam9.set("0")
        self.iam10.set("0")

        self.Amount_lable = customtkinter.CTkLabel(self.navigation_frame, text="Amount")
        self.Amount_lable.grid(row=0, column=9, padx=5, pady=5)

        self.no1_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam1)
        self.no1_amount_entry.grid(row=2, column=9, padx=5, pady=5)

        self.no2_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam2)
        self.no2_amount_entry.grid(row=3, column=9, padx=5, pady=5)

        self.no3_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam3)
        self.no3_amount_entry.grid(row=4, column=9, padx=5, pady=5)

        self.no4_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam4)
        self.no4_amount_entry.grid(row=5, column=9, padx=5, pady=5)

        self.no5_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam5)
        self.no5_amount_entry.grid(row=6, column=9, padx=5, pady=5)

        self.no6_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam6)
        self.no6_amount_entry.grid(row=7, column=9, padx=5, pady=5)

        self.no7_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam7)
        self.no7_amount_entry.grid(row=8, column=9, padx=5, pady=5)

        self.no8_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam8)
        self.no8_amount_entry.grid(row=9, column=9, padx=5, pady=5)

        self.no9_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam9)
        self.no9_amount_entry.grid(row=10, column=9, padx=5, pady=5)

        self.no10_amount_entry = customtkinter.CTkEntry(self.navigation_frame, width=100, textvariable=self.iam10)
        self.no10_amount_entry.grid(row=11, column=9, padx=5, pady=5)

        self.fi=StringVar()
        self.fi="0"

        self.Total_amount_lable = customtkinter.CTkLabel(self.navigation_frame, text=self.fi)
        self.Total_amount_lable.grid(row=12, column=9, padx=5, pady=5)

        self.get_party_data()

        self.Party_var=StringVar()
        self.partyname_entry = customtkinter.CTkComboBox(self, width=200, height=40, variable=self.Party_var,values=self.Partynames,command=self.party)
        self.partyname_entry.place(x=50, y=120)
        self.Party_var.trace('w',self.updateparty)

        self.get_party_gstin()
        self.get_party_number()


        # def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode("light")

    def add_party_event(self):
        self.get_party_gstin()
        self.get_amount()

        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:
            if self.partyname_entry.get() == "":
                print("Party Name must be required")
            elif self.partynumber.get() == "":
                print("Phone No must be required")
            elif self.gstin.get() == "":
                print("GST No must be required")
            elif self.invoice_entry.get() == "":
                print("Invoice No must be required")
            elif self.state_menu.get() == "None":
                print("Please select state!")
            elif self.no1_item_entry.get() == "None":
                print("Please select at list one item!")
            else:
                cur.execute("Select * from gstpurchase")

                if self.cash_switch.get() == 1:
                    crstete = "Credit"
                else:
                    crstete = "Cash"
                cur.execute("Insert into gstpurchase (partyname,phonenumber,gstin,cashorcr,invoiceno,invoicedate,steteofsuply,paymentype,refreceno,total,received,balance,item1name,qty1,unit1,unitprice1,dec1,desamount1,tax1,gstamount1,amount1,item2name,qty2,unit2,unitprice2,dec2,desamount2,tax2,gstamount2,amount2,item3name,qty3,unit3,unitprice3,dec3,desamount3,tax3,gstamount3,amount3,item4name,qty4,unit4,unitprice4,dec4,desamount4,tax4,gstamount4,amount4,item5name,qty5,unit5,unitprice5,dec5,desamount5,tax5,gstamount5,amount5,item6name,qty6,unit6,unitprice6,dec6,desamount6,tax6,gstamount6,amount6,item7name,qty7,unit7,unitprice7,dec7,desamount7,tax7,gstamount7,amount7,item8name,qty8,unit8,unitprice8,dec8,desamount8,tax8,gstamount8,amount8,item9name,qty9,unit9,unitprice9,dec9,desamount9,tax9,gstamount9,amount9,item10name,qty10,unit10,unitprice10,dec10,desamount10,tax10,gstamount10,amount10) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (

                        self.partyname_entry.get(),
                        self.phonenumber_entry.get(),
                        self.gstin_entry.get(),
                        crstete,
                        self.invoice_entry.get(),
                        self.date_entry.get(),
                        self.state_menu.get(),
                        self.Payment_type_entry.get(),
                        self.Cheque_entry.get(),
                        self.Total_entry.get(),
                        self.Received_entry.get(),
                        self.balence,

                        self.no1_item_entry.get(),
                        self.no1_qty_entry.get(),
                        self.no1_unit_entry.get(),
                        self.no1_unitprice_entry.get(),
                        self.no1_dec_percentagee_entry.get(),
                        self.no1_dec_amount_entry.get(),
                        self.no1_tax_percentagee_entry.get(),
                        self.no1_tax_amount_entry.get(),
                        self.no1_amount_entry.get(),

                        self.no2_item_entry.get(),
                        self.no2_qty_entry.get(),
                        self.no2_unit_entry.get(),
                        self.no2_unitprice_entry.get(),
                        self.no2_dec_percentagee_entry.get(),
                        self.no2_dec_amount_entry.get(),
                        self.no2_tax_percentagee_entry.get(),
                        self.no2_tax_amount_entry.get(),
                        self.no2_amount_entry.get(),

                        self.no3_item_entry.get(),
                        self.no3_qty_entry.get(),
                        self.no3_unit_entry.get(),
                        self.no3_unitprice_entry.get(),
                        self.no3_dec_percentagee_entry.get(),
                        self.no3_dec_amount_entry.get(),
                        self.no3_tax_percentagee_entry.get(),
                        self.no3_tax_amount_entry.get(),
                        self.no3_amount_entry.get(),

                        self.no4_item_entry.get(),
                        self.no4_qty_entry.get(),
                        self.no4_unit_entry.get(),
                        self.no4_unitprice_entry.get(),
                        self.no4_dec_percentagee_entry.get(),
                        self.no4_dec_amount_entry.get(),
                        self.no4_tax_percentagee_entry.get(),
                        self.no4_tax_amount_entry.get(),
                        self.no4_amount_entry.get(),

                        self.no5_item_entry.get(),
                        self.no5_qty_entry.get(),
                        self.no5_unit_entry.get(),
                        self.no5_unitprice_entry.get(),
                        self.no5_dec_percentagee_entry.get(),
                        self.no5_dec_amount_entry.get(),
                        self.no5_tax_percentagee_entry.get(),
                        self.no5_tax_amount_entry.get(),
                        self.no5_amount_entry.get(),

                        self.no6_item_entry.get(),
                        self.no6_qty_entry.get(),
                        self.no6_unit_entry.get(),
                        self.no6_unitprice_entry.get(),
                        self.no6_dec_percentagee_entry.get(),
                        self.no6_dec_amount_entry.get(),
                        self.no6_tax_percentagee_entry.get(),
                        self.no6_tax_amount_entry.get(),
                        self.no6_amount_entry.get(),

                        self.no7_item_entry.get(),
                        self.no7_qty_entry.get(),
                        self.no7_unit_entry.get(),
                        self.no7_unitprice_entry.get(),
                        self.no7_dec_percentagee_entry.get(),
                        self.no7_dec_amount_entry.get(),
                        self.no7_tax_percentagee_entry.get(),
                        self.no7_tax_amount_entry.get(),
                        self.no7_amount_entry.get(),

                        self.no8_item_entry.get(),
                        self.no8_qty_entry.get(),
                        self.no8_unit_entry.get(),
                        self.no8_unitprice_entry.get(),
                        self.no8_dec_percentagee_entry.get(),
                        self.no8_dec_amount_entry.get(),
                        self.no8_tax_percentagee_entry.get(),
                        self.no8_tax_amount_entry.get(),
                        self.no8_amount_entry.get(),

                        self.no9_item_entry.get(),
                        self.no9_qty_entry.get(),
                        self.no9_unit_entry.get(),
                        self.no9_unitprice_entry.get(),
                        self.no9_dec_percentagee_entry.get(),
                        self.no9_dec_amount_entry.get(),
                        self.no9_tax_percentagee_entry.get(),
                        self.no9_tax_amount_entry.get(),
                        self.no9_amount_entry.get(),

                        self.no10_item_entry.get(),
                        self.no10_qty_entry.get(),
                        self.no10_unit_entry.get(),
                        self.no10_unitprice_entry.get(),
                        self.no10_dec_percentagee_entry.get(),
                        self.no10_dec_amount_entry.get(),
                        self.no10_tax_percentagee_entry.get(),
                        self.no10_tax_amount_entry.get(),
                        self.no10_amount_entry.get(),

                    ))
                con.commit()
                messagebox.showinfo("Success", "supplier Addedd Successfully", parent=self)
                self.add_amount()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def add_amount(self):
     pay=float(self.resultam.get())
     rwsult=pay

     try:
        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()

        cur.execute(f"Select paybalence from partydata where pid={self.gstin_entry.get()}")
        cur.execute(f"Update partydata set paybalence=? where pid={self.gstin_entry.get()}",(
             rwsult,
            ))
        con.commit()


     except Exception as ex:
      print(ex)


    def add_invoice_event(self):
        self.get_party_gstin()

        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:
            if self.partyname_entry.get() == "":
                messagebox.showerror("Error", "Party Name must be required", parent=self)
            elif self.partynumber.get() == "":
                messagebox.showerror("Error", "Phone No must be required", parent=self)
            elif self.gstin.get() == "":
                messagebox.showerror("Error", "GST No must be required", parent=self)
            elif self.invoice_entry.get() == "":
                messagebox.showerror("Error", "Invoice No must be required", parent=self)
            elif self.state_menu.get() == "None":
                messagebox.showerror("Error", "Please select state!", parent=self)
            elif self.no1_item_entry.get() == "None":
                messagebox.showerror("Error", "Please select at list one item!", parent=self)
            else:
                cur.execute("Select * from invopurchasesale where sid=1")

                if self.cash_switch.get() == 1:
                    crstete = "Credit"
                else:
                    crstete = "Cash"
                cur.execute(
                    "Update invopurchasesale set partyname=?,phonenumber=?,gstin=?,cashorcr=?,invoiceno=?,invoicedate=?,steteofsuply=?,paymentype=?,refreceno=?,total=?,received=?,balance=?,totaltac=?,totaldec=?,totalqty=?,item1name=?,qty1=?,unit1=?,unitprice1=?,dec1=?,desamount1=?,tax1=?,gstamount1=?,amount1=?,item2name=?,qty2=?,unit2=?,unitprice2=?,dec2=?,desamount2=?,tax2=?,gstamount2=?,amount2=?,item3name=?,qty3=?,unit3=?,unitprice3=?,dec3=?,desamount3=?,tax3=?,gstamount3=?,amount3=?,item4name=?,qty4=?,unit4=?,unitprice4=?,dec4=?,desamount4=?,tax4=?,gstamount4=?,amount4=?,item5name=?,qty5=?,unit5=?,unitprice5=?,dec5=?,desamount5=?,tax5=?,gstamount5=?,amount5=?,item6name=?,qty6=?,unit6=?,unitprice6=?,dec6=?,desamount6=?,tax6=?,gstamount6=?,amount6=?,item7name=?,qty7=?,unit7=?,unitprice7=?,dec7=?,desamount7=?,tax7=?,gstamount7=?,amount7=?,item8name=?,qty8=?,unit8=?,unitprice8=?,dec8=?,desamount8=?,tax8=?,gstamount8=?,amount8=?,item9name=?,qty9=?,unit9=?,unitprice9=?,dec9=?,desamount9=?,tax9=?,gstamount9=?,amount9=?,item10name=?,qty10=?,unit10=?,unitprice10=?,dec10=?,desamount10=?,tax10=?,gstamount10=?,amount10=?",
                    (

                        self.partyname_entry.get(),
                        self.phonenumber_entry.get(),
                        self.gstin_entry.get(),
                        crstete,
                        self.invoice_entry.get(),
                        self.date_entry.get(),
                        self.state_menu.get(),
                        self.Payment_type_entry.get(),
                        self.Cheque_entry.get(),
                        self.Total_entry.get(),
                        self.Received_entry.get(),
                        self.balence,
                        self.diccc,
                        self.kk,
                        self.allqty,

                        self.no1_item_entry.get(),
                        self.no1_qty_entry.get(),
                        self.no1_unit_entry.get(),
                        self.no1_unitprice_entry.get(),
                        self.no1_dec_percentagee_entry.get(),
                        self.no1_dec_amount_entry.get(),
                        self.no1_tax_percentagee_entry.get(),
                        self.no1_tax_amount_entry.get(),
                        self.no1_amount_entry.get(),

                        self.no2_item_entry.get(),
                        self.no2_qty_entry.get(),
                        self.no2_unit_entry.get(),
                        self.no2_unitprice_entry.get(),
                        self.no2_dec_percentagee_entry.get(),
                        self.no2_dec_amount_entry.get(),
                        self.no2_tax_percentagee_entry.get(),
                        self.no2_tax_amount_entry.get(),
                        self.no2_amount_entry.get(),

                        self.no3_item_entry.get(),
                        self.no3_qty_entry.get(),
                        self.no3_unit_entry.get(),
                        self.no3_unitprice_entry.get(),
                        self.no3_dec_percentagee_entry.get(),
                        self.no3_dec_amount_entry.get(),
                        self.no3_tax_percentagee_entry.get(),
                        self.no3_tax_amount_entry.get(),
                        self.no3_amount_entry.get(),

                        self.no4_item_entry.get(),
                        self.no4_qty_entry.get(),
                        self.no4_unit_entry.get(),
                        self.no4_unitprice_entry.get(),
                        self.no4_dec_percentagee_entry.get(),
                        self.no4_dec_amount_entry.get(),
                        self.no4_tax_percentagee_entry.get(),
                        self.no4_tax_amount_entry.get(),
                        self.no4_amount_entry.get(),

                        self.no5_item_entry.get(),
                        self.no5_qty_entry.get(),
                        self.no5_unit_entry.get(),
                        self.no5_unitprice_entry.get(),
                        self.no5_dec_percentagee_entry.get(),
                        self.no5_dec_amount_entry.get(),
                        self.no5_tax_percentagee_entry.get(),
                        self.no5_tax_amount_entry.get(),
                        self.no5_amount_entry.get(),

                        self.no6_item_entry.get(),
                        self.no6_qty_entry.get(),
                        self.no6_unit_entry.get(),
                        self.no6_unitprice_entry.get(),
                        self.no6_dec_percentagee_entry.get(),
                        self.no6_dec_amount_entry.get(),
                        self.no6_tax_percentagee_entry.get(),
                        self.no6_tax_amount_entry.get(),
                        self.no6_amount_entry.get(),

                        self.no7_item_entry.get(),
                        self.no7_qty_entry.get(),
                        self.no7_unit_entry.get(),
                        self.no7_unitprice_entry.get(),
                        self.no7_dec_percentagee_entry.get(),
                        self.no7_dec_amount_entry.get(),
                        self.no7_tax_percentagee_entry.get(),
                        self.no7_tax_amount_entry.get(),
                        self.no7_amount_entry.get(),

                        self.no8_item_entry.get(),
                        self.no8_qty_entry.get(),
                        self.no8_unit_entry.get(),
                        self.no8_unitprice_entry.get(),
                        self.no8_dec_percentagee_entry.get(),
                        self.no8_dec_amount_entry.get(),
                        self.no8_tax_percentagee_entry.get(),
                        self.no8_tax_amount_entry.get(),
                        self.no8_amount_entry.get(),

                        self.no9_item_entry.get(),
                        self.no9_qty_entry.get(),
                        self.no9_unit_entry.get(),
                        self.no9_unitprice_entry.get(),
                        self.no9_dec_percentagee_entry.get(),
                        self.no9_dec_amount_entry.get(),
                        self.no9_tax_percentagee_entry.get(),
                        self.no9_tax_amount_entry.get(),
                        self.no9_amount_entry.get(),

                        self.no10_item_entry.get(),
                        self.no10_qty_entry.get(),
                        self.no10_unit_entry.get(),
                        self.no10_unitprice_entry.get(),
                        self.no10_dec_percentagee_entry.get(),
                        self.no10_dec_amount_entry.get(),
                        self.no10_tax_percentagee_entry.get(),
                        self.no10_tax_amount_entry.get(),
                        self.no10_amount_entry.get(),

                    ))
                con.commit()
                self.update_iqt()
                self.invoice_genrator()


        except Exception as ex:
            print(ex)
            # messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def invoice_event(self):
        call(["python", "purachseinvo.py"])
    def savedata(self):
        self.add_invoice_event()
        self.invoice_updator()
        self.add_party_event()
        self.invoice_event()


    def change_appearance_mode_event(self, new_appearance_mode):
        print(new_appearance_mode)

    def get_party_data(self):

        con = sqlite3.connect(database=r'../DataBase/ims.db')
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

    def get_party_gstin(self):

        if self.partyname_entry.get() == "":
            self.gstin.set("")
        else:
         con = sqlite3.connect(database=r'../DataBase/ims.db')
         cur = con.cursor()
         try:

            cur.execute("select gstin from partydata where partyname=?", (self.partyname_entry.get(),))
            rows = cur.fetchall()

            for row in rows:
                for i in row:
                    self.gstin.set(i)


         except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

         self.get_party_payamount()
         self.get_party_reciveamount()

    def get_party_state(self):

        if self.partyname_entry.get() == "":
            self.state_menu.set("None")
        else:
         con = sqlite3.connect(database=r'../DataBase/ims.db')
         cur = con.cursor()
         try:

            cur.execute("select state from partydata where partyname=?", (self.partyname_entry.get(),))
            rows = cur.fetchall()

            for row in rows:
                for i in row:
                    self.state_menu.set(i)
                    self.statelist.insert(0,i)
                    self.state_menu.configure(values=self.statelist)


         except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_party_payamount(self):

        if self.partyname_entry.get() == "":
            self.gstin.set("")
        else:
         con = sqlite3.connect(database=r'../DataBase/ims.db')
         cur = con.cursor()
         try:

            cur.execute("select paybalence from partydata where partyname=?", (self.partyname_entry.get(),))
            rows = cur.fetchall()
            # self.productTable.delete(*self.productTable.get_children())

            for row in rows:
                for i in row:
                    self.reciveamount.set(i)


         except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_party_reciveamount(self):

        if self.partyname_entry.get() == "":
            self.gstin.set("")
        else:
         con = sqlite3.connect(database=r'../DataBase/ims.db')
         cur = con.cursor()
         try:

            cur.execute("select recivebalence from partydata where partyname=?", (self.partyname_entry.get(),))
            rows = cur.fetchall()


            for row in rows:
                for i in row:
                    self.payamount.set(i)

         except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_party_number(self):

        if self.partyname_entry.get() == "":
            self.partynumber.set("")
        else:
          con = sqlite3.connect(database=r'../DataBase/ims.db')
          cur = con.cursor()
          try:

            cur.execute("select phonenumber from partydata where partyname=?", (self.partyname_entry.get(),))
            rows = cur.fetchall()
            # self.productTable.delete(*self.productTable.get_children())

            for row in rows:
                for i in row:
                    self.partynumber.set(i)


          except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_item_price(self, name, seto):
        if name == "":
            seto.set("")
        else:

          con = sqlite3.connect(database=r'../DataBase/ims.db')
          cur = con.cursor()
          try:

            cur.execute("select saleprice from itemdata where itemname=?", (name,))
            rows = cur.fetchall()
            # self.productTable.delete(*self.productTable.get_children())

            for row in rows:
                for i in row:
                    seto.set(i)

          except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_amount(self):
        # pay = int(self.payamount.get())
        recivee = float(self.reciveamount.get())
        payed = int(self.Received_entry.get())
        total = float(self.totalam.get())
        print(recivee)
        print(payed)
        print(total)
        esult = recivee + (total - payed)
        result =str(esult)
        self.resultam.set(result)



    def get_item_unit_list(self):
        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:

            cur.execute("select location from itemdata")
            rows = cur.fetchall()
            # self.productTable.delete(*self.productTable.get_children())

            for row in rows:
                for i in row:
                    self.Item_unit_List.append(i)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_item_tax(self, iname, iseto):
        if iname.get() == "":
            iseto.insert(0, "None")


        else:
          con = sqlite3.connect(database=r'../DataBase/ims.db')
          cur = con.cursor()
          try:

            cur.execute("select gsttax from itemdata where itemname=?", (iname.get(),))
            rows = cur.fetchall()
            # self.productTable.delete(*self.productTable.get_children())
            m=StringVar()
            for row in rows:
                for i in row:
                    iseto.insert(0, i)


          except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_item_qty(self, iname, iseto):
      if iname == "":
          iseto.set(" ")

      else:

        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        iseto.set("1")


    def qtty(self):
        self.itemtable()
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def itprientery(self,event,*args):
            self.itemtable()
            self.finalamount()
            self.totalqty()
            self.totaldesam()
            self.totaltaxam()

    def itemshow(self,event):
        self.itemtable()
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()
    def update_qtye1(self,event,*args):
        self.qtty()
        # self.get_item_qtyentery(self.no1_item_entry.get(), self.iq1)
    def update_qtye2(self,event,*args):
        self.qtty()
        # self.get_item_qtyentery(self.no2_item_entry.get(), self.iq2)
    def update_qtye3(self,event,*args):
        self.qtty()
        #self.get_item_qtyentery(self.no3_item_entry.get(), self.iq3)
    def update_qtye4(self,event,*args):
        self.qtty()
        #self.get_item_qtyentery(self.no4_item_entry.get(), self.iq4)
    def update_qtye5(self,event,*args):
        self.qtty()
        #self.get_item_qtyentery(self.no5_item_entry.get(), self.iq5)
    def update_qtye6(self,event,*args):
        self.qtty()
        #self.get_item_qtyentery(self.no6_item_entry.get(), self.iq6)
    def update_qtye7(self,event,*args):
        self.qtty()
        #self.get_item_qtyentery(self.no7_item_entry.get(), self.iq7)
    def update_qtye8(self,event,*args):
        self.qtty()
        #self.get_item_qtyentery(self.no8_item_entry.get(), self.iq8)
    def update_qtye9(self,event,*args):
        self.qtty()
        #self.get_item_qtyentery(self.no9_item_entry.get(), self.iq9)
    def update_qtye10(self,event,*args):
        self.qtty()
        #self.get_item_qtyentery(self.no10_item_entry.get(), self.iq10)


    # # todo: Update Qty
    # def update_item_qty(self, iname, iseto):
    #
    #     con = sqlite3.connect(database=r'../DataBase/ims.db')
    #     cur = con.cursor()
    #     try:
    #
    #         cur.execute("select minqty from itemdata where itemname=?", (iname,))
    #         rows = cur.fetchall()
    #         cur.execute("Update itemdata set minqty=?",
    #             (
    #         ))
    #         con.commit()
    #
    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)


    def get_item_dec(self, iname, iseto):
      if iname == "":
            iseto.set(" ")
      else:
        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:

            cur.execute("select discount from itemdata where itemname=?", (iname,))
            rows = cur.fetchall()

            for row in rows:

                for i in row:
                    if i == "":
                        i = "0"
                        iseto.set(i)

                    else:
                        iseto.set(i)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_item_unit(self, iname, iseto):
      if iname == "":
          iseto.insert(0, "")
      else:
        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:

            cur.execute("select unit from itemdata where itemname=?", (iname,))
            rows = cur.fetchall()


            for row in rows:

                for i in row:

                    iseto.insert(0, i)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def itemgstbill(self, qty, price, disc, discamo, wtax, tax, taxamout, amount):
       if qty == " " and disc ==" ":
           discamo.set(" ")
           taxamout.set(" ")
           amount.set("0")


       else:
        try:

         price = int(price)
         q=qty.replace(" ","")
         qty = int(q)
         itemprice = qty * price

         if "0" in tax or "0.25" in tax or "3" in tax or "5" in tax or "12" in tax or "18" in tax or "28" in tax or "None" in tax:

            rtax=tax.replace("IGST@","")
            rtax=rtax.replace("GST@","")
            rtax=rtax.replace("GST@","")
            ktax=rtax.replace("%","")
            mtax=ktax.replace("None","0")
            gsttax=float(mtax)


            if wtax.get() == "With Tax":
                if "%" in disc:
                    decf = disc.replace("%", "")
                    decq = decf.replace(" ", "0")
                    disca = float(decq)


                    #find gst
                    withbase = itemprice - (itemprice*(100/(100+gsttax)))
                    it=itemprice-withbase
                    rit=round(it,2)


                    #add discount
                    dicam=rit*disca/100
                    rdicam=round(dicam,2)
                    discamo.set(rdicam)
                    decrem=rit-rdicam
                    rdecrem=round(decrem,2)

                    #add gst
                    withotrem = rdecrem * gsttax / 100
                    rwithotrem=round(withotrem,2)
                    taxamout.set(rwithotrem)

                    finalamount=rdecrem+rwithotrem
                    rfinalamount=round(finalamount,2)
                    amount.set(rfinalamount)




                else:
                    disc.replace(" ","0")
                    disca = float(disc)

                    #find gst
                    withbase = itemprice - (itemprice*(100/(100+gsttax)))
                    it=itemprice-withbase
                    rit=round(it,2)


                    #add discount
                    dicam=rit-disca
                    rr=rit-dicam
                    rdicam=round(dicam,2)

                    discamo.set(rr)

                    #add gst
                    withotrem = rdicam * gsttax / 100
                    rwithotrem=round(withotrem,2)
                    taxamout.set(rwithotrem)

                    finalamount=rdicam+rwithotrem
                    rfinalamount=round(finalamount,2)
                    amount.set(rfinalamount)



            elif wtax.get() == "Without Tax":
                if "%" in disc:
                    decf = disc.replace("%", "")
                    decq = decf.replace(" ", "")
                    disca = float(decq)

                    dicam=itemprice*disca/100
                    discamo.set(dicam)
                    decrem=itemprice-dicam

                    withbase = (decrem * gsttax) / 100
                    rwithbase = round(withbase,2)
                    taxamout.set(rwithbase)

                    finalamount=decrem+withbase
                    amount.set(finalamount)
                else:
                    decf = disc.replace("%", "")
                    decq = decf.replace(" ", "")
                    disca = float(decq)

                    dicam=itemprice-disca

                    decrem=itemprice-dicam
                    discamo.set(decrem)

                    withbase = (dicam * gsttax) / 100
                    rwithbase = round(withbase,2)
                    taxamout.set(rwithbase)

                    finalamount=dicam+withbase
                    amount.set(finalamount)
        except Exception as e:
            print(e)
    def finalamount(self):


        sitam1=self.no1_amount_entry.get()
        sitam2=self.no2_amount_entry.get()
        sitam3=self.no3_amount_entry.get()
        sitam4=self.no4_amount_entry.get()
        sitam5=self.no5_amount_entry.get()
        sitam6=self.no6_amount_entry.get()
        sitam7=self.no7_amount_entry.get()
        sitam8=self.no8_amount_entry.get()
        sitam9=self.no9_amount_entry.get()
        sitam10=self.no10_amount_entry.get()



        if self.roundoff_check.get() == 1:

          finalamount=float(sitam1)+float(sitam2)+float(sitam3)+float(sitam4)+float(sitam5)+float(sitam6)+float(sitam7)+float(sitam8)+float(sitam9)+float(sitam10)
          self.roundoff.set(finalamount)

          roundfinal=round(finalamount)
          self.totalam.set(roundfinal)

          a=self.Received_entry.get()
          m=int(a)
          res=roundfinal-m
          rres=round(res)
          self.balence=rres
          self.Balance_entry.configure(text=self.balence)

        elif self.roundoff_check.get() == 0:
            finalamount=float(sitam1)+float(sitam2)+float(sitam3)+float(sitam4)+float(sitam5)+float(sitam6)+float(sitam7)+float(sitam8)+float(sitam9)+float(sitam10)
            self.roundoff.set("0")
            self.fi=finalamount
            self.Total_amount_lable.configure(text=self.fi)
            ro=finalamount
            self.totalam.set(ro)

            a=self.Received_entry.get()
            m=float(a)
            res=finalamount-m
            rres=res
            self.balence=rres
            self.Balance_entry.configure(text=self.balence)

    def totalqty(self):

        sitam1=self.no1_qty_entry.get()
        sitam2=self.no2_qty_entry.get()
        sitam3=self.no3_qty_entry.get()
        sitam4=self.no4_qty_entry.get()
        sitam5=self.no5_qty_entry.get()
        sitam6=self.no6_qty_entry.get()
        sitam7=self.no7_qty_entry.get()
        sitam8=self.no8_qty_entry.get()
        sitam9=self.no9_qty_entry.get()
        sitam10=self.no10_qty_entry.get()

        itam1=sitam1.replace(" ","0")
        itam2=sitam2.replace(" ","0")
        itam3=sitam3.replace(" ","0")
        itam4=sitam4.replace(" ","0")
        itam5=sitam5.replace(" ","0")
        itam6=sitam6.replace(" ","0")
        itam7=sitam7.replace(" ","0")
        itam8=sitam8.replace(" ","0")
        itam9=sitam9.replace(" ","0")
        itam10=sitam10.replace(" ","0")


        item1=int(itam1)
        item2=int(itam2)
        item3=int(itam3)
        item4=int(itam4)
        item5=int(itam5)
        item6=int(itam6)
        item7=int(itam7)
        item8=int(itam8)
        item9=int(itam9)
        item10=int(itam10)

        finalamount=(item1+item2+item3+item4+item5+item6+item7+item8+item9+item10)

        if finalamount <10:
            ffinalamount=str(finalamount)
            sf="0"+ffinalamount
            self.allqty=sf
            self.total_qty_lable.configure(text=self.allqty)

        else:
            self.allqty=finalamount
            self.total_qty_lable.configure(text=self.allqty)


    def totaldesam(self):

        sitam1=self.no1_dec_amount_entry.get()
        sitam2=self.no2_dec_amount_entry.get()
        sitam3=self.no3_dec_amount_entry.get()
        sitam4=self.no4_dec_amount_entry.get()
        sitam5=self.no5_dec_amount_entry.get()
        sitam6=self.no6_dec_amount_entry.get()
        sitam7=self.no7_dec_amount_entry.get()
        sitam8=self.no8_dec_amount_entry.get()
        sitam9=self.no9_dec_amount_entry.get()
        sitam10=self.no10_dec_amount_entry.get()

        itam1=sitam1.replace(" ","0")
        itam2=sitam2.replace(" ","0")
        itam3=sitam3.replace(" ","0")
        itam4=sitam4.replace(" ","0")
        itam5=sitam5.replace(" ","0")
        itam6=sitam6.replace(" ","0")
        itam7=sitam7.replace(" ","0")
        itam8=sitam8.replace(" ","0")
        itam9=sitam9.replace(" ","0")
        itam10=sitam10.replace(" ","0")
        try:
          item1=float(itam1)
          item2=float(itam2)
          item3=float(itam3)
          item4=float(itam4)
          item5=float(itam5)
          item6=float(itam6)
          item7=float(itam7)
          item8=float(itam8)
          item9=float(itam9)
          item10=float(itam10)


          finalamount=(item1+item2+item3+item4+item5+item6+item7+item8+item9+item10)

          self.kk=str(finalamount)
          self.Totaldic_lable.configure(text=self.kk)

        except Exception as e:
         print(e)

    def totaltaxam(self):

        sitam1=self.no1_tax_amount_entry.get()
        sitam2=self.no2_tax_amount_entry.get()
        sitam3=self.no3_tax_amount_entry.get()
        sitam4=self.no4_tax_amount_entry.get()
        sitam5=self.no5_tax_amount_entry.get()
        sitam6=self.no6_tax_amount_entry.get()
        sitam7=self.no7_tax_amount_entry.get()
        sitam8=self.no8_tax_amount_entry.get()
        sitam9=self.no9_tax_amount_entry.get()
        sitam10=self.no10_tax_amount_entry.get()

        itam1=sitam1.replace(" ","0")
        itam2=sitam2.replace(" ","0")
        itam3=sitam3.replace(" ","0")
        itam4=sitam4.replace(" ","0")
        itam5=sitam5.replace(" ","0")
        itam6=sitam6.replace(" ","0")
        itam7=sitam7.replace(" ","0")
        itam8=sitam8.replace(" ","0")
        itam9=sitam9.replace(" ","0")
        itam10=sitam10.replace(" ","0")

        try:
          item1=float(itam1)
          item2=float(itam2)
          item3=float(itam3)
          item4=float(itam4)
          item5=float(itam5)
          item6=float(itam6)
          item7=float(itam7)
          item8=float(itam8)
          item9=float(itam9)
          item10=float(itam10)

          finalamount=(item1+item2+item3+item4+item5+item6+item7+item8+item9+item10)
          rfinalamount=round(finalamount,2)
          self.diccc=str(rfinalamount)
          self.Totaltax_lable.configure(text=self.diccc)
        except Exception as e:
          print(e)




    def itpri(self):
        self.get_item_price(self.no1_item_entry.get(), self.ip1)
        self.get_item_price(self.no2_item_entry.get(), self.ip2)
        self.get_item_price(self.no3_item_entry.get(), self.ip3)
        self.get_item_price(self.no4_item_entry.get(), self.ip4)
        self.get_item_price(self.no5_item_entry.get(), self.ip5)
        self.get_item_price(self.no6_item_entry.get(), self.ip6)
        self.get_item_price(self.no7_item_entry.get(), self.ip7)
        self.get_item_price(self.no8_item_entry.get(), self.ip8)
        self.get_item_price(self.no9_item_entry.get(), self.ip9)
        self.get_item_price(self.no10_item_entry.get(), self.ip10)

    def itx(self):

        self.get_item_tax(self.no1_item_entry, self.itax1)
        self.get_item_tax(self.no2_item_entry, self.itax2)
        self.get_item_tax(self.no3_item_entry, self.itax3)
        self.get_item_tax(self.no4_item_entry, self.itax4)
        self.get_item_tax(self.no5_item_entry, self.itax5)
        self.get_item_tax(self.no6_item_entry, self.itax6)
        self.get_item_tax(self.no7_item_entry, self.itax7)
        self.get_item_tax(self.no8_item_entry, self.itax8)
        self.get_item_tax(self.no9_item_entry, self.itax9)
        self.get_item_tax(self.no10_item_entry, self.itax10)


    def iqt(self):
        self.get_item_qty(self.no1_item_entry.get(), self.iq1)
        self.get_item_qty(self.no2_item_entry.get(), self.iq2)
        self.get_item_qty(self.no3_item_entry.get(), self.iq3)
        self.get_item_qty(self.no4_item_entry.get(), self.iq4)
        self.get_item_qty(self.no5_item_entry.get(), self.iq5)
        self.get_item_qty(self.no6_item_entry.get(), self.iq6)
        self.get_item_qty(self.no7_item_entry.get(), self.iq7)
        self.get_item_qty(self.no8_item_entry.get(), self.iq8)
        self.get_item_qty(self.no9_item_entry.get(), self.iq9)
        self.get_item_qty(self.no10_item_entry.get(), self.iq10)

    def secper(self):
        self.get_item_dec(self.no1_item_entry.get(), self.id1)
        self.get_item_dec(self.no2_item_entry.get(), self.id2)
        self.get_item_dec(self.no3_item_entry.get(), self.id3)
        self.get_item_dec(self.no4_item_entry.get(), self.id4)
        self.get_item_dec(self.no5_item_entry.get(), self.id5)
        self.get_item_dec(self.no6_item_entry.get(), self.id6)
        self.get_item_dec(self.no7_item_entry.get(), self.id7)
        self.get_item_dec(self.no8_item_entry.get(), self.id8)
        self.get_item_dec(self.no9_item_entry.get(), self.id9)
        self.get_item_dec(self.no10_item_entry.get(), self.id10)

    def itemtable(self):
        self.itemgstbill(self.no1_qty_entry.get(), self.no1_unitprice_entry.get(), self.no1_dec_percentagee_entry.get(),
                         self.ida1, self.tax_unit_box, self.no1_tax_percentagee_entry.get(), self.ita1, self.iam1)
        self.itemgstbill(self.no2_qty_entry.get(), self.no2_unitprice_entry.get(), self.no2_dec_percentagee_entry.get(),
                         self.ida2, self.tax_unit_box, self.no2_tax_percentagee_entry.get(), self.ita2, self.iam2)
        self.itemgstbill(self.no3_qty_entry.get(), self.no3_unitprice_entry.get(), self.no3_dec_percentagee_entry.get(),
                         self.ida3, self.tax_unit_box, self.no3_tax_percentagee_entry.get(), self.ita3, self.iam3)
        self.itemgstbill(self.no4_qty_entry.get(), self.no4_unitprice_entry.get(), self.no4_dec_percentagee_entry.get(),
                         self.ida4, self.tax_unit_box, self.no4_tax_percentagee_entry.get(), self.ita4, self.iam4)
        self.itemgstbill(self.no5_qty_entry.get(), self.no5_unitprice_entry.get(), self.no5_dec_percentagee_entry.get(),
                         self.ida5, self.tax_unit_box, self.no5_tax_percentagee_entry.get(), self.ita5, self.iam5)
        self.itemgstbill(self.no6_qty_entry.get(), self.no6_unitprice_entry.get(), self.no6_dec_percentagee_entry.get(),
                         self.ida6, self.tax_unit_box, self.no6_tax_percentagee_entry.get(), self.ita6, self.iam6)
        self.itemgstbill(self.no7_qty_entry.get(), self.no7_unitprice_entry.get(), self.no7_dec_percentagee_entry.get(),
                         self.ida7, self.tax_unit_box, self.no7_tax_percentagee_entry.get(), self.ita7, self.iam7)
        self.itemgstbill(self.no8_qty_entry.get(), self.no8_unitprice_entry.get(), self.no8_dec_percentagee_entry.get(),
                         self.ida8, self.tax_unit_box, self.no8_tax_percentagee_entry.get(), self.ita8, self.iam8)
        self.itemgstbill(self.no9_qty_entry.get(), self.no9_unitprice_entry.get(), self.no9_dec_percentagee_entry.get(),
                         self.ida9, self.tax_unit_box, self.no9_tax_percentagee_entry.get(), self.ita9, self.iam9)
        self.itemgstbill(self.no10_qty_entry.get(), self.no10_unitprice_entry.get(), self.no10_dec_percentagee_entry.get(),
                         self.ida10, self.tax_unit_box, self.no10_tax_percentagee_entry.get(), self.ita10, self.iam10)

    def party(self,event):
        self.get_party_data()
        self.get_party_number()
        self.get_party_gstin()
        self.get_party_state()

    def show(self,event):
        self.itpri()
        self.itx()
        self.get_party_data()
        self.itemtable()
        self.finalamount()



    def get_item_name(self):
        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:

            cur.execute("select itemname from itemdata")
            rows = cur.fetchall()
            # self.productTable.delete(*self.productTable.get_children())
            self.ItemList.clear()
            for row in rows:
                for i in row:
                    self.ItemList.append(i)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def itemlist_update1(self,event,*args):
        self.update_combobox(self.no1_item_entry,self.itm1)
    def itemlist_update2(self,event,*args):
        self.update_combobox(self.no2_item_entry,self.itm2)
    def itemlist_update3(self,event,*args):
        self.update_combobox(self.no3_item_entry,self.itm3)
    def itemlist_update4(self,event,*args):
        self.update_combobox(self.no4_item_entry,self.itm4)
    def itemlist_update5(self,event,*args):
        self.update_combobox(self.no5_item_entry,self.itm5)
    def itemlist_update6(self,event,*args):
        self.update_combobox(self.no6_item_entry,self.itm6)
    def itemlist_update7(self,event,*args):
        self.update_combobox(self.no7_item_entry,self.itm7)
    def itemlist_update8(self,event,*args):
        self.update_combobox(self.no8_item_entry,self.itm8)
    def itemlist_update9(self,event,*args):
        self.update_combobox(self.no9_item_entry,self.itm9)
    def itemlist_update10(self,event,*args):
        self.update_combobox(self.no10_item_entry,self.itm10)

    def update_combobox(self,entery,method):
        type=entery.get()
        self.ItemList.clear()
        self.ItemList.append("")
        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select itemname from itemdata")
            rows = cur.fetchall()
            for items in rows:
              for i in items:
                m=str(i)
                if type.lower() in m.lower():
                  self.ItemList.append(i)

            entery.configure(values=self.ItemList)
            self.get_item_name()
        except Exception as ex:
              messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def updateparty(self,*args):
        self.Partynames.clear()
        self.Partynames.append("")
        name=self.Party_var.get()

        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:

            cur.execute("select partyname from partydata")
            rows = cur.fetchall()

            for row in rows:
                for i in row:

                    m=str(i)
                    if name.lower() in m.lower():

                        self.Partynames.append(i)
            self.partyname_entry.configure(values=self.Partynames)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)


    def itm1(self,event):
        self.get_item_qty(self.no1_item_entry.get(), self.iq1)
        self.get_item_price(self.no1_item_entry.get(), self.ip1)
        self.get_item_tax(self.no1_item_entry, self.itax1)
        self.get_item_dec(self.no1_item_entry.get(), self.id1)
        # self.itx()
        self.itemgstbill(self.no1_qty_entry.get(), self.no1_unitprice_entry.get(), self.no1_dec_percentagee_entry.get(),
                         self.ida1, self.tax_unit_box, self.no1_tax_percentagee_entry.get(), self.ita1, self.iam1)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()


    def itm2(self,event):
        self.get_item_qty(self.no2_item_entry.get(), self.iq2)
        self.get_item_price(self.no2_item_entry.get(), self.ip2)
        self.get_item_tax(self.no2_item_entry, self.itax2)
        self.get_item_dec(self.no2_item_entry.get(), self.id2)
        self.itemgstbill(self.no2_qty_entry.get(), self.no2_unitprice_entry.get(), self.no2_dec_percentagee_entry.get(),
                         self.ida2, self.tax_unit_box, self.no2_tax_percentagee_entry.get(), self.ita2, self.iam2)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def itm3(self,event):
        self.get_item_qty(self.no3_item_entry.get(), self.iq3)
        self.get_item_price(self.no3_item_entry.get(), self.ip3)
        self.get_item_tax(self.no3_item_entry, self.itax3)
        self.get_item_dec(self.no3_item_entry.get(), self.id3)
        self.itemgstbill(self.no3_qty_entry.get(), self.no3_unitprice_entry.get(), self.no3_dec_percentagee_entry.get(),
                         self.ida3, self.tax_unit_box, self.no3_tax_percentagee_entry.get(), self.ita3, self.iam3)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def itm4(self,event):
        self.get_item_qty(self.no4_item_entry.get(), self.iq4)
        self.get_item_price(self.no4_item_entry.get(), self.ip4)
        self.get_item_tax(self.no4_item_entry, self.itax4)
        self.get_item_dec(self.no4_item_entry.get(), self.id4)
        self.itemgstbill(self.no4_qty_entry.get(), self.no4_unitprice_entry.get(), self.no4_dec_percentagee_entry.get(),
                         self.ida4, self.tax_unit_box, self.no4_tax_percentagee_entry.get(), self.ita4, self.iam4)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def itm5(self,event):
        self.get_item_qty(self.no5_item_entry.get(), self.iq5)
        self.get_item_price(self.no5_item_entry.get(), self.ip5)
        self.get_item_tax(self.no5_item_entry, self.itax5)
        self.get_item_dec(self.no5_item_entry.get(), self.id5)
        self.itemgstbill(self.no5_qty_entry.get(), self.no5_unitprice_entry.get(), self.no5_dec_percentagee_entry.get(),
                         self.ida5, self.tax_unit_box, self.no5_tax_percentagee_entry.get(), self.ita5, self.iam5)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def itm6(self,event):
        self.get_item_qty(self.no6_item_entry.get(), self.iq6)
        self.get_item_price(self.no6_item_entry.get(), self.ip6)
        self.get_item_tax(self.no6_item_entry, self.itax6)
        self.get_item_dec(self.no6_item_entry.get(), self.id6)
        self.itemgstbill(self.no6_qty_entry.get(), self.no6_unitprice_entry.get(), self.no6_dec_percentagee_entry.get(),
                         self.ida6, self.tax_unit_box, self.no6_tax_percentagee_entry.get(), self.ita6, self.iam6)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def itm7(self,event):
        self.get_item_qty(self.no7_item_entry.get(), self.iq7)
        self.get_item_price(self.no7_item_entry.get(), self.ip7)
        self.get_item_tax(self.no7_item_entry, self.itax7)
        self.get_item_dec(self.no7_item_entry.get(), self.id7)
        self.itemgstbill(self.no7_qty_entry.get(), self.no7_unitprice_entry.get(), self.no7_dec_percentagee_entry.get(),
                         self.ida7, self.tax_unit_box, self.no7_tax_percentagee_entry.get(), self.ita7, self.iam7)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def itm8(self,event):
        self.get_item_qty(self.no8_item_entry.get(), self.iq8)
        self.get_item_price(self.no8_item_entry.get(), self.ip8)
        self.get_item_tax(self.no8_item_entry, self.itax8)
        self.get_item_dec(self.no8_item_entry.get(), self.id8)
        self.itemgstbill(self.no8_qty_entry.get(), self.no8_unitprice_entry.get(), self.no8_dec_percentagee_entry.get(),
                         self.ida8, self.tax_unit_box, self.no8_tax_percentagee_entry.get(), self.ita8, self.iam8)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def itm9(self,event):
        self.get_item_qty(self.no9_item_entry.get(), self.iq9)
        self.get_item_price(self.no9_item_entry.get(), self.ip9)
        self.get_item_tax(self.no9_item_entry, self.itax9)
        self.get_item_dec(self.no9_item_entry.get(), self.id9)
        self.itemgstbill(self.no9_qty_entry.get(), self.no9_unitprice_entry.get(), self.no9_dec_percentagee_entry.get(),
                         self.ida9, self.tax_unit_box, self.no9_tax_percentagee_entry.get(), self.ita9, self.iam9)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def itm10(self,event):
        self.get_item_qty(self.no10_item_entry.get(), self.iq10)
        self.get_item_price(self.no10_item_entry.get(), self.ip10)
        self.get_item_tax(self.no10_item_entry, self.itax10)
        self.get_item_dec(self.no10_item_entry.get(), self.id10)
        self.itemgstbill(self.no10_qty_entry.get(), self.no10_unitprice_entry.get(), self.no10_dec_percentagee_entry.get(),
                         self.ida10, self.tax_unit_box, self.no10_tax_percentagee_entry.get(), self.ita10, self.iam10)
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def tax(self,event):
        self.itemtable()
        self.finalamount()
        self.totalqty()
        self.totaldesam()
        self.totaltaxam()

    def invoice_genrator(self):

        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:

                cur.execute("select invoice from purinvo where no=1",)
                rows = cur.fetchall()
                # self.productTable.delete(*self.productTable.get_children())
                for row in rows:
                    for i in row:
                        invoice_zero=6-len(i)
                        self.incre=int(i)+1
                        a=1
                        mm = "0"
                        while a<invoice_zero:
                            mm=mm+"0"
                            a+=1
                        final=f"{mm}{self.incre}"
                        strfinal=str(final)
                        self.invo.set(strfinal)
                        self.invoice_entry.configure(textvariable=self.invo)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def invoice_updator(self):
        p = 1
        con = sqlite3.connect(database=r'../DataBase/ims.db')
        cur = con.cursor()
        try:

            cur.execute("Select no from purinvo where no=?", (p,))
            row = cur.fetchone()
            cur.execute("Update purinvo set invoice=? where no=?", (
                self.incre,
                p,
            ))
            con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def update_item_qty(self, name, seto,pri,unit,gst):
        if name == "":
            seto.set("")
        else:

          con = sqlite3.connect(database=r'../DataBase/ims.db')
          cur = con.cursor()
          try:
              if seto=="":
                  pass
              else:
                  cur.execute("select openqty from itemdata where itemname=?", (name,))
                  rows = cur.fetchall()

                  b=seto.get()
                  price=pri.get()
                  un=unit.get()
                  date=self.date_entry.get()
                  tax=gst.get()
                  for row in rows:
                     for i in row:
                       resualt=int(i)+int(b)
                       cur.execute("select pid from itemdata where itemname=?", (name,))
                       pids = cur.fetchall()
                       for pid in pids:
                           for p in pid:

                              cur.execute("Select pid from itemdata where pid=?", (p,))
                              row = cur.fetchone()
                              cur.execute("Update itemdata set openqty=?,purchesprice=?,date=?,location=?,gsttax=? where pid=?", (
                               resualt,
                               price,
                               date,
                               un,
                               tax,
                               p,
                                ))
                              con.commit()

          except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def update_iqt(self):
        self.update_item_qty(self.no1_item_entry.get(), self.iq1, self.ip1, self.no1_unit_entry, self.no1_tax_percentagee_entry)
        self.update_item_qty(self.no2_item_entry.get(), self.iq2, self.ip2, self.no2_unit_entry, self.no2_tax_percentagee_entry)
        self.update_item_qty(self.no3_item_entry.get(), self.iq3, self.ip3, self.no3_unit_entry, self.no3_tax_percentagee_entry)
        self.update_item_qty(self.no4_item_entry.get(), self.iq4, self.ip4, self.no4_unit_entry, self.no4_tax_percentagee_entry)
        self.update_item_qty(self.no5_item_entry.get(), self.iq5, self.ip5, self.no5_unit_entry, self.no5_tax_percentagee_entry)
        self.update_item_qty(self.no6_item_entry.get(), self.iq6, self.ip6, self.no6_unit_entry, self.no6_tax_percentagee_entry)
        self.update_item_qty(self.no7_item_entry.get(), self.iq7, self.ip7, self.no7_unit_entry, self.no7_tax_percentagee_entry)
        self.update_item_qty(self.no8_item_entry.get(), self.iq8, self.ip8, self.no8_unit_entry, self.no8_tax_percentagee_entry)
        self.update_item_qty(self.no9_item_entry.get(), self.iq9, self.ip9, self.no9_unit_entry, self.no9_tax_percentagee_entry)
        self.update_item_qty(self.no10_item_entry.get(), self.iq10, self.ip10, self.no10_unit_entry, self.no10_tax_percentagee_entry)

    def amountupdate(self,*args):
        self.finalamount()


    def refrance(self,event):
        if self.Payment_type_entry.get() == "Cheque":
           self.Cheque_entry.place(x=50, y=790)
        elif self.Payment_type_entry.get() == "Cash":
           self.Cheque_entry.place_forget()

if __name__ == "__main__":
    app = saleClass()
    app.mainloop()


