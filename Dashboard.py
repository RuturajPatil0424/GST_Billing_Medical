import customtkinter
from customtkinter import *
import os
from PIL import Image
from subprocess import call
import sqlite3
from tkinter import messagebox, END, ttk
from AppOpener import open as op, close
from datetime import date as Dates

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("GST Billing System")
        self.geometry("1920x1080+-10+-3")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
                                                 size=(26, 26))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home.png")),
                                                 size=(30, 30))

        self.party_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "party.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "party.png")),
                                                 size=(30, 30))
        self.item_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "items.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "items.png")),
                                                  size=(30, 30))
        self.gstsale_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "gstsale.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "gstsale.png")),
                                                 size=(30, 30))
        self.sale_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "sale.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "sale.png")),
                                                 size=(30, 30))
        self.purches_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "purches.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "purches.png")),
                                                 size=(30, 30))
        self.expenses_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "expencess.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "expencess.png")),
                                                 size=(30, 30))
        self.cashhandel_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "cashhandel.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "cashhandel.png")),
                                                 size=(30, 30))
        self.reports_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "report.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "report.png")),
                                                 size=(30, 30))
        self.sync_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "sync.png")),
                                                    dark_image=Image.open(os.path.join(image_path, "sync.png")),
                                                    size=(30, 30))
        self.backup_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "backup.png")),
                                                    dark_image=Image.open(os.path.join(image_path, "backup.png")),
                                                    size=(30, 30))
        self.setting_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "settings.png")),
                                                    dark_image=Image.open(os.path.join(image_path, "settings.png")),
                                                    size=(30, 30))
        self.download_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "download.png")),
                                                    dark_image=Image.open(os.path.join(image_path, "download.png")),
                                                    size=(30, 30))
        self.tools_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "tools.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "tools.png")),
                                                     size=(30, 30))
        self.scale_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "scale.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "scale.png")),
                                                  size=(30, 30))
        self.mode_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "mode.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "mode.png")),
                                                  size=(30, 30))
        self.buy_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "buy.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "buy.png")),
                                                 size=(30, 30))
        self.sellitem_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "saleitem.png")),
                                                dark_image=Image.open(os.path.join(image_path, "saleitem.png")),
                                                size=(30, 30))
        self.saleim_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "saleim.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "saleim.png")),
                                                     size=(30, 30))
        self.uparrow_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "uparrow.png")),
                                                   dark_image=Image.open(os.path.join(image_path, "uparrow.png")),
                                                   size=(30, 30))
        self.dwonarrow_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "downarrow.png")),
                                                   dark_image=Image.open(os.path.join(image_path, "downarrow.png")),
                                                   size=(30, 30))
        self.basket_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "basket.png")),
                                                      dark_image=Image.open(os.path.join(image_path, "basket.png")),
                                                      size=(30, 30))
        self.wallet_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "wallet.png")),
                                                      dark_image=Image.open(os.path.join(image_path, "wallet.png")),
                                                      size=(30, 30))
        self.add_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "addlight.png")),
                                                   dark_image=Image.open(os.path.join(image_path, "adddark.png")),
                                                   size=(30, 30))
        self.calculator_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "calculator.png")),
                                                dark_image=Image.open(os.path.join(image_path, "calculator.png")),
                                                size=(30, 30))
        self.stock_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "lowitem.png")),
            dark_image=Image.open(os.path.join(image_path, "lowitem.png")),
            size=(30, 30))
        self.edit_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "edit.png")),
            dark_image=Image.open(os.path.join(image_path, "edit.png")),
            size=(30, 30))
        self.bill_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "bill.png")),
            dark_image=Image.open(os.path.join(image_path, "bill.png")),
            size=(30, 30))

        # todo: crete navigation bar
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(22, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Cyber tech",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=5,
                                                   text="Home",
                                                   fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.parties_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=5, text="Parties",
                                                      fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                      text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.party_image, anchor="w",
                                                      command=self.parties_button_event)
        self.parties_button.grid(row=2, column=0, sticky="ew")

        self.Items_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                    border_spacing=5, text="Items",
                                                    fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                    text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.item_image, anchor="w",
                                                    command=self.Items_button_event)
        self.Items_button.grid(row=3, column=0, sticky="ew")

        self.gst_sale_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                       border_spacing=5, text="GST Sale",
                                                       fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                       text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       image=self.gstsale_image, anchor="w",
                                                       command=self.gst_sale_button_event)
        self.gst_sale_button.grid(row=4, column=0, sticky="ew")

        self.sale_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=5,
                                                   text="Sale",
                                                   fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.sale_image, anchor="w",
                                                   command=self.sale_button_event)
        self.sale_button.grid(row=5, column=0, sticky="ew")

        self.Purches_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=5, text="Purches",
                                                      fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                      text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.purches_image, anchor="w",
                                                      command=self.Purches_button_event)
        self.Purches_button.grid(row=6, column=0, sticky="ew")

        self.Expenses_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                       border_spacing=5, text="Expenses",
                                                       fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                       text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       image=self.expenses_image, anchor="w",
                                                       command=self.Expenses_button_event)
        self.Expenses_button.grid(row=7, column=0, sticky="ew")

        self.Cashhandel_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                         border_spacing=5, text="Cash & Handel",
                                                         fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                         text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         image=self.cashhandel_image, anchor="w",
                                                         command=self.Cashhandel_button_event)
        self.Cashhandel_button.grid(row=8, column=0, sticky="ew")

        self.Reports_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=5, text="Reports",
                                                      fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                      text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.reports_image, anchor="w",
                                                      command=self.Reports_button_event)
        self.Reports_button.grid(row=9, column=0, sticky="ew")

        self.Sync_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=5,
                                                   text="Sync",
                                                   fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.sync_image, anchor="w",
                                                   command=self.Sync_button_event)
        self.Sync_button.grid(row=10, column=0, sticky="ew")

        self.Backup_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                     border_spacing=5, text="Backup/Restore",
                                                     fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                     text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     image=self.backup_image, anchor="w",
                                                     command=self.Backup_button_event)
        self.Backup_button.grid(row=11, column=0, sticky="ew")

        self.Utilities_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                        border_spacing=5, text="Utilities",
                                                        fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                        text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        image=self.tools_image, anchor="w",
                                                        command=self.Utilities_button_event)
        self.Utilities_button.grid(row=12, column=0, sticky="ew")

        self.Setting_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=5, text="Settings",
                                                      fg_color="transparent", font=customtkinter.CTkFont(size=15),
                                                      text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.setting_image, anchor="w",
                                                      command=self.Setting_button_event)
        self.Setting_button.grid(row=13, column=0, sticky="ew")

        self.scaling_label = customtkinter.CTkLabel(self.navigation_frame,image=self.mode_image,compound="left",anchor="w", text="   Dark Mode", font=customtkinter.CTkFont(size=15))
        self.scaling_label.grid(row=14, column=0, padx=20, pady=(10, 0))

        self.apmodelist =["Light", "Dark", "System"]
        self.appearancelis2 = ["Light", "Dark", "System"]
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=15, column=0, padx=20, pady=20, sticky="s")

        self.scaling_label = customtkinter.CTkLabel(self.navigation_frame,image=self.scale_image,compound="left", text="   UI Scaling", anchor="w", font=customtkinter.CTkFont(size=15))
        self.scaling_label.grid(row=16, column=0, padx=20, pady=(10, 0))

        self.scalelis=["80%", "90%","100%","110%", "120%"]
        self.scalelis2 = ["80%", "90%", "100%", "110%", "120%"]
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                               command=self.change_appearance_mode_event)
        self.scaling_optionemenu.grid(row=17, column=0, padx=20, pady=(10, 20))
        self.get_appearance_mode_event()

        # todo: crete frames
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)


        # todo: Home frame
        self.in_home_top_frame = customtkinter.CTkFrame(self.home_frame, width=1720, height=80)
        self.in_home_top_frame.place(x=10, y=10)

        self.home_add_sale_button = customtkinter.CTkButton(self.in_home_top_frame,
                                                            font=customtkinter.CTkFont(size=18),command=self.addsale_event,
                                                            text="Add Sale", width=70, height=30,
                                                            image=self.bill_image,text_color="black",
                                                            hover_color=("gray70", "gray30"),fg_color="transparent")
        self.home_add_sale_button.place(x=1310, y=20)

        self.home_add_purchess_button = customtkinter.CTkButton(self.in_home_top_frame,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add Purchess", width=70, height=30,command=self.addpurchase_event,
                                                                image=self.buy_image,text_color="black",
                                                                hover_color=("gray70", "gray30"),fg_color="transparent")
        self.home_add_purchess_button.place(x=1440, y=20)

        self.home_setting_party_button = customtkinter.CTkButton(self.in_home_top_frame,width=30,height=30,text="",text_color="black", hover_color=("gray70", "gray30"),image=self.setting_image,fg_color="transparent")
        self.home_setting_party_button.place(x=1660, y=20)

        self.home_calculator_party_button = customtkinter.CTkButton(self.in_home_top_frame, width=30, height=30, text="",
                                                                 text_color="black", hover_color=("gray70", "gray30"),
                                                                 image=self.calculator_image, fg_color="transparent",command=self.opencalcu)
        self.home_calculator_party_button.place(x=1610, y=20)

        # todo: home main frame
        self.in_home_sale_top_frame = customtkinter.CTkFrame(self.home_frame, width=900, height=300)
        self.in_home_sale_top_frame.place(x=10, y=100)

        self.in_home_expenses_top_frame = customtkinter.CTkFrame(self.home_frame, width=310, height=300)
        self.in_home_expenses_top_frame.place(x=920, y=100)

        self.in_home_recive_top_frame = customtkinter.CTkFrame(self.home_frame, width=400, height=300)
        self.in_home_recive_top_frame.place(x=10, y=410)

        self.in_home_pay_top_frame = customtkinter.CTkFrame(self.home_frame, width=400, height=300)
        self.in_home_pay_top_frame.place(x=420, y=410)

        self.in_home_purchase_top_frame = customtkinter.CTkFrame(self.home_frame, width=400, height=300)
        self.in_home_purchase_top_frame.place(x=830, y=410)

        self.in_home_lowitem_top_frame = customtkinter.CTkFrame(self.home_frame, width=400, height=270)
        self.in_home_lowitem_top_frame.place(x=10, y=720)

        self.in_home_cheques_frame = customtkinter.CTkFrame(self.home_frame, width=460, height=120)
        self.in_home_cheques_frame.place(x=1255, y=540)

        self.in_home_stock_frame = customtkinter.CTkFrame(self.home_frame, width=460, height=90)
        self.in_home_stock_frame.place(x=1255, y=135)

        self.in_home_cash_frame = customtkinter.CTkFrame(self.home_frame, width=460, height=120)
        self.in_home_cash_frame.place(x=1255, y=280)

        self.in_bank_cash_frame = customtkinter.CTkFrame(self.home_frame, width=460, height=120)
        self.in_bank_cash_frame.place(x=1255, y=410)

        self.in_order_frame = customtkinter.CTkFrame(self.home_frame, width=460, height=120)
        self.in_order_frame.place(x=1255, y=710)

        self.in_purchase_order_frame = customtkinter.CTkFrame(self.home_frame, width=460, height=120)
        self.in_purchase_order_frame.place(x=1255, y=870)


        # todo: Purchase handel bar
        self.purchase_main_lable = customtkinter.CTkLabel(self.home_frame, text="Purchase",
                                                      font=customtkinter.CTkFont(size=20))
        self.purchase_main_lable.place(x=1255, y=840)
        self.purchase_lable = customtkinter.CTkLabel(self.in_purchase_order_frame, text="Purchase Orders",
                                                 font=customtkinter.CTkFont(size=20))
        self.purchase_lable.place(x=10, y=10)
        self.purchaseorderam = StringVar()
        self.purchaseorderam = "0"
        self.purchase_amount_orderam = StringVar()
        self.purchase_amount_orderam = "0"

        self.purchase_order_lable = customtkinter.CTkLabel(self.in_purchase_order_frame, text="No. Of Purchase Orders",
                                                      font=customtkinter.CTkFont(size=15))
        self.purchase_order_lable.place(x=10, y=50)

        self.purchase_order_amount_lable = customtkinter.CTkLabel(self.in_purchase_order_frame, text=self.purchaseorderam,
                                                             font=customtkinter.CTkFont(size=15))
        self.purchase_order_amount_lable.place(x=400, y=50)

        self.purchase_amount_lable = customtkinter.CTkLabel(self.in_purchase_order_frame, text="Purchase Orders Amount",
                                                      font=customtkinter.CTkFont(size=15))
        self.purchase_amount_lable.place(x=10, y=80)

        self.purchaseorder_amount_lable = customtkinter.CTkLabel(self.in_purchase_order_frame, text=self.purchase_amount_orderam,
                                                             font=customtkinter.CTkFont(size=15))
        self.purchaseorder_amount_lable.place(x=400, y=80)

        # todo: Sale  bar
        self.sale_main_lable = customtkinter.CTkLabel(self.home_frame, text="Sale",
                                                       font=customtkinter.CTkFont(size=20))
        self.sale_main_lable.place(x=1255, y=680)
        self.sale_lable = customtkinter.CTkLabel(self.in_order_frame, text="Sale Orders",
                                                 font=customtkinter.CTkFont(size=20))
        self.sale_lable.place(x=10, y=10)
        self.openorderam = StringVar()
        self.openorderam = "0"
        self.saleorderam = StringVar()
        self.saleorderam = "0"

        self.openorder_lable = customtkinter.CTkLabel(self.in_order_frame, text="No. Of Open Orders",
                                                 font=customtkinter.CTkFont(size=15))
        self.openorder_lable.place(x=10, y=50)

        self.openorder_amount_lable = customtkinter.CTkLabel(self.in_order_frame, text=self.openorderam,
                                                        font=customtkinter.CTkFont(size=15))
        self.openorder_amount_lable.place(x=400, y=50)

        self.saleorder_lable = customtkinter.CTkLabel(self.in_order_frame, text="Open Sale Orders Amount",
                                                      font=customtkinter.CTkFont(size=15))
        self.saleorder_lable.place(x=10, y=80)

        self.saleorder_amount_lable = customtkinter.CTkLabel(self.in_order_frame, text=self.saleorderam,
                                                             font=customtkinter.CTkFont(size=15))
        self.saleorder_amount_lable.place(x=400, y=80)

        # todo: cash handel bar
        self.Stock_main_lable = customtkinter.CTkLabel(self.home_frame, text="Cash & Bank",
                                                       font=customtkinter.CTkFont(size=20))
        self.Stock_main_lable.place(x=1255, y=245)
        self.cash_lable = customtkinter.CTkLabel(self.in_home_cash_frame, text="Cash in hand",
                                                  font=customtkinter.CTkFont(size=20))
        self.cash_lable.place(x=10, y=10)
        self.casham = StringVar()
        self.casham = "₹ 00.00"

        self.cash_amount_lable = customtkinter.CTkLabel(self.in_home_cash_frame, text=self.casham,
                                                         font=customtkinter.CTkFont(size=20),text_color="green")
        self.cash_amount_lable.place(x=10, y=50)

        # todo: bank handel bar
        self.bank_lable = customtkinter.CTkLabel(self.in_bank_cash_frame, text="Cash in Bank",
                                                 font=customtkinter.CTkFont(size=20))
        self.bank_lable.place(x=10, y=10)
        self.bankam = StringVar()
        self.bankam = "₹ 00.00"

        self.bank_amount_lable = customtkinter.CTkLabel(self.in_bank_cash_frame, text=self.bankam,
                                                        font=customtkinter.CTkFont(size=20))
        self.bank_amount_lable.place(x=10, y=50)

        # todo: Stock bar bar
        self.Stock_main_lable = customtkinter.CTkLabel(self.home_frame, text="Stock Inventory",
                                                  font=customtkinter.CTkFont(size=20))
        self.Stock_main_lable.place(x=1255, y=100)

        self.Stock_lable = customtkinter.CTkLabel(self.in_home_stock_frame, text="Stock Value",
                                                    font=customtkinter.CTkFont(size=20))
        self.Stock_lable.place(x=10, y=10)
        self.stockam = StringVar()
        self.stockam = "₹ 00.00"
        self.itemtotalamlist=[]

        self.stock_amount_lable = customtkinter.CTkLabel(self.in_home_stock_frame, text=self.stockam,
                                                        font=customtkinter.CTkFont(size=20))
        self.stock_amount_lable.place(x=10, y=50)

        self.calstockvalue()

        # todo: cheques bar bar
        self.cheques_lable = customtkinter.CTkLabel(self.in_home_cheques_frame, text="Open Cheques",
                                                        font=customtkinter.CTkFont(size=20))
        self.cheques_lable.place(x=10, y=10)

        self.cheques_lable = customtkinter.CTkLabel(self.in_home_cheques_frame, text=f"Received ()",
                                                    font=customtkinter.CTkFont(size=15))
        self.cheques_lable.place(x=10, y=50)

        self.cheques_am_lable = customtkinter.CTkLabel(self.in_home_cheques_frame, text="400",
                                                    font=customtkinter.CTkFont(size=15))
        self.cheques_am_lable.place(x=400, y=50)

        self.cheques_paid_lable = customtkinter.CTkLabel(self.in_home_cheques_frame, text=f"Paid ()",
                                                    font=customtkinter.CTkFont(size=15))
        self.cheques_paid_lable.place(x=10, y=80)

        self.cheques_paid_am_lable = customtkinter.CTkLabel(self.in_home_cheques_frame, text="500",
                                                    font=customtkinter.CTkFont(size=15))
        self.cheques_paid_am_lable.place(x=400, y=80)

        # todo: home sale frame

        self.sale_lable=customtkinter.CTkLabel(self.in_home_sale_top_frame,text=" Sale",font=customtkinter.CTkFont(size=25),image=self.saleim_image,compound="left",anchor="w")
        self.sale_lable.place(x=10,y=10)
        self.saleam=StringVar()
        self.saleam="₹ 00"
        self.saletotalamlist=[]
        self.totalsaleam=[]
        self.purtotalamlist = []
        self.pursaleam = []

        self.sale_amount_lable = customtkinter.CTkLabel(self.in_home_sale_top_frame, text=self.saleam,
                                                        font=customtkinter.CTkFont(size=30, weight="bold"))
        self.sale_amount_lable.place(x=10, y=80)
        self.sale_amount_lable2 = customtkinter.CTkLabel(self.in_home_sale_top_frame, text="Total Sale",
                                                        font=customtkinter.CTkFont(size=15))
        self.sale_amount_lable2.place(x=10, y=120)

        self.sale_amount_date = customtkinter.CTkLabel(self.in_home_sale_top_frame,
                                                         font=customtkinter.CTkFont(size=15))
        self.sale_amount_date.place(x=600, y=10)

        self.salegroth = StringVar()
        self.salegroth = "0%"

        self.sale_growt_lable = customtkinter.CTkLabel(self.in_home_sale_top_frame, text=self.salegroth,
                                                        font=customtkinter.CTkFont(size=30),text_color="green",image=self.uparrow_image,compound="left",anchor="w")
        self.sale_growt_lable.place(x=10, y=180)
        self.sale_growt_lable2 = customtkinter.CTkLabel(self.in_home_sale_top_frame, text="This Month Growth",
                                                         font=customtkinter.CTkFont(size=15))
        self.sale_growt_lable2.place(x=10, y=220)

        self.sale_optionemenu = customtkinter.CTkOptionMenu(self.in_home_sale_top_frame,width=40,
                                                               values=["Today",'Yesterday','This Weak','Last Weak','This Month',"Last Month", "This Quarter","Last Quarter", "This Year","Last Year"],command=self.gd)
        self.sale_optionemenu.place(x=790,y=10)

        # todo: home expenses frame

        self.expenses_lable = customtkinter.CTkLabel(self.in_home_expenses_top_frame, text="00.00",
                                                 font=customtkinter.CTkFont(size=25), image=self.wallet_image,
                                                 compound="left", anchor="w")
        self.expenses_lable.place(x=10, y=10)
        self.expenses_optionemenu = customtkinter.CTkOptionMenu(self.in_home_expenses_top_frame,width=40,
                                                            values=["This Month","Last Month", "This Quarter", "This Year"])
        self.expenses_optionemenu.place(x=200, y=10)

        self.expenses_lable2 = customtkinter.CTkLabel(self.in_home_expenses_top_frame, text=self.saleam,
                                                        font=customtkinter.CTkFont(size=20))
        self.expenses_lable2.place(x=10, y=50)

        # todo: home recive frame
        self.reciveam = StringVar()
        self.reciveam = "₹ 00.00"
        self.recivetotalamlist = []
        self.totalreciveam = []

        self.reciveam_lable = customtkinter.CTkLabel(self.in_home_recive_top_frame, text=" You'll Receive",
                                                     font=customtkinter.CTkFont(size=25), image=self.dwonarrow_image,
                                                     compound="left", anchor="w")
        self.reciveam_lable.place(x=10, y=10)

        self.reciveam_lable2 = customtkinter.CTkLabel(self.in_home_recive_top_frame, text=self.reciveam,
                                                      font=customtkinter.CTkFont(size=25, weight="bold"))
        self.reciveam_lable2.place(x=10, y=60)

        self.totalrecive()
        self.caluclattotalsale(self.recivetotalamlist, self.totalreciveam, self.reciveam_lable2)

        # todo: home pay frame
        self.payam = StringVar()
        self.payam = "₹ 00.00"
        self.paytotalamlist = []
        self.totalpayam = []
        self.payam_lable = customtkinter.CTkLabel(self.in_home_pay_top_frame, text=" You'll Pay",
                                                     font=customtkinter.CTkFont(size=25), image=self.uparrow_image,
                                                     compound="left", anchor="w")
        self.payam_lable.place(x=10, y=10)

        self.payam_lable2 = customtkinter.CTkLabel(self.in_home_pay_top_frame, text=self.payam,
                                                      font=customtkinter.CTkFont(size=25, weight="bold"))
        self.payam_lable2.place(x=10, y=60)

        self.totalpay()
        self.caluclattotalsale(self.paytotalamlist, self.totalpayam, self.payam_lable2)

        # todo: home purches frame
        self.purchesam_lable = customtkinter.CTkLabel(self.in_home_purchase_top_frame, text=" Purchase",
                                                  font=customtkinter.CTkFont(size=25), image=self.basket_image,
                                                  compound="left", anchor="w")
        self.purchesam_lable.place(x=10, y=10)

        self.purchesam_lable2 = customtkinter.CTkLabel(self.in_home_purchase_top_frame, text=self.saleam,
                                                   font=customtkinter.CTkFont(size=25, weight="bold"))
        self.purchesam_lable2.place(x=10, y=60)


        # todo: home low Stock frame
        self.itemlowlist=[]
        self.lowStock_lable = customtkinter.CTkLabel(self.in_home_lowitem_top_frame, text=" Low Stock",text_color="red",
                                                      font=customtkinter.CTkFont(size=25), image=self.stock_image,
                                                      compound="left", anchor="w")
        self.lowStock_lable.place(x=10, y=10)

        self.lowStock_lable2 = customtkinter.CTkTextbox(self.in_home_lowitem_top_frame,width=350,
                                                       font=customtkinter.CTkFont(size=15))
        self.lowStock_lable2.place(x=25, y=50)
        self.getdate()
        self.getlowitem()


        # todo: parties frame
        self.var_searchby = StringVar()
        self.Var_searchtxt = StringVar()

        self.parties_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#e4e8ef")

        self.in_party_top_frame = customtkinter.CTkFrame(self.parties_frame, width=1720, height=100, fg_color="#ffffff")
        self.in_party_top_frame.place(x=10, y=10)

        self.party_name_frame = customtkinter.CTkFrame(self.parties_frame, width=500, height=860, fg_color="#ffffff")
        self.party_name_frame.place(x=10, y=120)

        self.party_detail_frame = customtkinter.CTkFrame(self.parties_frame, width=1210, height=150, fg_color="#ffffff")
        self.party_detail_frame.place(x=520, y=120)

        self.party_transiction_frame = customtkinter.CTkFrame(self.parties_frame, width=1210, height=700,
                                                              fg_color="#ffffff")
        self.party_transiction_frame.place(x=520, y=280)


        self.parties_search = customtkinter.CTkComboBox(self.party_name_frame, width=100, height=30,
                                                      values=["Select", "Name", "GSTIN", "Phone No."])
        self.parties_search.place(x=10, y=160)

        self.party_serch_entery=customtkinter.CTkEntry(self.party_name_frame,width=200,height=30,textvariable=self.Var_searchtxt)
        self.party_serch_entery.place(x=120,y=160)

        self.party_serch_button = customtkinter.CTkButton(self.party_name_frame, width=70, height=30,text="Search",command=self.patysearch)
        self.party_serch_button.place(x=330, y=160)

        self.party_clear_button = customtkinter.CTkButton(self.party_name_frame, width=70, height=30, text="Clear",
                                                          command=self.patyclear)
        self.party_clear_button.place(x=410, y=160)


        self.add_party_button = customtkinter.CTkButton(self.party_name_frame, command=self.addparty_event,
                                                        font=customtkinter.CTkFont(size=15), text="Add Party", width=70,
                                                        height=40, image=self.add_image, fg_color="transparent",
                                                        hover_color=("gray70", "gray30"))
        self.add_party_button.place(x=360, y=20)

        self.edit_party_button = customtkinter.CTkButton(self.party_name_frame, command=self.editparty_event,
                                                        font=customtkinter.CTkFont(size=15), text="Edit Party", width=70,
                                                        height=40, image=self.edit_image, fg_color="transparent",
                                                        hover_color=("gray70", "gray30"))
        self.edit_party_button.place(x=360, y=80)

        self.imp_party_button = customtkinter.CTkButton(self.party_name_frame, font=customtkinter.CTkFont(size=18),
                                                        text="Import Parties", width=70, height=40,
                                                        image=self.image_icon_image, fg_color="transparent",
                                                        hover_color=("gray70", "gray30"))
        self.imp_party_button.place(x=20, y=20)

        self.home_add_sale_button = customtkinter.CTkButton(self.in_party_top_frame,
                                                            font=customtkinter.CTkFont(size=18),
                                                            text="Add Sale", width=70, height=30,command=self.addsale_event,
                                                            image=self.bill_image,
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.home_add_sale_button.place(x=1310, y=20)

        self.home_add_purchess_button = customtkinter.CTkButton(self.in_party_top_frame,command=self.addpurchase_event,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add Purchess", width=70, height=30,
                                                                image=self.buy_image, text_color="black",
                                                                hover_color=("gray70", "gray30"),
                                                                fg_color="transparent")
        self.home_add_purchess_button.place(x=1440, y=20)

        self.home_setting_party_button = customtkinter.CTkButton(self.in_party_top_frame, width=30, height=30, text="",
                                                                 text_color="black", hover_color=("gray70", "gray30"),
                                                                 image=self.setting_image, fg_color="transparent")
        self.home_setting_party_button.place(x=1660, y=20)

        self.home_calculator_party_button = customtkinter.CTkButton(self.in_party_top_frame, width=30, height=30,
                                                                    text="",
                                                                    text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    image=self.calculator_image, fg_color="transparent",command=self.opencalcu)
        self.home_calculator_party_button.place(x=1610, y=20)

        self.lablename_party_lable = customtkinter.CTkLabel(self.in_party_top_frame,
                                                            font=customtkinter.CTkFont(size=18), text="Name",
                                                            width=1720, height=40, fg_color="#F28C28")
        self.lablename_party_lable.place(x=0, y=60)

        p_Frame = ttk.Frame(self.party_name_frame, relief=RIDGE)
        p_Frame.place(x=20, y=210, height=630)

        scrolly = ttk.Scrollbar(p_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(p_Frame, orient=HORIZONTAL)

        self.productTable = ttk.Treeview(p_Frame, columns=("party", "gstin", "pay", "receive"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading("party", text="Party")
        self.productTable.heading("gstin", text="GSTIN")
        self.productTable.heading("pay", text="Pay")
        self.productTable.heading("receive", text="Receive")
        self.productTable["show"] = "headings"
        self.productTable.column("party", width=130, )
        self.productTable.column("gstin", width=100)
        self.productTable.column("pay", width=100)
        self.productTable.column("receive", width=100)
        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

        self.partyname = StringVar()
        self.partynumber = StringVar()
        self.partyemail = StringVar()
        self.partycrlimit = StringVar()
        self.partyaddress = StringVar()
        self.partygstin = StringVar()

        self.party_name_lable = customtkinter.CTkLabel(self.party_detail_frame, textvariable=self.partyname,font=customtkinter.CTkFont(size=18), text_color="black")
        self.party_name_lable.place(x=15, y=10)

        self.party_number_lable = customtkinter.CTkLabel(self.party_detail_frame, textvariable=self.partynumber,font=customtkinter.CTkFont(size=12), text_color="black")
        self.party_number_lable.place(x=15, y=60)

        self.party_email_lable = customtkinter.CTkLabel(self.party_detail_frame, textvariable=self.partyemail,
                                                        font=customtkinter.CTkFont(size=12), text_color="black")
        self.party_email_lable.place(x=15, y=85)

        self.party_crlimit_lable = customtkinter.CTkLabel(self.party_detail_frame, textvariable=self.partycrlimit,
                                                          font=customtkinter.CTkFont(size=12), text_color="black")
        self.party_crlimit_lable.place(x=15, y=110)

        self.party_address_lable = customtkinter.CTkLabel(self.party_detail_frame, textvariable=self.partyaddress,
                                                          font=customtkinter.CTkFont(size=12), text_color="black")
        self.party_address_lable.place(x=1000, y=60)

        self.party_gstin_lable = customtkinter.CTkLabel(self.party_detail_frame, textvariable=self.partygstin,
                                                        font=customtkinter.CTkFont(size=12), text_color="black")
        self.party_gstin_lable.place(x=1000, y=85)

        self.party_gstin_lable = customtkinter.CTkLabel(self.party_transiction_frame, text="TRANSACTION",
                                                        font=customtkinter.CTkFont(size=14, ), text_color="black")
        self.party_gstin_lable.place(x=10, y=10)

        transiction_Frame = ttk.Frame(self.party_transiction_frame, relief=RIDGE)
        transiction_Frame.place(x=20, y=100, width=1170, height=580)

        scrolly = ttk.Scrollbar(transiction_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(transiction_Frame, orient=HORIZONTAL)

        self.transictionTable = ttk.Treeview(transiction_Frame,
                                             columns=("number", "date", "type", "total", "balance", "cheqno"),
                                             yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.transictionTable.xview)
        scrolly.config(command=self.transictionTable.yview)

        self.transictionTable.heading("number", text="Invoice Number")
        self.transictionTable.heading("date", text="Date")
        self.transictionTable.heading("type", text="Payment Type")
        self.transictionTable.heading("total", text="Total Amount")
        self.transictionTable.heading("balance", text="Received Amount")
        self.transictionTable.heading("cheqno", text="Cheque No.")
        self.transictionTable["show"] = "headings"
        self.transictionTable.column("number", width=150)
        self.transictionTable.column("date", width=150)
        self.transictionTable.column("type", width=100)
        self.transictionTable.column("total", width=200)
        self.transictionTable.column("balance", width=200)
        self.transictionTable.column("cheqno", width=100)
        self.transictionTable.pack(fill=BOTH, expand=1)
        self.transictionTable.bind("<ButtonRelease-1>", self.add_amount)

        self.var_trans_searchby = StringVar()
        self.Var_trans_searchtxt = StringVar()

        self.party_trans_search = customtkinter.CTkComboBox(self.party_transiction_frame, width=110, height=30,
                                                              values=["Select", "Invoice", "Date", "Payment Type","Cheque No."])
        self.party_trans_search.place(x=590, y=60)

        self.party_trans_serch_entery = customtkinter.CTkEntry(self.party_transiction_frame, width=300, height=30,
                                                               textvariable=self.Var_trans_searchtxt)
        self.party_trans_serch_entery.place(x=710, y=60)

        self.party_trans_serch_button = customtkinter.CTkButton(self.party_transiction_frame, width=70, height=30,
                                                                text="Search",
                                                                command=self.partytranssearch)
        self.party_trans_serch_button.place(x=1020, y=60)

        self.party_trans_clear_button = customtkinter.CTkButton(self.party_transiction_frame, width=70, height=30,
                                                                text="Clear",
                                                                command=self.patytransclear)
        self.party_trans_clear_button.place(x=1100, y=60)

        self.party_trans_Edit_button = customtkinter.CTkButton(self.party_transiction_frame, width=70, height=30,
                                                                text="Edit",
                                                                command=self.editparty_event)
        self.party_trans_Edit_button.place(x=20, y=60)


        # todo: item frame
        self.items_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.Vark_item_searchtxt = StringVar()

        self.in_item_top_frame = customtkinter.CTkFrame(self.items_frame, width=1720, height=100)
        self.in_item_top_frame.place(x=10, y=10)

        self.item_name_frame = customtkinter.CTkFrame(self.items_frame, width=500, height=860)
        self.item_name_frame.place(x=10, y=120)

        self.item_detail_frame = customtkinter.CTkFrame(self.items_frame, width=1210, height=150)
        self.item_detail_frame.place(x=520, y=120)

        self.item_transiction_frame = customtkinter.CTkFrame(self.items_frame, width=1210, height=700)
        self.item_transiction_frame.place(x=520, y=280)

        self.item_search = customtkinter.CTkComboBox(self.item_name_frame, width=100, height=30,
                                                        values=["Select", "Name", "Item Code", "HSN"])
        self.item_search.place(x=10, y=160)

        self.item_serch_entery = customtkinter.CTkEntry(self.item_name_frame, width=200, height=30,
                                                           textvariable=self.Vark_item_searchtxt)
        self.item_serch_entery.place(x=120, y=160)

        self.item_serch_button = customtkinter.CTkButton(self.item_name_frame, width=70, height=30, text="Search",command=self.itemsearch)
        self.item_serch_button.place(x=330, y=160)

        self.item_clear_button = customtkinter.CTkButton(self.item_name_frame, width=70, height=30, text="Clear",command=self.itemclear)
        self.item_clear_button.place(x=410, y=160)

        self.add_item_button = customtkinter.CTkButton(self.item_name_frame,
                                                          font=customtkinter.CTkFont(size=15), text="Add Item",command=self.additem_event,
                                                          width=70,
                                                          height=40, image=self.add_image, fg_color="transparent",
                                                          text_color="black",
                                                          hover_color=("gray70", "gray30"))
        self.add_item_button.place(x=360, y=20)

        self.imp_item_button = customtkinter.CTkButton(self.item_name_frame, font=customtkinter.CTkFont(size=18),
                                                          text="Import Items", width=70, height=40,
                                                          image=self.image_icon_image, fg_color="transparent",
                                                          text_color="black",
                                                          hover_color=("gray70", "gray30"))
        self.imp_item_button.place(x=20, y=20)

        self.edit_item_button = customtkinter.CTkButton(self.item_name_frame,
                                                       font=customtkinter.CTkFont(size=15), text="Edit Item",
                                                       command=self.edititem_event,
                                                       width=70,
                                                       height=40, image=self.edit_image, fg_color="transparent",
                                                       text_color="black",
                                                       hover_color=("gray70", "gray30"))
        self.edit_item_button.place(x=360, y=80)

        self.home_add_sale_button = customtkinter.CTkButton(self.in_item_top_frame,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.addsale_event,
                                                            text="Add Sale", width=70, height=30,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.home_add_sale_button.place(x=1310, y=20)

        self.home_add_items_button = customtkinter.CTkButton(self.in_item_top_frame,
                                                                command=self.addpurchase_event,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add items", width=70, height=30,
                                                                image=self.buy_image, text_color="black",
                                                                hover_color=("gray70", "gray30"),
                                                                fg_color="transparent")
        self.home_add_items_button.place(x=1440, y=20)

        self.home_setting_item_button = customtkinter.CTkButton(self.in_item_top_frame, width=30, height=30,
                                                                   text="",
                                                                   text_color="black", hover_color=("gray70", "gray30"),
                                                                   image=self.setting_image, fg_color="transparent")
        self.home_setting_item_button.place(x=1660, y=20)

        self.home_calculator_item_button = customtkinter.CTkButton(self.in_item_top_frame, width=30, height=30,
                                                                      text="",
                                                                      text_color="black",
                                                                      hover_color=("gray70", "gray30"),
                                                                      image=self.calculator_image,
                                                                      fg_color="transparent",
                                                                      command=self.opencalcu)
        self.home_calculator_item_button.place(x=1610, y=20)

        self.lablename_item_lable = customtkinter.CTkLabel(self.in_item_top_frame,
                                                              font=customtkinter.CTkFont(size=18), text="Name",
                                                              width=1720, height=40, fg_color="#F28C28")
        self.lablename_item_lable.place(x=0, y=60)

        m_Frame = ttk.Frame(self.item_name_frame, relief=RIDGE)
        m_Frame.place(x=20, y=210, height=630)

        scrolly = ttk.Scrollbar(m_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(m_Frame, orient=HORIZONTAL)

        self.itemTable = ttk.Treeview(m_Frame, columns=("itemname", "hsn", "itemcode", "openqty"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.itemTable.xview)
        scrolly.config(command=self.itemTable.yview)
        self.itemTable.heading("itemname", text="Name")
        self.itemTable.heading("hsn", text="HSN")
        self.itemTable.heading("itemcode", text="Item Code")
        self.itemTable.heading("openqty", text="Stock")

        self.itemTable["show"] = "headings"

        self.itemTable.column("itemname", width=130, )
        self.itemTable.column("hsn", width=100)
        self.itemTable.column("itemcode", width=100)
        self.itemTable.column("openqty", width=100)

        self.itemTable.pack(fill=BOTH, expand=1)
        self.itemTable.bind("<ButtonRelease-1>",self.get_itemtrans_data)

        self.itemshow()

        self.itemname = StringVar()
        self.itemnumber = StringVar()
        self.itememail = StringVar()
        self.itemcrlimit = StringVar()
        self.itemaddress = StringVar()
        self.itemgstin = StringVar()
        self.itemstock = StringVar()
        self.itemstockprice = StringVar()
        self.itempurchase = StringVar()

        self.item_name_lable = customtkinter.CTkLabel(self.item_detail_frame, textvariable=self.itemname,
                                                         font=customtkinter.CTkFont(size=18))
        self.item_name_lable.place(x=15, y=10)

        self.item_number_lable = customtkinter.CTkLabel(self.item_detail_frame, textvariable=self.itemnumber,
                                                           font=customtkinter.CTkFont(size=12))
        self.item_number_lable.place(x=15, y=60)

        self.item_email_lable = customtkinter.CTkLabel(self.item_detail_frame, textvariable=self.itememail,
                                                          font=customtkinter.CTkFont(size=12))
        self.item_email_lable.place(x=15, y=85)

        self.item_crlimit_lable = customtkinter.CTkLabel(self.item_detail_frame, textvariable=self.itemcrlimit,
                                                            font=customtkinter.CTkFont(size=12))
        self.item_crlimit_lable.place(x=15, y=110)

        self.item_address_lable = customtkinter.CTkLabel(self.item_detail_frame, textvariable=self.itemaddress,
                                                            font=customtkinter.CTkFont(size=12))
        self.item_address_lable.place(x=1000, y=60)

        self.item_gstin_lable = customtkinter.CTkLabel(self.item_detail_frame, textvariable=self.itemgstin,
                                                          font=customtkinter.CTkFont(size=12))
        self.item_gstin_lable.place(x=1000, y=85)

        self.item_stock_lable = customtkinter.CTkLabel(self.item_detail_frame, textvariable=self.itemstock,
                                                          font=customtkinter.CTkFont(size=15))
        self.item_stock_lable.place(x=1000, y=10)

        self.item_stock_price_lable = customtkinter.CTkLabel(self.item_detail_frame, textvariable=self.itemstockprice,
                                                       font=customtkinter.CTkFont(size=13))
        self.item_stock_price_lable.place(x=1000, y=35)

        self.item_purchase_lable = customtkinter.CTkLabel(self.item_detail_frame, textvariable=self.itempurchase,
                                                          font=customtkinter.CTkFont(size=12))
        self.item_purchase_lable.place(x=1000, y=110)

        self.item_gstin_lable = customtkinter.CTkLabel(self.item_transiction_frame, text="TRANSACTION",
                                                          font=customtkinter.CTkFont(size=14, ))
        self.item_gstin_lable.place(x=10, y=10)

        transiction_Frame = ttk.Frame(self.item_transiction_frame, relief=RIDGE)
        transiction_Frame.place(x=20, y=100, width=1170, height=580)

        scrolly = ttk.Scrollbar(transiction_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(transiction_Frame, orient=HORIZONTAL)

        self.itemtransictionTable = ttk.Treeview(transiction_Frame,
                                                    columns=("number", "date", "type", "total", "balance", "cheqno"),
                                                    yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.itemtransictionTable.xview)
        scrolly.config(command=self.itemtransictionTable.yview)

        self.itemtransictionTable.heading("number", text="Invoice Number")
        self.itemtransictionTable.heading("date", text="Date")
        self.itemtransictionTable.heading("type", text="Payment Type")
        self.itemtransictionTable.heading("total", text="Total Amount")
        self.itemtransictionTable.heading("balance", text="Received Amount")
        self.itemtransictionTable.heading("cheqno", text="Cheque No.")

        self.itemtransictionTable["show"] = "headings"

        self.itemtransictionTable.column("number", width=150)
        self.itemtransictionTable.column("date", width=150)
        self.itemtransictionTable.column("type", width=100)
        self.itemtransictionTable.column("total", width=200)
        self.itemtransictionTable.column("balance", width=200)
        self.itemtransictionTable.column("cheqno", width=100)

        self.itemtransictionTable.pack(fill=BOTH, expand=1)
        self.itemtransictionTable.bind("<ButtonRelease-1>", self.add_itemamount)

        self.var_pur_searchby = StringVar()
        self.Var_pur_searchtxt = StringVar()

        self.item_pur_search = customtkinter.CTkComboBox(self.item_transiction_frame, width=110, height=30,
                                                            values=["Select", "Invoice", "Date", "Payment Type",
                                                                    "Cheque No."])
        self.item_pur_search.place(x=590, y=60)

        self.item_pur_serch_entery = customtkinter.CTkEntry(self.item_transiction_frame, width=300, height=30,textvariable=self.Var_pur_searchtxt)
        self.item_pur_serch_entery.place(x=710, y=60)

        self.item_pur_serch_button = customtkinter.CTkButton(self.item_transiction_frame, width=70, height=30,text="Search",command=self.itemtranssearch)
        self.item_pur_serch_button.place(x=1020, y=60)

        self.item_pur_clear_button = customtkinter.CTkButton(self.item_transiction_frame, width=70, height=30,
                                                                text="Clear",
                                                                command=self.itemctranslear)
        self.item_pur_clear_button.place(x=1100, y=60)

        self.item_trans_Edit_button = customtkinter.CTkButton(self.item_transiction_frame, width=70, height=30,
                                                               text="Edit",
                                                               command=self.edititem_event)
        self.item_trans_Edit_button.place(x=20, y=60)


        # todo : GST sale frame
        self.gstsale_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.in_gstsale_top_frame = customtkinter.CTkFrame(self.gstsale_frame, width=1720, height=100)
        self.in_gstsale_top_frame.place(x=10, y=10)

        self.gstsale_detail_frame = customtkinter.CTkFrame(self.gstsale_frame, width=1720, height=150)
        self.gstsale_detail_frame.place(x=10, y=120)

        self.gstsale_detail_frame1 = customtkinter.CTkFrame(self.gstsale_detail_frame, width=200, height=80,
                                                            fg_color="#b9f3e7")
        self.gstsale_detail_frame1.place(x=20, y=60)
        self.gstsale_detail_frame2 = customtkinter.CTkFrame(self.gstsale_detail_frame, width=200, height=80,
                                                            fg_color="#cfe6fe")
        self.gstsale_detail_frame2.place(x=260, y=60)
        self.gstsale_detail_frame3 = customtkinter.CTkFrame(self.gstsale_detail_frame, width=200, height=80,
                                                            fg_color="#f8c888")
        self.gstsale_detail_frame3.place(x=500, y=60)

        self.gstsale_detail_paid_lable = customtkinter.CTkLabel(self.gstsale_detail_frame1,
                                                                font=customtkinter.CTkFont(size=20), text="Paid",
                                                                text_color="black")
        self.gstsale_detail_paid_lable.place(x=20, y=10)

        self.gstsale_detail_unpaid_lable = customtkinter.CTkLabel(self.gstsale_detail_frame2,
                                                                  font=customtkinter.CTkFont(size=20), text="Unpaid",
                                                                  text_color="black")
        self.gstsale_detail_unpaid_lable.place(x=20, y=10)

        self.gstsale_detail_total_lable = customtkinter.CTkLabel(self.gstsale_detail_frame3,
                                                                 font=customtkinter.CTkFont(size=20), text="Total",
                                                                 text_color="black")
        self.gstsale_detail_total_lable.place(x=20, y=10)
        self.gstsale_paidamount = StringVar()
        self.gstsale_unpaidamount = StringVar()
        self.gstsale_totalamount = StringVar()
        self.gstsale_paidamount = "₹00.00"
        self.gstsale_unpaidamount = "₹00.00"
        self.gstsale_totalamount = "₹00.00"

        self.gstsale_paidamount_list = []
        self.gstsale_unpaidamount_list = []
        self.gstsale_totalamount_list = []

        self.gstsale_detail_paid_amount_lable = customtkinter.CTkLabel(self.gstsale_detail_frame1,
                                                                       font=customtkinter.CTkFont(size=25,
                                                                                                  weight="bold"),
                                                                       text=self.gstsale_paidamount,
                                                                       text_color="black")
        self.gstsale_detail_paid_amount_lable.place(x=20, y=40)

        self.gstsale_detail_unpaid_amount_lable = customtkinter.CTkLabel(self.gstsale_detail_frame2,
                                                                         font=customtkinter.CTkFont(size=25,
                                                                                                    weight="bold"),
                                                                         text=self.gstsale_unpaidamount,
                                                                         text_color="black")
        self.gstsale_detail_unpaid_amount_lable.place(x=20, y=40)

        self.gstsale_detail_total_amount_lable = customtkinter.CTkLabel(self.gstsale_detail_frame3,
                                                                        font=customtkinter.CTkFont(size=25,
                                                                                                   weight="bold"),
                                                                        text=self.gstsale_totalamount,
                                                                        text_color="black")
        self.gstsale_detail_total_amount_lable.place(x=20, y=40)

        self.gstsale_detail_plus_lable = customtkinter.CTkLabel(self.gstsale_detail_frame,
                                                                font=customtkinter.CTkFont(size=25), text="+")
        self.gstsale_detail_plus_lable.place(x=235, y=85)

        self.gstsale_detail_equal_lable = customtkinter.CTkLabel(self.gstsale_detail_frame,
                                                                 font=customtkinter.CTkFont(size=25), text="=")
        self.gstsale_detail_equal_lable.place(x=475, y=85)

        self.gstsale_transiction_frame = customtkinter.CTkFrame(self.gstsale_frame, width=1720, height=700)
        self.gstsale_transiction_frame.place(x=10, y=280)

        self.submenu_gstsale_lable = customtkinter.CTkFrame(self.in_gstsale_top_frame, width=1720, height=40,
                                                            fg_color="transparent")
        self.submenu_gstsale_lable.place(x=0, y=60)

        self.gstsale_estimate_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.gstsale_payment_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.gstsale_order_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.gstsale_Delivery_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.gstsale_return_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.gstsale_invoice_button = customtkinter.CTkButton(self.submenu_gstsale_lable,
                                                              font=customtkinter.CTkFont(size=18),
                                                              command=self.gst_sale_button_event,
                                                              text="Sale Invoice", width=70, height=20,
                                                              image=self.bill_image, text_color="black",
                                                              hover_color=("gray70", "gray30"), fg_color="transparent")
        self.gstsale_invoice_button.place(x=10, y=0)

        self.gstsale_estimate_button = customtkinter.CTkButton(self.submenu_gstsale_lable,
                                                               font=customtkinter.CTkFont(size=18),
                                                               command=self.gstsale_estimate_event,
                                                               text="Sale Estimate", width=70, height=20,
                                                               image=self.bill_image, text_color="black",
                                                               hover_color=("gray70", "gray30"), fg_color="transparent")
        self.gstsale_estimate_button.place(x=180, y=0)

        self.gstsale_payment_button = customtkinter.CTkButton(self.submenu_gstsale_lable,
                                                              font=customtkinter.CTkFont(size=18),
                                                              command=self.gstsale_payment_event,
                                                              text="Payment In", width=70, height=20,
                                                              image=self.bill_image, text_color="black",
                                                              hover_color=("gray70", "gray30"), fg_color="transparent")
        self.gstsale_payment_button.place(x=360, y=0)

        self.gstsale_order_button = customtkinter.CTkButton(self.submenu_gstsale_lable,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.gstsale_order_event,
                                                            text="Sale Order", width=70, height=20,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.gstsale_order_button.place(x=520, y=0)

        self.gstsale_chalan_button = customtkinter.CTkButton(self.submenu_gstsale_lable,
                                                             font=customtkinter.CTkFont(size=18),
                                                             command=self.gstsale_delivery_event,
                                                             text="Delivery Challan", width=70, height=20,
                                                             image=self.bill_image, text_color="black",
                                                             hover_color=("gray70", "gray30"), fg_color="transparent")
        self.gstsale_chalan_button.place(x=680, y=0)

        self.gstsale_return_button = customtkinter.CTkButton(self.submenu_gstsale_lable,
                                                             font=customtkinter.CTkFont(size=18),
                                                             command=self.gstsale_return_event,
                                                             text="Sale Return", width=70, height=20,
                                                             image=self.bill_image, text_color="black",
                                                             hover_color=("gray70", "gray30"), fg_color="transparent")
        self.gstsale_return_button.place(x=880, y=0)

        self.gstsale_add_gstsale_button = customtkinter.CTkButton(self.in_gstsale_top_frame,
                                                                  font=customtkinter.CTkFont(size=18),
                                                                  command=self.addgstsale_event,
                                                                  text="Add Sale", width=70, height=30,
                                                                  image=self.bill_image, text_color="black",
                                                                  hover_color=("gray70", "gray30"),
                                                                  fg_color="transparent")
        self.gstsale_add_gstsale_button.place(x=1310, y=20)

        self.gstsale_add_purchess_button = customtkinter.CTkButton(self.in_gstsale_top_frame,
                                                                   command=self.addpurchase_event,
                                                                   font=customtkinter.CTkFont(size=18),
                                                                   text="Add Purchess", width=70, height=30,
                                                                   image=self.buy_image, text_color="black",
                                                                   hover_color=("gray70", "gray30"),
                                                                   fg_color="transparent")
        self.gstsale_add_purchess_button.place(x=1440, y=20)

        self.gstsale_setting_purches_button = customtkinter.CTkButton(self.in_gstsale_top_frame, width=30, height=30,
                                                                      text="",
                                                                      text_color="black",
                                                                      hover_color=("gray70", "gray30"),
                                                                      image=self.setting_image, fg_color="transparent")
        self.gstsale_setting_purches_button.place(x=1660, y=20)

        self.gstsale_calculator_purches_button = customtkinter.CTkButton(self.in_gstsale_top_frame, width=30, height=30,
                                                                         text="",
                                                                         text_color="black",
                                                                         hover_color=("gray70", "gray30"),
                                                                         image=self.calculator_image,
                                                                         fg_color="transparent",
                                                                         command=self.opencalcu)
        self.gstsale_calculator_purches_button.place(x=1610, y=20)

        # self.calgetsaletotalamount()
        self.involista3 = []

        transiction_Frame = ttk.Frame(self.gstsale_transiction_frame, relief=RIDGE)
        transiction_Frame.place(x=20, y=100, width=1680, height=580)

        scrolly = ttk.Scrollbar(transiction_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(transiction_Frame, orient=HORIZONTAL)

        self.gstsaletransictionTable = ttk.Treeview(transiction_Frame,
                                                    columns=(
                                                        "date", "invonumber", "name", "type", "total", "balance",
                                                        "cheqno"),
                                                    yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.gstsaletransictionTable.xview)
        scrolly.config(command=self.gstsaletransictionTable.yview)

        self.gstsaletransictionTable.heading("date", text="Date")
        self.gstsaletransictionTable.heading("invonumber", text="Invoice Number")
        self.gstsaletransictionTable.heading("name", text="Party Name")
        self.gstsaletransictionTable.heading("type", text="Payment Type")
        self.gstsaletransictionTable.heading("total", text="Total Amount")
        self.gstsaletransictionTable.heading("balance", text="Received Amount")
        self.gstsaletransictionTable.heading("cheqno", text="Cheque No.")
        self.gstsaletransictionTable["show"] = "headings"
        self.gstsaletransictionTable.column("date", width=150, anchor="center")
        self.gstsaletransictionTable.column("invonumber", width=150, anchor="center")
        self.gstsaletransictionTable.column("name", width=200, anchor="center")
        self.gstsaletransictionTable.column("type", width=100, anchor="center")
        self.gstsaletransictionTable.column("total", width=200, anchor="center")
        self.gstsaletransictionTable.column("balance", width=200, anchor="center")
        self.gstsaletransictionTable.column("cheqno", width=150, anchor="center")

        self.gstsaletransictionTable.pack(fill=BOTH, expand=1)
        self.gstsaletransictionTable.bind("<ButtonRelease-1>", self.gstsaledataget)

        self.gstsaletrans()

        self.Var_gstsale_searchtxt = StringVar()

        self.gstsale_pur_lable = customtkinter.CTkLabel(self.gstsale_transiction_frame,
                                                        font=customtkinter.CTkFont(size=25),
                                                        text="Transition")
        self.gstsale_pur_lable.place(x=20, y=20)

        self.gstsale_add_gstsale_button = customtkinter.CTkButton(self.gstsale_transiction_frame, width=70, height=30,
                                                                  text="Add Sale", command=self.addgstsale_event)
        self.gstsale_add_gstsale_button.place(x=20, y=60)

        self.gstsale_pur_search = customtkinter.CTkComboBox(self.gstsale_transiction_frame, width=110, height=30,
                                                            values=["Select", "Invoice", "Date", "Payment Type",
                                                                    "Cheque No.", "Name"])
        self.gstsale_pur_search.place(x=1120, y=60)

        self.gstsale_pur_serch_entery = customtkinter.CTkEntry(self.gstsale_transiction_frame, width=300, height=30,
                                                               textvariable=self.Var_gstsale_searchtxt)
        self.gstsale_pur_serch_entery.place(x=1240, y=60)

        self.gstsale_pur_serch_button = customtkinter.CTkButton(self.gstsale_transiction_frame, width=70, height=30,
                                                                text="Search", command=self.gstsalestranssearch)
        self.gstsale_pur_serch_button.place(x=1550, y=60)

        self.gstsale_pur_clear_button = customtkinter.CTkButton(self.gstsale_transiction_frame, width=70, height=30,
                                                                text="Clear", command=self.gstsaletransclear)
        self.gstsale_pur_clear_button.place(x=1630, y=60)

        self.gstsale_pur_edit_button = customtkinter.CTkButton(self.gstsale_transiction_frame, width=70, height=30,
                                                               text="Edit", command=self.editgstsale_event)
        self.gstsale_pur_edit_button.place(x=100, y=60)


        # todo: sale frame
        self.sale_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.in_sale_top_frame = customtkinter.CTkFrame(self.sale_frame, width=1720, height=100)
        self.in_sale_top_frame.place(x=10, y=10)

        self.sale_detail_frame = customtkinter.CTkFrame(self.sale_frame, width=1720, height=150)
        self.sale_detail_frame.place(x=10, y=120)

        self.sale_detail_frame1 = customtkinter.CTkFrame(self.sale_detail_frame, width=200, height=80,fg_color="#b9f3e7")
        self.sale_detail_frame1.place(x=20, y=60)
        self.sale_detail_frame2 = customtkinter.CTkFrame(self.sale_detail_frame, width=200, height=80,fg_color="#cfe6fe")
        self.sale_detail_frame2.place(x=260, y=60)
        self.sale_detail_frame3 = customtkinter.CTkFrame(self.sale_detail_frame, width=200, height=80,fg_color="#f8c888")
        self.sale_detail_frame3.place(x=500, y=60)

        self.sale_detail_paid_lable = customtkinter.CTkLabel(self.sale_detail_frame1,
                                                              font=customtkinter.CTkFont(size=20), text="Paid",text_color="black")
        self.sale_detail_paid_lable.place(x=20, y=10)

        self.sale_detail_unpaid_lable = customtkinter.CTkLabel(self.sale_detail_frame2,
                                                             font=customtkinter.CTkFont(size=20), text="Unpaid",
                                                             text_color="black")
        self.sale_detail_unpaid_lable.place(x=20, y=10)

        self.sale_detail_total_lable = customtkinter.CTkLabel(self.sale_detail_frame3,
                                                               font=customtkinter.CTkFont(size=20), text="Total",
                                                               text_color="black")
        self.sale_detail_total_lable.place(x=20, y=10)
        self.sale_paidamount=StringVar()
        self.sale_unpaidamount = StringVar()
        self.sale_totalamount = StringVar()
        self.sale_paidamount = "₹00.00"
        self.sale_unpaidamount = "₹00.00"
        self.sale_totalamount = "₹00.00"

        self.sale_paidamount_list = []
        self.sale_unpaidamount_list = []
        self.sale_totalamount_list = []

        self.sale_detail_paid_amount_lable = customtkinter.CTkLabel(self.sale_detail_frame1,
                                                             font=customtkinter.CTkFont(size=25,weight="bold"), text=self.sale_paidamount,
                                                             text_color="black")
        self.sale_detail_paid_amount_lable.place(x=20, y=40)

        self.sale_detail_unpaid_amount_lable = customtkinter.CTkLabel(self.sale_detail_frame2,
                                                               font=customtkinter.CTkFont(size=25,weight="bold"), text=self.sale_unpaidamount,
                                                               text_color="black")
        self.sale_detail_unpaid_amount_lable.place(x=20, y=40)

        self.sale_detail_total_amount_lable = customtkinter.CTkLabel(self.sale_detail_frame3,
                                                              font=customtkinter.CTkFont(size=25,weight="bold"), text=self.sale_totalamount,
                                                              text_color="black")
        self.sale_detail_total_amount_lable.place(x=20, y=40)

        self.sale_detail_plus_lable = customtkinter.CTkLabel(self.sale_detail_frame,font=customtkinter.CTkFont(size=25),text="+")
        self.sale_detail_plus_lable.place(x=235, y=85)

        self.sale_detail_equal_lable = customtkinter.CTkLabel(self.sale_detail_frame,
                                                             font=customtkinter.CTkFont(size=25), text="=")
        self.sale_detail_equal_lable.place(x=475, y=85)

        self.sale_transiction_frame = customtkinter.CTkFrame(self.sale_frame, width=1720, height=700)
        self.sale_transiction_frame.place(x=10, y=280)

        self.submenu_sale_lable = customtkinter.CTkFrame(self.in_sale_top_frame, width=1720, height=40,
                                                         fg_color="transparent")
        self.submenu_sale_lable.place(x=0, y=60)

        self.sale_estimate_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sale_payment_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sale_order_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sale_Delivery_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sale_return_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.sale_invoice_button = customtkinter.CTkButton(self.submenu_sale_lable,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.sale_button_event,
                                                            text="Sale Invoice", width=70, height=20,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_invoice_button.place(x=10, y=0)

        self.sale_estimate_button = customtkinter.CTkButton(self.submenu_sale_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_estimate_event,
                                                           text="Sale Estimate", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_estimate_button.place(x=180, y=0)

        self.sale_payment_button = customtkinter.CTkButton(self.submenu_sale_lable,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.sale_payment_event,
                                                            text="Payment In", width=70, height=20,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_payment_button.place(x=360, y=0)

        self.sale_order_button = customtkinter.CTkButton(self.submenu_sale_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_order_event,
                                                           text="Sale Order", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_order_button.place(x=520, y=0)

        self.sale_chalan_button = customtkinter.CTkButton(self.submenu_sale_lable,
                                                         font=customtkinter.CTkFont(size=18),
                                                         command=self.sale_delivery_event,
                                                         text="Delivery Challan", width=70, height=20,
                                                         image=self.bill_image, text_color="black",
                                                         hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_chalan_button.place(x=680, y=0)

        self.sale_return_button = customtkinter.CTkButton(self.submenu_sale_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_return_event,
                                                          text="Sale Return", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_return_button.place(x=880, y=0)

        self.sale_add_sale_button = customtkinter.CTkButton(self.in_sale_top_frame,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.addsale_event,
                                                            text="Add Sale", width=70, height=30,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_add_sale_button.place(x=1310, y=20)

        self.sale_add_purchess_button = customtkinter.CTkButton(self.in_sale_top_frame,
                                                                command=self.addpurchase_event,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add Purchess", width=70, height=30,
                                                                image=self.buy_image, text_color="black",
                                                                hover_color=("gray70", "gray30"),
                                                                fg_color="transparent")
        self.sale_add_purchess_button.place(x=1440, y=20)

        self.sale_setting_purches_button = customtkinter.CTkButton(self.in_sale_top_frame, width=30, height=30,
                                                                   text="",
                                                                   text_color="black", hover_color=("gray70", "gray30"),
                                                                   image=self.setting_image, fg_color="transparent")
        self.sale_setting_purches_button.place(x=1660, y=20)

        self.sale_calculator_purches_button = customtkinter.CTkButton(self.in_sale_top_frame, width=30, height=30,
                                                                      text="",
                                                                      text_color="black",
                                                                      hover_color=("gray70", "gray30"),
                                                                      image=self.calculator_image,
                                                                      fg_color="transparent",
                                                                      command=self.opencalcu)
        self.sale_calculator_purches_button.place(x=1610, y=20)

        self.calgetsaletotalamount()
        self.involista1=[]

        transiction_Frame = ttk.Frame(self.sale_transiction_frame, relief=RIDGE)
        transiction_Frame.place(x=20, y=100, width=1680, height=580)

        scrolly = ttk.Scrollbar(transiction_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(transiction_Frame, orient=HORIZONTAL)

        self.saletransictionTable = ttk.Treeview(transiction_Frame,
                                                 columns=("date","invonumber","name", "type", "total", "balance", "cheqno"),
                                                 yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.saletransictionTable.xview)
        scrolly.config(command=self.saletransictionTable.yview)

        self.saletransictionTable.heading("date", text="Date")
        self.saletransictionTable.heading("invonumber", text="Invoice Number")
        self.saletransictionTable.heading("name", text="Party Name")
        self.saletransictionTable.heading("type", text="Payment Type")
        self.saletransictionTable.heading("total", text="Total Amount")
        self.saletransictionTable.heading("balance", text="Received Amount")
        self.saletransictionTable.heading("cheqno", text="Cheque No.")

        self.saletransictionTable["show"] = "headings"

        self.saletransictionTable.column("date", width=150,anchor="center")
        self.saletransictionTable.column("invonumber", width=150,anchor="center")
        self.saletransictionTable.column("name", width=200,anchor="center")
        self.saletransictionTable.column("type", width=100,anchor="center")
        self.saletransictionTable.column("total", width=200,anchor="center")
        self.saletransictionTable.column("balance", width=200,anchor="center")
        self.saletransictionTable.column("cheqno", width=150,anchor="center")

        self.saletransictionTable.pack(fill=BOTH, expand=1)
        self.saletransictionTable.bind("<ButtonRelease-1>",self.saledataget)

        self.saletrans()

        self.Var_sale_searchtxt = StringVar()

        self.sale_pur_lable = customtkinter.CTkLabel(self.sale_transiction_frame,font=customtkinter.CTkFont(size=25),text="Transition")
        self.sale_pur_lable.place(x=20, y=20)

        self.sale_add_sale_button = customtkinter.CTkButton(self.sale_transiction_frame, width=70, height=30,
                                                             text="Add Sale", command=self.addsale_event)
        self.sale_add_sale_button.place(x=20, y=60)

        self.sale_pur_search = customtkinter.CTkComboBox(self.sale_transiction_frame, width=110, height=30,
                                                         values=["Select", "Invoice", "Date", "Payment Type",
                                                                 "Cheque No.","Name"])
        self.sale_pur_search.place(x=1120, y=60)

        self.sale_pur_serch_entery = customtkinter.CTkEntry(self.sale_transiction_frame, width=300, height=30,
                                                            textvariable=self.Var_sale_searchtxt)
        self.sale_pur_serch_entery.place(x=1240, y=60)

        self.sale_pur_serch_button = customtkinter.CTkButton(self.sale_transiction_frame, width=70, height=30,
                                                             text="Search",command=self.salestranssearch )
        self.sale_pur_serch_button.place(x=1550, y=60)

        self.sale_pur_clear_button = customtkinter.CTkButton(self.sale_transiction_frame, width=70, height=30,
                                                             text="Clear",command=self.saletransclear)
        self.sale_pur_clear_button.place(x=1630, y=60)

        self.sale_pur_edit_button = customtkinter.CTkButton(self.sale_transiction_frame, width=70, height=30,
                                                             text="Edit", command=self.editsale_event)
        self.sale_pur_edit_button.place(x=100, y=60)


        #todo:sale estimate
        self.in_sale_estimate_top_frame = customtkinter.CTkFrame(self.sale_estimate_frame, width=1720, height=100)
        self.in_sale_estimate_top_frame.place(x=10, y=10)

        self.saleestimate_add_sale_button = customtkinter.CTkButton(self.in_sale_estimate_top_frame,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.addsale_event,
                                                            text="Add Sale", width=70, height=30,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.saleestimate_add_sale_button.place(x=1310, y=20)

        self.sale_add_estimate_button = customtkinter.CTkButton(self.in_sale_estimate_top_frame,
                                                                command=self.addpurchase_event,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add Purchess", width=70, height=30,
                                                                image=self.buy_image, text_color="black",
                                                                hover_color=("gray70", "gray30"),
                                                                fg_color="transparent")
        self.sale_add_estimate_button.place(x=1440, y=20)

        self.sale_setting_estimate_button = customtkinter.CTkButton(self.in_sale_estimate_top_frame, width=30, height=30,
                                                                   text="",
                                                                   text_color="black", hover_color=("gray70", "gray30"),
                                                                   image=self.setting_image, fg_color="transparent")
        self.sale_setting_estimate_button.place(x=1660, y=20)

        self.sale_calculator_estimate_button = customtkinter.CTkButton(self.in_sale_estimate_top_frame, width=30, height=30,
                                                                      text="",
                                                                      text_color="black",
                                                                      hover_color=("gray70", "gray30"),
                                                                      image=self.calculator_image,
                                                                      fg_color="transparent",
                                                                      command=self.opencalcu)
        self.sale_calculator_estimate_button.place(x=1610, y=20)

        self.submenu_sale_estimate_lable = customtkinter.CTkFrame(self.in_sale_estimate_top_frame, width=1720, height=40,
                                                         fg_color="transparent")
        self.submenu_sale_estimate_lable.place(x=0, y=60)

        self.sale_invoice_button = customtkinter.CTkButton(self.submenu_sale_estimate_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_button_event,
                                                           text="Sale Invoice", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_invoice_button.place(x=10, y=0)

        self.sale_estimate_button = customtkinter.CTkButton(self.submenu_sale_estimate_lable,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.sale_estimate_event,
                                                            text="Sale Estimate", width=70, height=20,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_estimate_button.place(x=180, y=0)

        self.sale_payment_button = customtkinter.CTkButton(self.submenu_sale_estimate_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_payment_event,
                                                           text="Payment In", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_payment_button.place(x=360, y=0)

        self.sale_order_button = customtkinter.CTkButton(self.submenu_sale_estimate_lable,
                                                         font=customtkinter.CTkFont(size=18),
                                                         command=self.sale_order_event,
                                                         text="Sale Order", width=70, height=20,
                                                         image=self.bill_image, text_color="black",
                                                         hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_order_button.place(x=520, y=0)

        self.sale_chalan_button = customtkinter.CTkButton(self.submenu_sale_estimate_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_delivery_event,
                                                          text="Delivery Challan", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_chalan_button.place(x=680, y=0)

        self.sale_return_button = customtkinter.CTkButton(self.submenu_sale_estimate_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_return_event,
                                                          text="Sale Return", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_return_button.place(x=880, y=0)

        self.estimatee_sale_detail_frame = customtkinter.CTkFrame(self.sale_estimate_frame, width=1720, height=150)
        self.estimatee_sale_detail_frame.place(x=10, y=120)


        self.estimatee_sale_detail_frame3 = customtkinter.CTkFrame(self.estimatee_sale_detail_frame, width=200, height=80,
                                                         fg_color="#f8c888")
        self.estimatee_sale_detail_frame3.place(x=20, y=60)


        self.estimatee_sale_detail_total_lable = customtkinter.CTkLabel(self.estimatee_sale_detail_frame3,
                                                              font=customtkinter.CTkFont(size=20), text="Total E Amount",
                                                              text_color="black")
        self.estimatee_sale_detail_total_lable.place(x=20, y=10)
        self.estimatee_sale_paidamount = StringVar()
        self.estimatee_sale_unpaidamount = StringVar()
        self.estimatee_sale_totalamount = StringVar()
        self.estimatee_sale_totalamount = "₹00.00"

        self.estimatee_sale_paidamount_list = []
        self.estimatee_sale_unpaidamount_list = []
        self.estimatee_sale_totalamount_list = []


        self.estimatee_sale_detail_total_amount_lable = customtkinter.CTkLabel(self.estimatee_sale_detail_frame3,
                                                                     font=customtkinter.CTkFont(size=25, weight="bold"),
                                                                     text=self.estimatee_sale_totalamount,
                                                                     text_color="black")
        self.estimatee_sale_detail_total_amount_lable.place(x=20, y=40)



        self.sale_estimate_transiction_frame = customtkinter.CTkFrame(self.sale_estimate_frame, width=1720, height=700)
        self.sale_estimate_transiction_frame.place(x=10, y=280)

        transiction_estimate_Frame = ttk.Frame(self.sale_estimate_transiction_frame, relief=RIDGE)
        transiction_estimate_Frame.place(x=20, y=100, width=1680, height=580)

        scrolly = ttk.Scrollbar(transiction_estimate_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(transiction_estimate_Frame, orient=HORIZONTAL)

        self.sale_estimatetransictionTable = ttk.Treeview(transiction_estimate_Frame,
                                                 columns=(
                                                 "date", "invonumber", "name", "type", "total", "balance", "cheqno"),
                                                 yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.sale_estimatetransictionTable.xview)
        scrolly.config(command=self.sale_estimatetransictionTable.yview)

        self.sale_estimatetransictionTable.heading("date", text="Date")
        self.sale_estimatetransictionTable.heading("invonumber", text="Invoice Number")
        self.sale_estimatetransictionTable.heading("name", text="Party Name")
        self.sale_estimatetransictionTable.heading("type", text="Payment Type")
        self.sale_estimatetransictionTable.heading("total", text="Total Amount")
        self.sale_estimatetransictionTable.heading("balance", text="Received Amount")
        self.sale_estimatetransictionTable.heading("cheqno", text="Cheque No.")

        self.sale_estimatetransictionTable["show"] = "headings"

        self.sale_estimatetransictionTable.column("date", width=150, anchor="center")
        self.sale_estimatetransictionTable.column("invonumber", width=150, anchor="center")
        self.sale_estimatetransictionTable.column("name", width=200, anchor="center")
        self.sale_estimatetransictionTable.column("type", width=100, anchor="center")
        self.sale_estimatetransictionTable.column("total", width=200, anchor="center")
        self.sale_estimatetransictionTable.column("balance", width=200, anchor="center")
        self.sale_estimatetransictionTable.column("cheqno", width=150, anchor="center")

        self.sale_estimatetransictionTable.pack(fill=BOTH, expand=1)
        self.sale_estimatetransictionTable.bind("<ButtonRelease-1>", self.saleestimatetrans)


        self.Var_sale_estimate_searchtxt = StringVar()

        self.sale_pur_lable = customtkinter.CTkLabel(self.sale_estimate_transiction_frame, font=customtkinter.CTkFont(size=25),
                                                     text="Transition")
        self.sale_pur_lable.place(x=20, y=20)

        self.sale_add_sale_button = customtkinter.CTkButton(self.sale_estimate_transiction_frame, width=70, height=30,
                                                            text="Add Estimate", command=self.addestimate_event)
        self.sale_add_sale_button.place(x=1600, y=10)

        self.sale_estimate_pur_search = customtkinter.CTkComboBox(self.sale_estimate_transiction_frame, width=110, height=30,
                                                         values=["Select", "Invoice", "Date", "Payment Type",
                                                                 "Cheque No.", "Name"])
        self.sale_estimate_pur_search.place(x=1120, y=60)

        self.sale_estimate_pur_serch_entery = customtkinter.CTkEntry(self.sale_estimate_transiction_frame, width=300, height=30,
                                                            textvariable=self.Var_sale_estimate_searchtxt)
        self.sale_estimate_pur_serch_entery.place(x=1240, y=60)

        self.sale_estimate_pur_serch_button = customtkinter.CTkButton(self.sale_estimate_transiction_frame, width=70, height=30,
                                                             text="Search", command=self.salesestimatetranssearch)
        self.sale_estimate_pur_serch_button.place(x=1550, y=60)

        self.sale_estimate_pur_clear_button = customtkinter.CTkButton(self.sale_estimate_transiction_frame, width=70, height=30,
                                                             text="Clear", command=self.saleestimatetransclear)
        self.sale_estimate_pur_clear_button.place(x=1630, y=60)
        self.calgetsaleestimatetotalamount()
        self.saleestimatetrans()

        # todo:sale payment
        self.in_sale_payment_top_frame = customtkinter.CTkFrame(self.sale_payment_frame, width=1720, height=100)
        self.in_sale_payment_top_frame.place(x=10, y=10)

        self.salepayment_add_sale_button = customtkinter.CTkButton(self.in_sale_payment_top_frame,
                                                                    font=customtkinter.CTkFont(size=18),
                                                                    command=self.addsale_event,
                                                                    text="Add Sale", width=70, height=30,
                                                                    image=self.bill_image, text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    fg_color="transparent")
        self.salepayment_add_sale_button.place(x=1310, y=20)

        self.sale_add_payment_button = customtkinter.CTkButton(self.in_sale_payment_top_frame,
                                                                command=self.addpurchase_event,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add Purchess", width=70, height=30,
                                                                image=self.buy_image, text_color="black",
                                                                hover_color=("gray70", "gray30"),
                                                                fg_color="transparent")
        self.sale_add_payment_button.place(x=1440, y=20)

        self.sale_setting_payment_button = customtkinter.CTkButton(self.in_sale_payment_top_frame, width=30,
                                                                    height=30,
                                                                    text="",
                                                                    text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    image=self.setting_image, fg_color="transparent")
        self.sale_setting_payment_button.place(x=1660, y=20)

        self.sale_calculator_payment_button = customtkinter.CTkButton(self.in_sale_payment_top_frame, width=30,
                                                                       height=30,
                                                                       text="",
                                                                       text_color="black",
                                                                       hover_color=("gray70", "gray30"),
                                                                       image=self.calculator_image,
                                                                       fg_color="transparent",
                                                                       command=self.opencalcu)
        self.sale_calculator_payment_button.place(x=1610, y=20)

        self.submenu_sale_payment_lable = customtkinter.CTkFrame(self.in_sale_payment_top_frame, width=1720,
                                                                  height=40,
                                                                  fg_color="transparent")
        self.submenu_sale_payment_lable.place(x=0, y=60)

        self.sale_invoice_button = customtkinter.CTkButton(self.submenu_sale_payment_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_button_event,
                                                           text="Sale Invoice", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_invoice_button.place(x=10, y=0)

        self.sale_estimate_button = customtkinter.CTkButton(self.submenu_sale_payment_lable,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.sale_estimate_event,
                                                            text="Sale Estimate", width=70, height=20,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_estimate_button.place(x=180, y=0)

        self.sale_payment_button = customtkinter.CTkButton(self.submenu_sale_payment_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_payment_event,
                                                           text="Payment In", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_payment_button.place(x=360, y=0)

        self.sale_order_button = customtkinter.CTkButton(self.submenu_sale_payment_lable,
                                                         font=customtkinter.CTkFont(size=18),
                                                         command=self.sale_order_event,
                                                         text="Sale Order", width=70, height=20,
                                                         image=self.bill_image, text_color="black",
                                                         hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_order_button.place(x=520, y=0)

        self.sale_chalan_button = customtkinter.CTkButton(self.submenu_sale_payment_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_delivery_event,
                                                          text="Delivery Challan", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_chalan_button.place(x=680, y=0)

        self.sale_return_button = customtkinter.CTkButton(self.submenu_sale_payment_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_return_event,
                                                          text="Sale Return", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_return_button.place(x=880, y=0)

        self.sale_payment_transiction_frame = customtkinter.CTkFrame(self.sale_payment_frame, width=1720, height=700)
        self.sale_payment_transiction_frame.place(x=10, y=280)

        transiction_payment_Frame = ttk.Frame(self.sale_payment_transiction_frame, relief=RIDGE)
        transiction_payment_Frame.place(x=20, y=100, width=1680, height=580)

        scrolly = ttk.Scrollbar(transiction_payment_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(transiction_payment_Frame, orient=HORIZONTAL)

        self.sale_paymenttransictionTable = ttk.Treeview(transiction_payment_Frame,
                                                          columns=(
                                                              "date", "invonumber", "name", "type", "total", "balance",
                                                              "cheqno"),
                                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.sale_paymenttransictionTable.xview)
        scrolly.config(command=self.sale_paymenttransictionTable.yview)

        self.sale_paymenttransictionTable.heading("date", text="Date")
        self.sale_paymenttransictionTable.heading("invonumber", text="Invoice Number")
        self.sale_paymenttransictionTable.heading("name", text="Party Name")
        self.sale_paymenttransictionTable.heading("type", text="Payment Type")
        self.sale_paymenttransictionTable.heading("total", text="Total Amount")
        self.sale_paymenttransictionTable.heading("balance", text="Received Amount")
        self.sale_paymenttransictionTable.heading("cheqno", text="Cheque No.")

        self.sale_paymenttransictionTable["show"] = "headings"

        self.sale_paymenttransictionTable.column("date", width=150, anchor="center")
        self.sale_paymenttransictionTable.column("invonumber", width=150, anchor="center")
        self.sale_paymenttransictionTable.column("name", width=200, anchor="center")
        self.sale_paymenttransictionTable.column("type", width=100, anchor="center")
        self.sale_paymenttransictionTable.column("total", width=200, anchor="center")
        self.sale_paymenttransictionTable.column("balance", width=200, anchor="center")
        self.sale_paymenttransictionTable.column("cheqno", width=150, anchor="center")

        self.sale_paymenttransictionTable.pack(fill=BOTH, expand=1)
        self.sale_paymenttransictionTable.bind("<ButtonRelease-1>", self.salepaymentintrans)

        self.salepaymentintrans()

        self.Var_sale_payment_searchtxt = StringVar()

        self.sale_pur_lable = customtkinter.CTkLabel(self.sale_payment_transiction_frame,
                                                     font=customtkinter.CTkFont(size=25),
                                                     text="Transition")
        self.sale_pur_lable.place(x=20, y=20)

        self.sale_add_sale_button = customtkinter.CTkButton(self.sale_payment_transiction_frame, width=70, height=30,
                                                            text="Add Sale", command=self.addsale_event)
        self.sale_add_sale_button.place(x=1600, y=10)

        self.sale_payment_search = customtkinter.CTkComboBox(self.sale_payment_transiction_frame, width=110, height=30,
                                                         values=["Select", "Invoice", "Date", "GSTIN",
                                                                 "Phone No.", "Name"])
        self.sale_payment_search.place(x=1120, y=60)

        self.sale_payment_serch_entery = customtkinter.CTkEntry(self.sale_payment_transiction_frame, width=300, height=30,
                                                            textvariable=self.Var_sale_payment_searchtxt)
        self.sale_payment_serch_entery.place(x=1240, y=60)

        self.sale_payment_serch_button = customtkinter.CTkButton(self.sale_payment_transiction_frame, width=70, height=30,
                                                             text="Search", command=self.salepaymentintranssearch)
        self.sale_payment_serch_button.place(x=1550, y=60)

        self.sale_payment_clear_button = customtkinter.CTkButton(self.sale_payment_transiction_frame, width=70, height=30,
                                                             text="Clear", command=self.salepaymentcler)
        self.sale_payment_clear_button.place(x=1630, y=60)

        # todo:sale order
        self.in_sale_order_top_frame = customtkinter.CTkFrame(self.sale_order_frame, width=1720, height=100)
        self.in_sale_order_top_frame.place(x=10, y=10)

        self.saleorder_add_sale_button = customtkinter.CTkButton(self.in_sale_order_top_frame,
                                                                    font=customtkinter.CTkFont(size=18),
                                                                    command=self.addsale_event,
                                                                    text="Add Sale", width=70, height=30,
                                                                    image=self.bill_image, text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    fg_color="transparent")
        self.saleorder_add_sale_button.place(x=1310, y=20)

        self.sale_add_order_button = customtkinter.CTkButton(self.in_sale_order_top_frame,
                                                                command=self.addpurchase_event,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add Purchess", width=70, height=30,
                                                                image=self.buy_image, text_color="black",
                                                                hover_color=("gray70", "gray30"),
                                                                fg_color="transparent")
        self.sale_add_order_button.place(x=1440, y=20)

        self.sale_setting_order_button = customtkinter.CTkButton(self.in_sale_order_top_frame, width=30,
                                                                    height=30,
                                                                    text="",
                                                                    text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    image=self.setting_image, fg_color="transparent")
        self.sale_setting_order_button.place(x=1660, y=20)

        self.sale_calculator_order_button = customtkinter.CTkButton(self.in_sale_order_top_frame, width=30,
                                                                       height=30,
                                                                       text="",
                                                                       text_color="black",
                                                                       hover_color=("gray70", "gray30"),
                                                                       image=self.calculator_image,
                                                                       fg_color="transparent",
                                                                       command=self.opencalcu)
        self.sale_calculator_order_button.place(x=1610, y=20)

        self.submenu_sale_order_lable = customtkinter.CTkFrame(self.in_sale_order_top_frame, width=1720,
                                                                  height=40,
                                                                  fg_color="transparent")
        self.submenu_sale_order_lable.place(x=0, y=60)

        self.sale_invoice_button = customtkinter.CTkButton(self.submenu_sale_order_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_button_event,
                                                           text="Sale Invoice", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_invoice_button.place(x=10, y=0)

        self.sale_estimate_button = customtkinter.CTkButton(self.submenu_sale_order_lable,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.sale_estimate_event,
                                                            text="Sale Estimate", width=70, height=20,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_estimate_button.place(x=180, y=0)

        self.sale_payment_button = customtkinter.CTkButton(self.submenu_sale_order_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_payment_event,
                                                           text="Payment In", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_payment_button.place(x=360, y=0)

        self.sale_order_button = customtkinter.CTkButton(self.submenu_sale_order_lable,
                                                         font=customtkinter.CTkFont(size=18),
                                                         command=self.sale_order_event,
                                                         text="Sale Order", width=70, height=20,
                                                         image=self.bill_image, text_color="black",
                                                         hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_order_button.place(x=520, y=0)

        self.sale_chalan_button = customtkinter.CTkButton(self.submenu_sale_order_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_delivery_event,
                                                          text="Delivery Challan", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_chalan_button.place(x=680, y=0)

        self.sale_return_button = customtkinter.CTkButton(self.submenu_sale_order_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_return_event,
                                                          text="Sale Return", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_return_button.place(x=880, y=0)

        self.sale_order_transiction_frame = customtkinter.CTkFrame(self.sale_order_frame, width=1720, height=700)
        self.sale_order_transiction_frame.place(x=10, y=280)

        transiction_order_Frame = ttk.Frame(self.sale_order_transiction_frame, relief=RIDGE)
        transiction_order_Frame.place(x=20, y=100, width=1680, height=580)

        scrolly = ttk.Scrollbar(transiction_order_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(transiction_order_Frame, orient=HORIZONTAL)

        self.sale_ordertransictionTable = ttk.Treeview(transiction_order_Frame,
                                                         columns=(
                                                             "date", "invonumber", "name", "type", "total", "balance",
                                                             "cheqno"),
                                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.sale_ordertransictionTable.xview)
        scrolly.config(command=self.sale_ordertransictionTable.yview)

        self.sale_ordertransictionTable.heading("date", text="Date")
        self.sale_ordertransictionTable.heading("invonumber", text="Invoice Number")
        self.sale_ordertransictionTable.heading("name", text="Party Name")
        self.sale_ordertransictionTable.heading("type", text="Payment Type")
        self.sale_ordertransictionTable.heading("total", text="Total Amount")
        self.sale_ordertransictionTable.heading("balance", text="Received Amount")
        self.sale_ordertransictionTable.heading("cheqno", text="Cheque No.")

        self.sale_ordertransictionTable["show"] = "headings"

        self.sale_ordertransictionTable.column("date", width=150, anchor="center")
        self.sale_ordertransictionTable.column("invonumber", width=150, anchor="center")
        self.sale_ordertransictionTable.column("name", width=200, anchor="center")
        self.sale_ordertransictionTable.column("type", width=100, anchor="center")
        self.sale_ordertransictionTable.column("total", width=200, anchor="center")
        self.sale_ordertransictionTable.column("balance", width=200, anchor="center")
        self.sale_ordertransictionTable.column("cheqno", width=150, anchor="center")

        self.sale_ordertransictionTable.pack(fill=BOTH, expand=1)
        self.sale_ordertransictionTable.bind("<ButtonRelease-1>",)



        self.Var_sale_searchtxt = StringVar()

        self.sale_pur_lable = customtkinter.CTkLabel(self.sale_order_transiction_frame,
                                                     font=customtkinter.CTkFont(size=25),
                                                     text="Transition")
        self.sale_pur_lable.place(x=20, y=20)

        self.sale_add_sale_button = customtkinter.CTkButton(self.sale_order_transiction_frame, width=70, height=30,
                                                            text="Add Sale", command=self.addsale_event)
        self.sale_add_sale_button.place(x=1600, y=10)

        self.sale_pur_search = customtkinter.CTkComboBox(self.sale_order_transiction_frame, width=110, height=30,
                                                         values=["Select", "Invoice", "Date", "Payment Type",
                                                                 "Cheque No.", "Name"])
        self.sale_pur_search.place(x=1120, y=60)

        self.sale_pur_serch_entery = customtkinter.CTkEntry(self.sale_order_transiction_frame, width=300, height=30,
                                                            textvariable=self.Var_sale_searchtxt)
        self.sale_pur_serch_entery.place(x=1240, y=60)

        self.sale_pur_serch_button = customtkinter.CTkButton(self.sale_order_transiction_frame, width=70, height=30,
                                                             text="Search", command=self.salestranssearch)
        self.sale_pur_serch_button.place(x=1550, y=60)

        self.sale_pur_clear_button = customtkinter.CTkButton(self.sale_order_transiction_frame, width=70, height=30,
                                                             text="Clear", command=self.saletransclear)
        self.sale_pur_clear_button.place(x=1630, y=60)

        # todo:sale Delivery
        self.in_sale_Delivery_top_frame = customtkinter.CTkFrame(self.sale_Delivery_frame, width=1720, height=100)
        self.in_sale_Delivery_top_frame.place(x=10, y=10)

        self.saleDelivery_add_sale_button = customtkinter.CTkButton(self.in_sale_Delivery_top_frame,
                                                                    font=customtkinter.CTkFont(size=18),
                                                                    command=self.addsale_event,
                                                                    text="Add Sale", width=70, height=30,
                                                                    image=self.bill_image, text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    fg_color="transparent")
        self.saleDelivery_add_sale_button.place(x=1310, y=20)

        self.sale_add_Delivery_button = customtkinter.CTkButton(self.in_sale_Delivery_top_frame,
                                                                command=self.addpurchase_event,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add Purchess", width=70, height=30,
                                                                image=self.buy_image, text_color="black",
                                                                hover_color=("gray70", "gray30"),
                                                                fg_color="transparent")
        self.sale_add_Delivery_button.place(x=1440, y=20)

        self.sale_setting_Delivery_button = customtkinter.CTkButton(self.in_sale_Delivery_top_frame, width=30,
                                                                    height=30,
                                                                    text="",
                                                                    text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    image=self.setting_image, fg_color="transparent")
        self.sale_setting_Delivery_button.place(x=1660, y=20)

        self.sale_calculator_Delivery_button = customtkinter.CTkButton(self.in_sale_Delivery_top_frame, width=30,
                                                                       height=30,
                                                                       text="",
                                                                       text_color="black",
                                                                       hover_color=("gray70", "gray30"),
                                                                       image=self.calculator_image,
                                                                       fg_color="transparent",
                                                                       command=self.opencalcu)
        self.sale_calculator_Delivery_button.place(x=1610, y=20)

        self.submenu_sale_Delivery_lable = customtkinter.CTkFrame(self.in_sale_Delivery_top_frame, width=1720,
                                                                  height=40,
                                                                  fg_color="transparent")
        self.submenu_sale_Delivery_lable.place(x=0, y=60)

        self.sale_invoice_button = customtkinter.CTkButton(self.submenu_sale_Delivery_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_button_event,
                                                           text="Sale Invoice", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_invoice_button.place(x=10, y=0)

        self.sale_estimate_button = customtkinter.CTkButton(self.submenu_sale_Delivery_lable,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.sale_estimate_event,
                                                            text="Sale Estimate", width=70, height=20,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_estimate_button.place(x=180, y=0)

        self.sale_payment_button = customtkinter.CTkButton(self.submenu_sale_Delivery_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_payment_event,
                                                           text="Payment In", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_payment_button.place(x=360, y=0)

        self.sale_order_button = customtkinter.CTkButton(self.submenu_sale_Delivery_lable,
                                                         font=customtkinter.CTkFont(size=18),
                                                         command=self.sale_order_event,
                                                         text="Sale Order", width=70, height=20,
                                                         image=self.bill_image, text_color="black",
                                                         hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_order_button.place(x=520, y=0)

        self.sale_chalan_button = customtkinter.CTkButton(self.submenu_sale_Delivery_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_delivery_event,
                                                          text="Delivery Challan", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_chalan_button.place(x=680, y=0)

        self.sale_return_button = customtkinter.CTkButton(self.submenu_sale_Delivery_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_return_event,
                                                          text="Sale Return", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_return_button.place(x=880, y=0)

        # todo:sale return
        self.in_sale_return_top_frame = customtkinter.CTkFrame(self.sale_return_frame, width=1720, height=100)
        self.in_sale_return_top_frame.place(x=10, y=10)

        self.salereturn_add_sale_button = customtkinter.CTkButton(self.in_sale_return_top_frame,
                                                                    font=customtkinter.CTkFont(size=18),
                                                                    command=self.addsale_event,
                                                                    text="Add Sale", width=70, height=30,
                                                                    image=self.bill_image, text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    fg_color="transparent")
        self.salereturn_add_sale_button.place(x=1310, y=20)

        self.sale_add_return_button = customtkinter.CTkButton(self.in_sale_return_top_frame,
                                                                command=self.addpurchase_event,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add Purchess", width=70, height=30,
                                                                image=self.buy_image, text_color="black",
                                                                hover_color=("gray70", "gray30"),
                                                                fg_color="transparent")
        self.sale_add_return_button.place(x=1440, y=20)

        self.sale_setting_return_button = customtkinter.CTkButton(self.in_sale_return_top_frame, width=30,
                                                                    height=30,
                                                                    text="",
                                                                    text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    image=self.setting_image, fg_color="transparent")
        self.sale_setting_return_button.place(x=1660, y=20)

        self.sale_calculator_return_button = customtkinter.CTkButton(self.in_sale_return_top_frame, width=30,
                                                                       height=30,
                                                                       text="",
                                                                       text_color="black",
                                                                       hover_color=("gray70", "gray30"),
                                                                       image=self.calculator_image,
                                                                       fg_color="transparent",
                                                                       command=self.opencalcu)
        self.sale_calculator_return_button.place(x=1610, y=20)

        self.submenu_sale_return_lable = customtkinter.CTkFrame(self.in_sale_return_top_frame, width=1720,
                                                                  height=40,
                                                                  fg_color="transparent")
        self.submenu_sale_return_lable.place(x=0, y=60)

        self.sale_invoice_button = customtkinter.CTkButton(self.submenu_sale_return_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_button_event,
                                                           text="Sale Invoice", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_invoice_button.place(x=10, y=0)

        self.sale_estimate_button = customtkinter.CTkButton(self.submenu_sale_return_lable,
                                                            font=customtkinter.CTkFont(size=18),
                                                            command=self.sale_estimate_event,
                                                            text="Sale Estimate", width=70, height=20,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_estimate_button.place(x=180, y=0)

        self.sale_payment_button = customtkinter.CTkButton(self.submenu_sale_return_lable,
                                                           font=customtkinter.CTkFont(size=18),
                                                           command=self.sale_payment_event,
                                                           text="Payment In", width=70, height=20,
                                                           image=self.bill_image, text_color="black",
                                                           hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_payment_button.place(x=360, y=0)

        self.sale_order_button = customtkinter.CTkButton(self.submenu_sale_return_lable,
                                                         font=customtkinter.CTkFont(size=18),
                                                         command=self.sale_order_event,
                                                         text="Sale Order", width=70, height=20,
                                                         image=self.bill_image, text_color="black",
                                                         hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_order_button.place(x=520, y=0)

        self.sale_chalan_button = customtkinter.CTkButton(self.submenu_sale_return_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_delivery_event,
                                                          text="Delivery Challan", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_chalan_button.place(x=680, y=0)

        self.sale_return_button = customtkinter.CTkButton(self.submenu_sale_return_lable,
                                                          font=customtkinter.CTkFont(size=18),
                                                          command=self.sale_return_event,
                                                          text="Sale Return", width=70, height=20,
                                                          image=self.bill_image, text_color="black",
                                                          hover_color=("gray70", "gray30"), fg_color="transparent")
        self.sale_return_button.place(x=880, y=0)

        # todo: purches frame
        self.purches_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.Vark_pur_searchtxt = StringVar()

        self.in_purches_top_frame = customtkinter.CTkFrame(self.purches_frame, width=1720, height=100)
        self.in_purches_top_frame.place(x=10, y=10)

        self.purches_name_frame = customtkinter.CTkFrame(self.purches_frame, width=500, height=860)
        self.purches_name_frame.place(x=10, y=120)

        self.purches_detail_frame = customtkinter.CTkFrame(self.purches_frame, width=1210, height=150)
        self.purches_detail_frame.place(x=520, y=120)

        self.purches_transiction_frame = customtkinter.CTkFrame(self.purches_frame, width=1210, height=700)
        self.purches_transiction_frame.place(x=520, y=280)

        self.purches_search = customtkinter.CTkComboBox(self.purches_name_frame, width=100, height=30,
                                                        values=["Select", "Name", "GSTIN", "Phone No."])
        self.purches_search.place(x=10, y=160)

        self.purches_serch_entery = customtkinter.CTkEntry(self.purches_name_frame, width=200, height=30,
                                                         textvariable=self.Vark_pur_searchtxt)
        self.purches_serch_entery.place(x=120, y=160)

        self.purches_serch_button = customtkinter.CTkButton(self.purches_name_frame, width=70, height=30, text="Search",command=self.purchessearch)
        self.purches_serch_button.place(x=330, y=160)

        self.purches_clear_button = customtkinter.CTkButton(self.purches_name_frame, width=70, height=30, text="Clear",command=self.purclear)
        self.purches_clear_button.place(x=410, y=160)

        self.add_purches_button = customtkinter.CTkButton(self.purches_name_frame,
                                                        font=customtkinter.CTkFont(size=15), text="Add Parches", width=70,
                                                        height=40, image=self.add_image, fg_color="transparent",
                                                        text_color="black",
                                                        hover_color=("gray70", "gray30"))
        self.add_purches_button.place(x=360, y=20)

        self.imp_purches_button = customtkinter.CTkButton(self.purches_name_frame, font=customtkinter.CTkFont(size=18),
                                                        text="Import Parches Data", width=70, height=40,
                                                        image=self.image_icon_image, fg_color="transparent",
                                                        text_color="black",
                                                        hover_color=("gray70", "gray30"))
        self.imp_purches_button.place(x=20, y=20)

        self.purches_add_sale_button = customtkinter.CTkButton(self.in_purches_top_frame,
                                                            font=customtkinter.CTkFont(size=18),command=self.addsale_event,
                                                            text="Add Sale", width=70, height=30,
                                                            image=self.bill_image, text_color="black",
                                                            hover_color=("gray70", "gray30"), fg_color="transparent")
        self.purches_add_sale_button.place(x=1310, y=20)

        self.purches_add_purchess_button = customtkinter.CTkButton(self.in_purches_top_frame,command=self.addpurchase_event,
                                                                font=customtkinter.CTkFont(size=18),
                                                                text="Add Purchess", width=70, height=30,
                                                                image=self.buy_image, text_color="black",
                                                                hover_color=("gray70", "gray30"),
                                                                fg_color="transparent")
        self.purches_add_purchess_button.place(x=1440, y=20)

        self.purches_setting_purches_button = customtkinter.CTkButton(self.in_purches_top_frame, width=30, height=30, text="",
                                                                 text_color="black", hover_color=("gray70", "gray30"),
                                                                 image=self.setting_image, fg_color="transparent")
        self.purches_setting_purches_button.place(x=1660, y=20)

        self.purches_calculator_purches_button = customtkinter.CTkButton(self.in_purches_top_frame, width=30, height=30,
                                                                    text="",
                                                                    text_color="black",
                                                                    hover_color=("gray70", "gray30"),
                                                                    image=self.calculator_image, fg_color="transparent",
                                                                    command=self.opencalcu)
        self.purches_calculator_purches_button.place(x=1610, y=20)

        self.lablename_purches_lable = customtkinter.CTkLabel(self.in_purches_top_frame,
                                                            font=customtkinter.CTkFont(size=18), text="Name",
                                                            width=1720, height=40, fg_color="#F28C28")
        self.lablename_purches_lable.place(x=0, y=60)

        p_Frame = ttk.Frame(self.purches_name_frame, relief=RIDGE)
        p_Frame.place(x=20, y=210, height=630)

        scrolly = ttk.Scrollbar(p_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(p_Frame, orient=HORIZONTAL)

        self.purchesTable = ttk.Treeview(p_Frame, columns=("party", "gstin", "pay", "receive"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.purchesTable.xview)
        scrolly.config(command=self.purchesTable.yview)
        self.purchesTable.heading("party", text="Party")
        self.purchesTable.heading("gstin", text="GSTIN")
        self.purchesTable.heading("pay", text="Pay")
        self.purchesTable.heading("receive", text="Receive")

        self.purchesTable["show"] = "headings"

        self.purchesTable.column("party", width=130, )
        self.purchesTable.column("gstin", width=100)
        self.purchesTable.column("pay", width=100)
        self.purchesTable.column("receive", width=100)

        self.purchesTable.pack(fill=BOTH, expand=1)
        self.purchesTable.bind("<ButtonRelease-1>", self.get_purchase_data)

        self.purshow()

        self.purchesname = StringVar()
        self.purchesnumber = StringVar()
        self.purchesemail = StringVar()
        self.purchescrlimit = StringVar()
        self.purchesaddress = StringVar()
        self.purchesgstin = StringVar()

        self.purches_name_lable = customtkinter.CTkLabel(self.purches_detail_frame, textvariable=self.purchesname,
                                          font=customtkinter.CTkFont(size=18))
        self.purches_name_lable.place(x=15, y=10)

        self.purches_number_lable = customtkinter.CTkLabel(self.purches_detail_frame, textvariable=self.purchesnumber,
                                                         font=customtkinter.CTkFont(size=12))
        self.purches_number_lable.place(x=15, y=60)

        self.purches_email_lable = customtkinter.CTkLabel(self.purches_detail_frame, textvariable=self.purchesemail,
                                                        font=customtkinter.CTkFont(size=12))
        self.purches_email_lable.place(x=15, y=85)

        self.purches_crlimit_lable = customtkinter.CTkLabel(self.purches_detail_frame, textvariable=self.purchescrlimit,
                                                          font=customtkinter.CTkFont(size=12))
        self.purches_crlimit_lable.place(x=15, y=110)

        self.purches_address_lable = customtkinter.CTkLabel(self.purches_detail_frame, textvariable=self.purchesaddress,
                                                          font=customtkinter.CTkFont(size=12))
        self.purches_address_lable.place(x=1000, y=60)

        self.purches_gstin_lable = customtkinter.CTkLabel(self.purches_detail_frame, textvariable=self.purchesgstin,
                                                        font=customtkinter.CTkFont(size=12))
        self.purches_gstin_lable.place(x=1000, y=85)

        self.purches_gstin_lable = customtkinter.CTkLabel(self.purches_transiction_frame, text="TRANSACTION",
                                                        font=customtkinter.CTkFont(size=14, ))
        self.purches_gstin_lable.place(x=10, y=10)

        transiction_Frame = ttk.Frame(self.purches_transiction_frame, relief=RIDGE)
        transiction_Frame.place(x=20, y=100, width=1170, height=580)

        scrolly = ttk.Scrollbar(transiction_Frame, orient=VERTICAL)
        scrollx = ttk.Scrollbar(transiction_Frame, orient=HORIZONTAL)

        self.purchestransictionTable = ttk.Treeview(transiction_Frame,
                                             columns=("number", "date", "type", "total", "balance", "cheqno"),
                                             yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.purchestransictionTable.xview)
        scrolly.config(command=self.purchestransictionTable.yview)

        self.purchestransictionTable.heading("number", text="Invoice Number")
        self.purchestransictionTable.heading("date", text="Date")
        self.purchestransictionTable.heading("type", text="Payment Type")
        self.purchestransictionTable.heading("total", text="Total Amount")
        self.purchestransictionTable.heading("balance", text="Received Amount")
        self.purchestransictionTable.heading("cheqno", text="Cheque No.")

        self.purchestransictionTable["show"] = "headings"

        self.purchestransictionTable.column("number", width=150)
        self.purchestransictionTable.column("date", width=150)
        self.purchestransictionTable.column("type", width=100)
        self.purchestransictionTable.column("total", width=200)
        self.purchestransictionTable.column("balance", width=200)
        self.purchestransictionTable.column("cheqno", width=100)

        self.purchestransictionTable.pack(fill=BOTH, expand=1)
        self.purchestransictionTable.bind("<ButtonRelease-1>", self.purchasedataget)

        self.var_pur_searchby = StringVar()
        self.Var_pur_searchtxt = StringVar()

        self.purches_pur_search = customtkinter.CTkComboBox(self.purches_transiction_frame, width=110, height=30,
                                                              values=["Select", "Invoice", "Date", "Payment Type",
                                                                      "Cheque No."])
        self.purches_pur_search.place(x=590, y=60)

        self.purches_pur_serch_entery = customtkinter.CTkEntry(self.purches_transiction_frame, width=300, height=30,
                                                               textvariable=self.Var_pur_searchtxt)
        self.purches_pur_serch_entery.place(x=710, y=60)

        self.purches_pur_serch_button = customtkinter.CTkButton(self.purches_transiction_frame, width=70, height=30,
                                                                text="Search",command=self.purchestranssearch)
        self.purches_pur_serch_button.place(x=1020, y=60)

        self.purches_pur_clear_button = customtkinter.CTkButton(self.purches_transiction_frame, width=70, height=30,
                                                                text="Clear",
                                                                command=self.purtransclear)
        self.purches_pur_clear_button.place(x=1100, y=60)

        # create third frame
        self.expenses_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.cashhandel_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.reports_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.sync_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.backup_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.utilities_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.setting_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.parties_button.configure(fg_color=("gray75", "gray25") if name == "parties" else "transparent")
        self.Items_button.configure(fg_color=("gray75", "gray25") if name == "items" else "transparent")
        self.gst_sale_button.configure(fg_color=("gray75", "gray25") if name == "gstsale" else "transparent")
        self.sale_button.configure(fg_color=("gray75", "gray25") if name == "sale" or name == "return" or name == "payment" or name == "order" or name == "delivery" or name == "estimate" else "transparent")
        self.Purches_button.configure(fg_color=("gray75", "gray25") if name == "purches" else "transparent")
        self.Expenses_button.configure(fg_color=("gray75", "gray25") if name == "expenses" else "transparent")
        self.Cashhandel_button.configure(fg_color=("gray75", "gray25") if name == "cashhandel" else "transparent")
        self.Reports_button.configure(fg_color=("gray75", "gray25") if name == "reports" else "transparent")
        self.Sync_button.configure(fg_color=("gray75", "gray25") if name == "sync" else "transparent")
        self.Backup_button.configure(fg_color=("gray75", "gray25") if name == "backup" else "transparent")
        self.Utilities_button.configure(fg_color=("gray75", "gray25") if name == "utilities" else "transparent")
        self.Setting_button.configure(fg_color=("gray75", "gray25") if name == "setting" else "transparent")

        # GST Sale Frames
        self.gstsale_return_button.configure(fg_color=("gray75", "gray25") if name == "gstreturn" else "transparent")
        self.gstsale_payment_button.configure(fg_color=("gray75", "gray25") if name == "gstpayment" else "transparent")
        self.gstsale_order_button.configure(fg_color=("gray75", "gray25") if name == "gstorder" else "transparent")
        self.gstsale_chalan_button.configure(fg_color=("gray75", "gray25") if name == "gstdelivery" else "transparent")
        self.gstsale_estimate_button.configure(fg_color=("gray75", "gray25") if name == "gstestimate" else "transparent")

        # Sale Frames
        self.sale_return_button.configure(fg_color=("gray75", "gray25") if name == "return" else "transparent")
        self.sale_payment_button.configure(fg_color=("gray75", "gray25") if name == "payment" else "transparent")
        self.sale_order_button.configure(fg_color=("gray75", "gray25") if name == "order" else "transparent")
        self.sale_chalan_button.configure(fg_color=("gray75", "gray25") if name == "delivery" else "transparent")
        self.sale_estimate_button.configure(fg_color=("gray75", "gray25") if name == "estimate" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "parties":
            self.parties_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.parties_frame.grid_forget()
        if name == "items":
            self.items_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.items_frame.grid_forget()
        if name == "gstsale":
            self.gstsale_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gstsale_frame.grid_forget()
        if name == "sale" :
            self.sale_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sale_frame.grid_forget()
        if name == "purches":
            self.purches_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.purches_frame.grid_forget()
        if name == "expenses":
            self.expenses_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.expenses_frame.grid_forget()
        if name == "cashhandel":
            self.cashhandel_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.cashhandel_frame.grid_forget()
        if name == "reports":
            self.sync_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sync_frame.grid_forget()
        if name == "sync":
            self.reports_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.reports_frame.grid_forget()
        if name == "backup":
            self.backup_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.backup_frame.grid_forget()
        if name == "utilities":
            self.utilities_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.utilities_frame.grid_forget()
        if name == "setting":
            self.setting_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.setting_frame.grid_forget()

        # GST Sale
        if name == "gstreturn":
            self.gstsale_return_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gstsale_return_frame.grid_forget()
        if name == "gstpayment":
            self.gstsale_payment_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gstsale_payment_frame.grid_forget()
        if name == "gstorder":
            self.gstsale_order_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gstsale_order_frame.grid_forget()
        if name == "gstdelivery":
            self.gstsale_Delivery_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gstsale_Delivery_frame.grid_forget()
        if name == "gstestimate":
            self.gstsale_estimate_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gstsale_estimate_frame.grid_forget()

        # Sale
        if name == "return":
            self.sale_return_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sale_return_frame.grid_forget()
        if name == "payment":
            self.sale_payment_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sale_payment_frame.grid_forget()
        if name == "order":
            self.sale_order_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sale_order_frame.grid_forget()
        if name == "delivery":
            self.sale_Delivery_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sale_Delivery_frame.grid_forget()
        if name == "estimate":
            self.sale_estimate_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sale_estimate_frame.grid_forget()

    def sale_invoice_button_event(self):
        self.select_frame_by_name("sale_invoice")

    # home
    def home_button_event(self):
        self.select_frame_by_name("home")
        self.totalrecive()
        self.totalpay()
        self.getdate()
        self.calstockvalue()
        self.getlowitem()
    # Party
    def parties_button_event(self):
        self.select_frame_by_name("parties")

    # item
    def Items_button_event(self):
        self.select_frame_by_name("items")

    # GST Sale
    def gst_sale_button_event(self):
        self.select_frame_by_name("gstsale")
        self.gstcalgetsaletotalamount()
        self.gstsaletrans()

    def gstsale_return_event(self):
        self.select_frame_by_name("gstreturn")

    def gstsale_payment_event(self):
        self.select_frame_by_name("gstpayment")

    def gstsale_order_event(self):
        self.select_frame_by_name("gstorder")

    def gstsale_delivery_event(self):
        self.select_frame_by_name("gstdelivery")

    def gstsale_estimate_event(self):
        self.select_frame_by_name("gstestimate")
        self.calgetsaleestimatetotalamount()
        self.saleestimatetrans()

    # Sale
    def sale_button_event(self):
        self.select_frame_by_name("sale")
        self.calgetsaletotalamount()
        self.saletrans()
    def sale_return_event(self):
        self.select_frame_by_name("return")
    def sale_payment_event(self):
        self.select_frame_by_name("payment")
    def sale_order_event(self):
        self.select_frame_by_name("order")
    def sale_delivery_event(self):
        self.select_frame_by_name("delivery")
    def sale_estimate_event(self):
        self.select_frame_by_name("estimate")
        self.calgetsaleestimatetotalamount()
        self.saleestimatetrans()

    # Purchase
    def Purches_button_event(self):
        self.select_frame_by_name("purches")

    # Expenses
    def Expenses_button_event(self):
        self.select_frame_by_name("expenses")

    # Cash Handel
    def Cashhandel_button_event(self):
        self.select_frame_by_name("cashhandel")

    # Reports
    def Reports_button_event(self):
        self.select_frame_by_name("reports")

    # Sync
    def Sync_button_event(self):
        self.select_frame_by_name("sync")

    # Backup
    def Backup_button_event(self):
        self.select_frame_by_name("backup")

    # Utilities
    def Utilities_button_event(self):
        self.select_frame_by_name("utilities")

    # Setting
    def Setting_button_event(self):
        self.select_frame_by_name("setting")



    # External py open
    def opencalcu(self):
        op("Calculator")

    # gst
    def addgstsale_event(self):
        call(["python", "AddSale.py"])
    def editgstsale_event(self):
        call(["python", "EditGSTSale.py"])


    # sale
    def addsale_event(self):
        call(["python", "sale.py"])
    def editsale_event(self):
        call(["python", "EditSale.py"])
    def addestimate_event(self):
        call(["python", "Estimate.py"])


    # Party
    def addparty_event(self):
        call(["python", "AddParty.py"])
    def editparty_event(self):
        call(["python", "EditParty.py"])

    # item
    def edititem_event(self):
        call(["python", "EditItem.py"])
    def additem_event(self):
        call(["python", "AddItem.py"])

    # Purchase
    def addpurchase_event(self):
        call(["python", "Purchase.py"])
    def editparty_event(self):
        call(["python", "EditParty.py"])



    def change_appearance_mode_event(self,event):
        p = 1
        scale=self.scaling_optionemenu.get()
        theme = self.appearance_mode_menu.get()
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select no from invosalenon where no=?", (p,))
            row = cur.fetchone()
            cur.execute("Update appearance set theme=? where no=?", (
                theme,
                p,
            ))
            con.commit()
            cur.execute("Select no from invosalenon where no=?", (p,))
            row = cur.fetchone()
            cur.execute("Update appearance set scelling=? where no=?", (
                scale,
                p,
            ))
            con.commit()
            self.get_appearance_mode_event()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_appearance_mode_event(self):
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        self.apmodelist.clear()
        self.scalelis.clear()
        try:
            cur.execute("select theme from appearance where no=1")
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                  customtkinter.set_appearance_mode(r)
                  self.apmodelist.insert(0,r)
                  self.appearance_mode_menu.set(r)
                  for i in self.appearancelis2:
                      self.apmodelist.append(i)
                  self.appearance_mode_menu.configure(values=self.apmodelist)
            cur.execute("select scelling from appearance where no=1")
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                    new_scaling_float = int(r.replace("%", "")) / 100
                    customtkinter.set_widget_scaling(new_scaling_float)
                    self.scalelis.insert(0, r)
                    self.scaling_optionemenu.set(r)
                    for i in self.scalelis2:
                        self.scalelis.append(i)
                    self.scaling_optionemenu.configure(values=self.scalelis)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    # def change_scaling_event(self, new_scaling: str):
    #     new_scaling_float = int(new_scaling.replace("%", "")) / 100
    #     customtkinter.set_widget_scaling(new_scaling_float)

    # home frame methods
    def calstockvalue(self):
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        self.itemtotalamlist.clear()
        try:
            cur.execute(f"select saleprice,openqty from itemdata ",)
            rows = cur.fetchall()
            for row in rows:
                a=int(row[0])
                b =int(row[1])
                c=a*b
                self.itemtotalamlist.append(c)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
        result="₹ "+str(sum(self.itemtotalamlist))
        self.stock_amount_lable.configure(text=result,text_color="green")

    def totalrecive(self):
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select recivebalence from partydata ",)
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                    self.recivetotalamlist.append(r)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def totalpay(self):
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select paybalence from partydata ",)
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                    self.paytotalamlist.append(r)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def caluclattotalsale(self,list1,list2,variable):
        for r in list1:
          if r == "":
             pass
          else:
            a= float(r)
            list2.append(a)
        result=sum(list2)
        s=str(result)
        rresult="₹ "+s
        variable.configure(text=rresult)
    def totalsael(self,d,m,y,ld,lm,ly):
      con = sqlite3.connect(database=r'DataBase/ims.db')
      cur = con.cursor()
      self.saletotalamlist.clear()
      self.totalsaleam.clear()
      while y <= ly:
        while m <= lm:
            while d <= ld:
              if len(str(d)) == 1:
                date="0"+str(d)
              elif len(str(d)) == 1 and d == 0:
                dm=str(d)
                dd=dm.replace("0","1")
                date="0"+dd
              else:
                date =str(d)
              if len(str(m)) == 1:
                month="/0"+str(m)
              elif len(str(m)) == 1 and m == 0:
                dm=str(m)
                dd=dm.replace("0","1")
                month="/0"+dd
              else:
                month ="/"+str(m)
              date=date+month+"/"+str(y)
              try:
                cur.execute(f"select total from gstsale where invoicedate=?",(date,) )
                rows = cur.fetchall()
                for row in rows:
                  for r in row:
                    self.saletotalamlist.append(r)
              except Exception as ex:
                 messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
              d = d + 1
            m = m + 1
            d =1
        y= y + 1
      self.caluclattotalsale(self.saletotalamlist,self.totalsaleam,self.sale_amount_lable)

    def totalpurc(self,d,m,y,ld,lm,ly):
      con = sqlite3.connect(database=r'DataBase/ims.db')
      cur = con.cursor()
      self.purtotalamlist.clear()
      self.pursaleam.clear()
      while y <= ly:
        while m <= lm:

            while d <= ld:
              if len(str(d)) == 1:
                date="0"+str(d)
              elif len(str(d)) == 1 and d == 0:
                dm=str(d)
                dd=dm.replace("0","1")
                date="0"+dd
              else:
                date =str(d)
              if len(str(m)) == 1:
                month="/0"+str(m)
              elif len(str(m)) == 1 and m == 0:
                dm=str(m)
                dd=dm.replace("0","1")
                month="/0"+dd
              else:
                month ="/"+str(m)
              date=date+month+"/"+str(y)
              try:
                cur.execute(f"select total from gstpurchase where invoicedate=?",(date,) )
                rows = cur.fetchall()
                for row in rows:
                  for r in row:
                    self.purtotalamlist.append(r)

              except Exception as ex:
                 messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
              d = d + 1
            m = m + 1
            d =1
        y= y + 1
      self.caluclattotalsale(self.purtotalamlist,self.pursaleam,self.purchesam_lable2)
    def gd(self,event):
        self.getdate()
    def getdate(self):
        TodayDate= Dates.today()
        currentdate = TodayDate.strftime("%d")
        currentmonth=TodayDate.strftime("%m")
        currentYear = TodayDate.strftime("%Y")
        lastdate=self.sale_optionemenu.get()
        if lastdate == "This Month" :
            d=1
            m=int(currentmonth)
            y=int(currentYear)
            ld=31
            lm=int(currentmonth)
            ly = int(currentYear)
            datess=f"{d}/{m}/{y}  To  {ld}/{lm}/{ly}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)
        elif lastdate == "Today" :
            d=int(currentdate)
            m=int(currentmonth)
            y=int(currentYear)
            ld=int(currentdate)
            lm=int(currentmonth)
            ly=int(currentYear)
            datess = f"{d}/{m}/{y}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)
        elif lastdate == "Yesterday" :
            d=int(currentdate)-1
            m=int(currentmonth)
            y=int(currentYear)
            ld=int(currentdate)-1
            lm=int(currentmonth)
            ly=int(currentYear)
            datess = f"{d}/{m}/{y}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)
        elif lastdate == "This Weak" :
            m = int(currentmonth)
            y = int(currentYear)
            lm = int(currentmonth)
            ly = int(currentYear)
            if int(currentdate) >= 1 and int(currentdate) <= 7:
             d=1
             ld=7
            elif int(currentdate) >= 8 and int(currentdate) <= 14:
             d = 8
             ld = 14
            elif int(currentdate) >= 15 and int(currentdate) <= 21:
             d = 15
             ld = 21
            elif int(currentdate) >= 22 and int(currentdate) <= 31:
             d = 22
             ld = 31

            datess = f"{d}/{m}/{y}  To  {ld}/{lm}/{ly}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)
        elif lastdate == "Last Weak" :
            m = int(currentmonth)
            y = int(currentYear)
            lm = int(currentmonth)
            ly = int(currentYear)
            if int(currentdate) >= 1 and int(currentdate) <= 7:
                d = 22
                ld = 31
            elif int(currentdate) >= 8 and int(currentdate) <= 14:
                d = 1
                ld = 7
            elif int(currentdate) >= 15 and int(currentdate) <= 21:
                d = 8
                ld = 14
            elif int(currentdate) >= 22 and int(currentdate) <= 31:
                d = 15
                ld = 21
            datess = f"{d}/{m}/{y}  To  {ld}/{lm}/{ly}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)
        elif lastdate == "Last Month" :
            d=1
            if int(currentmonth) == 1:
                m=12
            else:
                m=int(currentmonth)-1
            y=int(currentYear)
            ld=31
            lm=int(currentmonth)-1
            ly=int(currentYear)
            datess = f"{d}/{m}/{y}  To  {ld}/{lm}/{ly}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)
        elif lastdate == "This Quarter" :
            d=1
            ld = 31
            y = int(currentYear)
            ly = int(currentYear)
            if int(currentmonth) == 1 or int(currentmonth) == 2 or int(currentmonth) == 3 or int(currentmonth) == 4 :
             m=1
             lm=4
            elif int(currentmonth) == 5 or int(currentmonth) == 6 or int(currentmonth) == 7 or int(currentmonth) == 8 :
             m=5
             lm=8
            elif int(currentmonth) == 9 or int(currentmonth) == 10 or int(currentmonth) == 11 or int(currentmonth) == 12 :
             m=9
             lm=12
            datess = f"{d}/{m}/{y}  To  {ld}/{lm}/{ly}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)
        elif lastdate == "Last Quarter" :
            d = 1
            ld = 31
            y = int(currentYear)
            ly = int(currentYear)
            if int(currentmonth) == 1 or int(currentmonth) == 2 or int(currentmonth) == 3 or int(currentmonth) == 4:
                m = 5
                lm = 8
            elif int(currentmonth) == 5 or int(currentmonth) == 6 or int(currentmonth) == 7 or int(currentmonth) == 8:
                m = 9
                lm = 12
            elif int(currentmonth) == 9 or int(currentmonth) == 10 or int(currentmonth) == 11 or int(currentmonth) == 12:
                m = 1
                lm = 4
            datess = f"{d}/{m}/{y}  To  {ld}/{lm}/{ly}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)
        elif lastdate == "This Year" :
            d=1
            m=1
            y=int(currentYear)
            ld=31
            lm=12
            ly=int(currentYear)
            datess = f"{d}/{m}/{y}  To  {ld}/{lm}/{ly}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)
        elif lastdate == "Last Year" :
            d=1
            m=1
            y=int(currentYear)-1
            ld=31
            lm=12
            ly=int(currentYear)-1
            datess = f"{d}/{m}/{y}  To  {ld}/{lm}/{ly}"
            self.sale_amount_date.configure(text=datess)
            self.totalsael(d,m,y,ld,lm,ly)
            self.totalpurc(d, m, y, ld, lm, ly)

    def getlowitem(self):
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        self.itemtotalamlist.clear()
        try:
            cur.execute(f"select itemname,openqty from itemdata ",)
            rows = cur.fetchall()
            for row in rows:
                if int(row[1]) <= 5:
                 a=row[0]
                 b =int(row[1])
                 c=f"Item Name :    {a}       qty  :  {b}"
                 self.itemlowlist.append(c)
                else:
                 pass
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
        if len(self.itemlowlist) < 1 :
            self.lowStock_lable2.insert(0.0,"No Item")
            self.lowStock_lable2.configure(state='disabled')
        else:
          for i in self.itemlowlist :
            result=f"\n {i}"
            self.lowStock_lable2.insert(0.0,result)
            self.lowStock_lable2.configure(state='disabled')

    # Party Frame Methods
    def show(self):
      con = sqlite3.connect(database=r'DataBase/ims.db')
      cur = con.cursor()
      try:
        cur.execute("select partyname,gstin,paybalence,recivebalence from partydata")
        rows = cur.fetchall()
        self.productTable.delete(*self.productTable.get_children())
        for row in rows:
            self.productTable.insert('', END, values=row)
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def get_transiction_data(self):

        gst = self.partygstin.get()
        rgst = gst.replace("GSTIN : ", "")
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select invoiceno,invoicedate,paymentype,total,received,refreceno from gstsale where gstin=?",
                        (rgst,))
            rows = cur.fetchall()

            self.transictionTable.delete(*self.transictionTable.get_children())
            for row in rows:
                self.transictionTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def get_data(self, ev):
        partydatalist=[]
        f = self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute(
                "select partyname,phonenumber,emailid,recivebalence,billaddress,gstin from partydata where pid=?",
                (row[1],))
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.partyname.set(row[0])
                self.partynumber.set(f"Phone No. : {row[1]}")
                self.partyemail.set(f"Email : {row[2]}")
                self.partycrlimit.set(f"Receiving Amount : ₹{row[3]}")
                self.partyaddress.set(f"Address : {row[4]}")
                self.partygstin.set(f"GSTIN : {row[5]}")
                self.show()
                self.get_transiction_data()
                self.patyclear()
            cur.execute("select pid,partyname,gstin,phonenumber,gsttype,state,emailid,billaddress,shipaddress,paybalence,recivebalence,date,creditlim,add1,add2,add3,add4 from partydata where partyname=?",
                (row[0],))
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                    partydatalist.append(r)
            cur.execute(
                "Update editpartydata set partyname=?,gstin=?,phonenumber=?,gsttype=?,state=?,emailid=?,billaddress=?,shipaddress=?,paybalence=?,recivebalence=?,date=?,creditlim=?,add1=?,add2=?,add3=?,add4=? where pid=1",
                (
                    partydatalist[1],
                    partydatalist[2],
                    partydatalist[3],
                    partydatalist[4],
                    partydatalist[5],
                    partydatalist[6],
                    partydatalist[7],
                    partydatalist[8],
                    partydatalist[9],
                    partydatalist[10],
                    partydatalist[11],
                    partydatalist[12],
                    partydatalist[13],
                    partydatalist[14],
                    partydatalist[15],
                    partydatalist[16],
                ))
            con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def add_amount(self, ev):
        f = self.transictionTable.focus()
        content = (self.transictionTable.item(f))
        row = content['values']
        invo = row[0]
        try:
            con = sqlite3.connect(database=r'DataBase/ims.db')
            cur = con.cursor()

            cur.execute("Select invoice from edittransction where no=1")
            cur.execute("Update edittransction set invoice=?", (
                invo,
            ))
            con.commit()
        except Exception as ex:
            print(ex)
    def patysearch(self):
        select=self.parties_search.get()
        ssk=select.replace("Name","partyname")
        ssm=ssk.replace("GSTIN","gstin")
        sss = ssm.replace("Phone No.", "phonenumber")
        con=sqlite3.connect(database=r'DataBase/ims.db')
        cur=con.cursor()
        try:
            if self.parties_search.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self)
            elif self.Var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self)
            else :
              cur.execute("select partyname,gstin,paybalence,recivebalence from partydata where "+sss+" LIKE '%"+self.Var_searchtxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                self.productTable.delete(*self.productTable.get_children())
                for row in rows:
                 self.productTable.insert('',END,values=row)
              else:
                  messagebox.showerror("Error","No record found!!!",parent=self)
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self)
    def patyclear(self):
        self.parties_search.set("Select"),
        self.Var_searchtxt.set(""),
        self.show()
    def partytranssearch(self):
        select=self.party_trans_search.get()
        ssk=select.replace("Invoice","invoiceno")
        ssm=ssk.replace("Date","invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        sss = ssmk.replace("Payment Type", "paymentype")
        con=sqlite3.connect(database=r'DataBase/ims.db')
        cur=con.cursor()
        try:
            if self.party_trans_search.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self)
            elif self.Var_trans_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self)
            else :
              cur.execute("select invoiceno,invoicedate,paymentype,total,received,refreceno from gstsale where "+sss+" LIKE '%"+self.Var_trans_searchtxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                self.transictionTable.delete(*self.transictionTable.get_children())
                for row in rows:
                 self.transictionTable.insert('',END,values=row)
              else:
                  messagebox.showerror("Error","No record found!!!",parent=self)
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self)
    def patytransclear(self):
        self.party_trans_search.set("Select"),
        self.Var_trans_searchtxt.set(""),
        self.get_transiction_data()


   # Item Frame methods
    def itemshow(self):
      con = sqlite3.connect(database=r'DataBase/ims.db')
      cur = con.cursor()
      try:
        cur.execute("select itemname,hsn,itemcode,openqty from itemdata")
        rows = cur.fetchall()
        self.itemTable.delete(*self.itemTable.get_children())
        for row in rows:
            self.itemTable.insert('', END, values=row)
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def stoclprice(self,price,qtyy,var):
        stprice=int(price)
        qty=int(qtyy)
        stock=stprice*qty
        var.set(f"Stock Price : ₹{stock}")
    def get_itemtrans_data(self, ev):
        itemdatalist=[]
        itemdatalist.clear()
        f = self.itemTable.focus()
        content = (self.itemTable.item(f))
        row = content['values']
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute(
                f"select itemname,hsn,itemcode,gsttax,saleprice,wholesaleprice,purchesprice,openqty from itemdata where hsn=?",
                (row[1],))
            rows = cur.fetchall()
            self.itemTable.delete(*self.itemTable.get_children())
            for row in rows:
                self.itemname.set(row[0])
                self.itemnumber.set(f"HSN No. : {row[1]}")
                self.itememail.set(f"Item Code. : {row[2]}")
                self.itemcrlimit.set(f"Tax Rate : {row[3]}")
                self.itemaddress.set(f"Sale Price : ₹{row[4]}")
                self.itemgstin.set(f"Wholesale Price : ₹{row[5]}")
                self.itempurchase.set(f"Purchase Price : ₹{row[6]}")
                self.itemstock.set(f"In Stock : {row[7]}")
                self.stoclprice(row[4],row[7],self.itemstockprice)
                self.itemshow()
                self.get_item_data()
                self.itemclear()
            cur.execute("select pid,itemname,hsn,category,itemcode,saleprice,tax1,discount,dicst,wholesaleprice,tax2,minqty,purchesprice,gsttax,openqty,atprice,date,minstockmanten,location,unit from itemdata where hsn=?",
                (row[1],))
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                  itemdatalist.append(r)
            cur.execute("Update edititemdata set itemname=?,hsn=?,category=?,itemcode=?,saleprice=?,tax1=?,discount=?,dicst=?,wholesaleprice=?,tax2=?,minqty=?,purchesprice=?,gsttax=?,openqty=?,atprice=?,date=?,minstockmanten=?,location=?,unit=? where pid=1",(
                    itemdatalist[1],
                    itemdatalist[2],
                    itemdatalist[3],
                    itemdatalist[4],
                    itemdatalist[5],
                    itemdatalist[6],
                    itemdatalist[7],
                    itemdatalist[8],
                    itemdatalist[9],
                    itemdatalist[10],
                    itemdatalist[11],
                    itemdatalist[12],
                    itemdatalist[13],
                    itemdatalist[14],
                    itemdatalist[15],
                    itemdatalist[16],
                    itemdatalist[17],
                    itemdatalist[18],
                    itemdatalist[19],
                ))
            con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def itemsearch(self):
        select=self.item_search.get()
        ssk=select.replace("Name","itemname")
        ssm=ssk.replace("HSN","hsn")
        sss = ssm.replace("Item Code", "itemcode")
        con=sqlite3.connect(database=r'DataBase/ims.db')
        cur=con.cursor()
        try:
            if self.item_search.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self)
            elif self.item_serch_entery.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self)
            else :
              cur.execute("select itemname,hsn,itemcode,openqty from itemdata where "+sss+" LIKE '%"+self.item_serch_entery.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                self.itemTable.delete(*self.itemTable.get_children())
                for row in rows:
                 self.itemTable.insert('',END,values=row)
              else:
                  messagebox.showerror("Error","No record found!!!",parent=self)
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self)
    def itemclear(self):
        self.item_search.set("Select"),
        self.Vark_item_searchtxt.set(""),
        self.itemshow()
    def add_itemamount(self, ev):
        f = self.itemtransictionTable.focus()
        content = (self.itemtransictionTable.item(f))
        row = content['values']
        invo = row[0]
        try:
            con = sqlite3.connect(database=r'DataBase/ims.db')
            cur = con.cursor()

            cur.execute("Select invoice from edittransction where no=1")
            cur.execute("Update edittransction set invoice=?", (
                invo,
            ))
            con.commit()
        except Exception as ex:
            print(ex)

    def itemtranssearch(self):
        select = self.item_pur_search.get()
        ssk = select.replace("Invoice", "invoiceno")
        ssm = ssk.replace("Date", "invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        sss = ssmk.replace("Payment Type", "paymentype")
        select = self.itemname.get()
        lis = ["item1name", "item2name", "item3name", "item4name", "item5name", "item6name", "item7name", "item8name",
               "item9name", "item10name"]
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        for i in lis:
          try:
            if self.item_pur_search.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self)
            elif self.item_pur_serch_entery.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self)
            else:
                cur.execute("select invoiceno,invoicedate,paymentype,total,received,refreceno from gstsale where " + sss + " LIKE '%" + self.item_pur_serch_entery.get() + "%' and "+i+" LIKE '%"+select+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.itemtransictionTable.delete(*self.itemtransictionTable.get_children())
                    for row in rows:
                        self.itemtransictionTable.insert('', END, values=row)
                else:
                    print("Error", "No record found!!!")
          except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def itemctranslear(self):
        self.item_pur_search.set("Select"),
        self.Var_pur_searchtxt.set(""),
        self.get_item_data()
    def get_item_data(self):
        lis = ["item1name", "item2name", "item3name", "item4name", "item5name", "item6name", "item7name", "item8name",
               "item9name", "item10name"]

        select = self.itemname.get()
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        self.itemtransictionTable.delete(*self.itemtransictionTable.get_children())
        for i in lis:
          try:
            cur.execute(f"select invoiceno,invoicedate,paymentype,total,received,refreceno from gstsale where {i}=?",
                        (select,))
            rows = cur.fetchall()

            for row in rows:
                self.itemtransictionTable.insert('', END, values=row)

          except Exception as ex:
            print("Error", f"Error due to : {str(ex)}")
    def itemctranslear(self):
        self.item_pur_search.set("Select"),
        self.Var_pur_searchtxt.set(""),
        self.get_item_data()



    # GST Sale Frame Methods
    def gstgetsaletotalamount(self):
        self.gstsale_paidamount_mlist.clear()
        self.gstsale_totalamount_mlist.clear()
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select received from gstsale ",)
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                  rm=int(r)
                  self.gstsale_paidamount_mlist.append(rm)

            cur.execute("select total from gstsale ", )
            rows = cur.fetchall()
            for rosw in rows:
                for r in rosw:
                  rk=float(r)
                  self.gstsale_totalamount_mlist.append(rk)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def gstcalgetsaletotalamount(self):
        self.gstsale_paidamount_mlist = []
        self.gstsale_unpaidamount_mlist = []
        self.gstsale_totalamount_mlist = []
        self.gstgetsaletotalamount()
        print(self.gstsale_totalamount_mlist)
        for i in self.gstsale_paidamount_list:
           for k in i:
             if k == "":
                 pass
             else:
              a=int(k)
              self.gstsale_paidamount_mlist.append(a)
        for m in self.gstsale_totalamount_list:
            for k in m:
             if k == "":
                 pass
             else:
               b=float(k)
               self.gstsale_totalamount_mlist.append(b)
        sumpaid=sum(self.gstsale_paidamount_mlist)
        sumtotal=sum(self.gstsale_totalamount_mlist)
        recive=sumtotal-sumpaid
        self.gstsale_paidamount=f"₹{sumpaid}"
        self.gstsale_unpaidamount =f"₹{recive}"
        self.gstsale_totalamount=f"₹{sumtotal}"
        self.gstsale_detail_paid_amount_lable.configure(text=self.gstsale_paidamount)
        self.gstsale_detail_unpaid_amount_lable.configure(text=self.gstsale_unpaidamount)
        self.gstsale_detail_total_amount_lable.configure(text=self.gstsale_totalamount)
    def gstsaletrans(self):
            self.involista3.clear()
            con = sqlite3.connect(database=r'DataBase/ims.db')
            cur = con.cursor()
            try:
                cur.execute("select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from gstsale")
                rows = cur.fetchall()
                self.gstsaletransictionTable.delete(*self.gstsaletransictionTable.get_children())
                for row in rows:
                    self.gstsaletransictionTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def gstsaledataget(self,event):
        f = self.gstsaletransictionTable.focus()
        content = (self.gstsaletransictionTable.item(f))
        mow = content['values']
        invoice_zero=6-len(str(mow[1]))
        a = 1
        mm = "0"
        while a < invoice_zero:
            mm = mm + "0"
            a += 1
        final = f"{mm}{mow[1]}"
        strfinal = str(final)
        involista3 = []
        involista3.clear()
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
          cur.execute("select partyname,phonenumber,gstin,invoiceno,cashorcr,invoicedate,steteofsuply,paymentype,refreceno,total,received,balance,item1name,qty1,unit1,unitprice1,dec1,desamount1,amount1,item2name,qty2,unit2,unitprice2,dec2,desamount2,amount2,item3name,qty3,unit3,unitprice3,dec3,desamount3,amount3,item4name,qty4,unit4,unitprice4,dec4,desamount4,amount4,item5name,qty5,unit5,unitprice5,dec5,desamount5,amount5,item6name,qty6,unit6,unitprice6,dec6,desamount6,amount6,item7name,qty7,unit7,unitprice7,dec7,desamount7,amount7,item8name,qty8,unit8,unitprice8,dec8,desamount8,amount8,item9name,qty9,unit9,unitprice9,dec9,desamount9,amount9,item10name,qty10,unit10,unitprice10,dec10,desamount10,amount10 from gstsale where invoiceno=?",
            (strfinal,))
          rows = cur.fetchall()
          for row in rows:
            for r in row:
                involista3.append(r)
          cur.execute("Update editgstsale set partyname=?,phonenumber=?,gstin=?,invoiceno=?,cashorcr=?,invoicedate=?,steteofsuply=?,paymentype=?,refreceno=?,total=?,received=?,balance=?,item1name=?,qty1=?,unit1=?,unitprice1=?,dec1=?,desamount1=?,amount1=?,item2name=?,qty2=?,unit2=?,unitprice2=?,dec2=?,desamount2=?,amount2=?,item3name=?,qty3=?,unit3=?,unitprice3=?,dec3=?,desamount3=?,amount3=?,item4name=?,qty4=?,unit4=?,unitprice4=?,dec4=?,desamount4=?,amount4=?,item5name=?,qty5=?,unit5=?,unitprice5=?,dec5=?,desamount5=?,amount5=?,item6name=?,qty6=?,unit6=?,unitprice6=?,dec6=?,desamount6=?,amount6=?,item7name=?,qty7=?,unit7=?,unitprice7=?,dec7=?,desamount7=?,amount7=?,item8name=?,qty8=?,unit8=?,unitprice8=?,dec8=?,desamount8=?,amount8=?,item9name=?,qty9=?,unit9=?,unitprice9=?,dec9=?,desamount9=?,amount9=?,item10name=?,qty10=?,unit10=?,unitprice10=?,dec10=?,desamount10=?,amount10=? where sid=1",
                (
                    involista3[0],
                    involista3[1],
                    involista3[2],
                    involista3[3],
                    involista3[4],
                    involista3[5],
                    involista3[6],
                    involista3[7],
                    involista3[8],
                    involista3[9],
                    involista3[10],
                    involista3[11],
                    involista3[12],
                    involista3[13],
                    involista3[14],
                    involista3[15],
                    involista3[16],
                    involista3[17],
                    involista3[18],
                    involista3[19],
                    involista3[20],
                    involista3[21],
                    involista3[22],
                    involista3[23],
                    involista3[24],
                    involista3[25],
                    involista3[26],
                    involista3[27],
                    involista3[28],
                    involista3[29],
                    involista3[30],
                    involista3[31],
                    involista3[32],
                    involista3[33],
                    involista3[34],
                    involista3[35],
                    involista3[36],
                    involista3[37],
                    involista3[38],
                    involista3[39],
                    involista3[40],
                    involista3[41],
                    involista3[42],
                    involista3[43],
                    involista3[44],
                    involista3[45],
                    involista3[46],
                    involista3[47],
                    involista3[48],
                    involista3[49],
                    involista3[50],
                    involista3[51],
                    involista3[52],
                    involista3[53],
                    involista3[54],
                    involista3[55],
                    involista3[56],
                    involista3[57],
                    involista3[58],
                    involista3[59],
                    involista3[60],
                    involista3[61],
                    involista3[62],
                    involista3[63],
                    involista3[64],
                    involista3[65],
                    involista3[66],
                    involista3[67],
                    involista3[68],
                    involista3[69],
                    involista3[70],
                    involista3[71],
                    involista3[72],
                    involista3[73],
                    involista3[74],
                    involista3[75],
                    involista3[76],
                    involista3[77],
                    involista3[78],
                    involista3[79],
                    involista3[80],
                    involista3[81],
                ))
          con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def gstsalestranssearch(self):
        select = self.gstsale_pur_search.get()
        ssk = select.replace("Invoice", "invoiceno")
        ssm = ssk.replace("Date", "invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        ssml = ssmk.replace("Name", "partyname")
        sss = ssml.replace("Payment Type", "paymentype")
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            if self.gstsale_pur_search.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self)
            elif self.Var_gstsale_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self)
            else:
                cur.execute(
                    "select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from gstsale where " + sss + " LIKE '%" + self.Var_gstsale_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.gstsaletransictionTable.delete(*self.gstsaletransictionTable.get_children())
                    for row in rows:
                        self.gstsaletransictionTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def gstsaletransclear(self):
        self.gstsale_pur_search.set("Select"),
        self.Var_gstsale_searchtxt.set(""),
        self.gstsaletrans()




    # Sale Frame Methods
    def saletrans(self):
            self.involista1.clear()
            con = sqlite3.connect(database=r'DataBase/ims.db')
            cur = con.cursor()
            try:
                cur.execute("select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from sale")
                rows = cur.fetchall()
                self.saletransictionTable.delete(*self.saletransictionTable.get_children())
                for row in rows:
                    self.saletransictionTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def getsaletotalamount(self):
        self.sale_paidamount_list.clear()
        self.sale_totalamount_list.clear()
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select received from gstsale ",)
            rows = cur.fetchall()
            for row in rows:
                self.sale_paidamount_list.append(row)
            cur.execute("select total from gstsale ", )
            rowms = cur.fetchall()
            for rosw in rowms:
                self.sale_totalamount_list.append(rosw)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def calgetsaletotalamount(self):
        self.sale_paidamount_mlist = []
        self.sale_unpaidamount_mlist = []
        self.sale_totalamount_mlist = []
        self.getsaletotalamount()
        for i in self.sale_paidamount_list:
           for k in i:
             if k == "":
                 pass
             else:
              a=int(k)
              self.sale_paidamount_mlist.append(a)
        for m in self.sale_totalamount_list:
            for k in m:
             if k == "":
                 pass
             else:
               b=float(k)
               self.sale_totalamount_mlist.append(b)
        sumpaid=sum(self.sale_paidamount_mlist)
        sumtotal = sum(self.sale_totalamount_mlist)
        recive=sumtotal-sumpaid
        self.sale_paidamount=f"₹{sumpaid}"
        self.sale_unpaidamount =f"₹{recive}"
        self.sale_totalamount=f"₹{sumtotal}"
        self.sale_detail_paid_amount_lable.configure(text=self.sale_paidamount)
        self.sale_detail_unpaid_amount_lable.configure(text=self.sale_unpaidamount)
        self.sale_detail_total_amount_lable.configure(text=self.sale_totalamount)
    def saletrans(self):
            self.involista1.clear()
            con = sqlite3.connect(database=r'DataBase/ims.db')
            cur = con.cursor()
            try:
                cur.execute("select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from sale")
                rows = cur.fetchall()
                self.saletransictionTable.delete(*self.saletransictionTable.get_children())
                for row in rows:
                    self.saletransictionTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def saledataget(self,event):
        f = self.saletransictionTable.focus()
        content = (self.saletransictionTable.item(f))
        mow = content['values']
        invoice_zero=6-len(str(mow[1]))
        a = 1
        mm = "0"
        while a < invoice_zero:
            mm = mm + "0"
            a += 1
        final = f"{mm}{mow[1]}"
        strfinal = str(final)
        involista2 = []
        involista2.clear()
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
          cur.execute("select partyname,phonenumber,gstin,invoiceno,cashorcr,invoicedate,steteofsuply,paymentype,refreceno,total,received,balance,item1name,qty1,unit1,unitprice1,dec1,desamount1,amount1,item2name,qty2,unit2,unitprice2,dec2,desamount2,amount2,item3name,qty3,unit3,unitprice3,dec3,desamount3,amount3,item4name,qty4,unit4,unitprice4,dec4,desamount4,amount4,item5name,qty5,unit5,unitprice5,dec5,desamount5,amount5,item6name,qty6,unit6,unitprice6,dec6,desamount6,amount6,item7name,qty7,unit7,unitprice7,dec7,desamount7,amount7,item8name,qty8,unit8,unitprice8,dec8,desamount8,amount8,item9name,qty9,unit9,unitprice9,dec9,desamount9,amount9,item10name,qty10,unit10,unitprice10,dec10,desamount10,amount10 from sale where invoiceno=?",
            (strfinal,))
          rows = cur.fetchall()
          for row in rows:
            for r in row:
                involista2.append(r)
          cur.execute("Update editsale set partyname=?,phonenumber=?,gstin=?,invoiceno=?,cashorcr=?,invoicedate=?,steteofsuply=?,paymentype=?,refreceno=?,total=?,received=?,balance=?,item1name=?,qty1=?,unit1=?,unitprice1=?,dec1=?,desamount1=?,amount1=?,item2name=?,qty2=?,unit2=?,unitprice2=?,dec2=?,desamount2=?,amount2=?,item3name=?,qty3=?,unit3=?,unitprice3=?,dec3=?,desamount3=?,amount3=?,item4name=?,qty4=?,unit4=?,unitprice4=?,dec4=?,desamount4=?,amount4=?,item5name=?,qty5=?,unit5=?,unitprice5=?,dec5=?,desamount5=?,amount5=?,item6name=?,qty6=?,unit6=?,unitprice6=?,dec6=?,desamount6=?,amount6=?,item7name=?,qty7=?,unit7=?,unitprice7=?,dec7=?,desamount7=?,amount7=?,item8name=?,qty8=?,unit8=?,unitprice8=?,dec8=?,desamount8=?,amount8=?,item9name=?,qty9=?,unit9=?,unitprice9=?,dec9=?,desamount9=?,amount9=?,item10name=?,qty10=?,unit10=?,unitprice10=?,dec10=?,desamount10=?,amount10=? where sid=1",
                (
                    involista2[0],
                    involista2[1],
                    involista2[2],
                    involista2[3],
                    involista2[4],
                    involista2[5],
                    involista2[6],
                    involista2[7],
                    involista2[8],
                    involista2[9],
                    involista2[10],
                    involista2[11],
                    involista2[12],
                    involista2[13],
                    involista2[14],
                    involista2[15],
                    involista2[16],
                    involista2[17],
                    involista2[18],
                    involista2[19],
                    involista2[20],
                    involista2[21],
                    involista2[22],
                    involista2[23],
                    involista2[24],
                    involista2[25],
                    involista2[26],
                    involista2[27],
                    involista2[28],
                    involista2[29],
                    involista2[30],
                    involista2[31],
                    involista2[32],
                    involista2[33],
                    involista2[34],
                    involista2[35],
                    involista2[36],
                    involista2[37],
                    involista2[38],
                    involista2[39],
                    involista2[40],
                    involista2[41],
                    involista2[42],
                    involista2[43],
                    involista2[44],
                    involista2[45],
                    involista2[46],
                    involista2[47],
                    involista2[48],
                    involista2[49],
                    involista2[50],
                    involista2[51],
                    involista2[52],
                    involista2[53],
                    involista2[54],
                    involista2[55],
                    involista2[56],
                    involista2[57],
                    involista2[58],
                    involista2[59],
                    involista2[60],
                    involista2[61],
                    involista2[62],
                    involista2[63],
                    involista2[64],
                    involista2[65],
                    involista2[66],
                    involista2[67],
                    involista2[68],
                    involista2[69],
                    involista2[70],
                    involista2[71],
                    involista2[72],
                    involista2[73],
                    involista2[74],
                    involista2[75],
                    involista2[76],
                    involista2[77],
                    involista2[78],
                    involista2[79],
                    involista2[80],
                    involista2[81],
                ))
          con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def salestranssearch(self):
        select = self.sale_pur_search.get()
        ssk = select.replace("Invoice", "invoiceno")
        ssm = ssk.replace("Date", "invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        ssml = ssmk.replace("Name", "partyname")
        sss = ssml.replace("Payment Type", "paymentype")
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            if self.sale_pur_search.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self)
            elif self.Var_sale_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self)
            else:
                cur.execute(
                    "select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from gstsale where " + sss + " LIKE '%" + self.Var_sale_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.saletransictionTable.delete(*self.saletransictionTable.get_children())
                    for row in rows:
                        self.saletransictionTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def saletransclear(self):
        self.sale_pur_search.set("Select"),
        self.Var_sale_searchtxt.set(""),
        self.saletrans()


    # sale estimate
    def calgetsaleestimatetotalamount(self):
        self.estimate_sale_paidamount_mlist = []
        self.estimate_sale_unpaidamount_mlist = []
        self.estimate_sale_totalamount_mlist = []
        self.getsaleestimatetotalamount()
        for m in self.estimatee_sale_totalamount_list:
            for k in m:
             if k == "":
                 pass
             else:
               b=float(k)
               self.sale_totalamount_mlist.append(b)
        sumtotal = sum(self.sale_totalamount_mlist)
        self.estimatee_sale_totalamount=f"₹{sumtotal}"
        self.estimatee_sale_detail_total_amount_lable.configure(text=self.estimatee_sale_totalamount)
    def saleestimatetrans(self):
            con = sqlite3.connect(database=r'DataBase/ims.db')
            cur = con.cursor()
            try:
                cur.execute("select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from estimategstsale")
                rows = cur.fetchall()
                self.sale_estimatetransictionTable.delete(*self.sale_estimatetransictionTable.get_children())
                for row in rows:
                    self.sale_estimatetransictionTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def salesestimatetranssearch(self):
        select = self.sale_estimate_pur_search.get()
        ssk = select.replace("Invoice", "invoiceno")
        ssm = ssk.replace("Date", "invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        ssml = ssmk.replace("Name", "partyname")
        sss = ssml.replace("Payment Type", "paymentype")
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            if self.sale_estimate_pur_search.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self)
            elif self.Var_sale_estimate_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self)
            else:
                cur.execute(
                    "select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from estimategstsale where " + sss + " LIKE '%" + self.Var_sale_estimate_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.sale_estimatetransictionTable.delete(*self.sale_estimatetransictionTable.get_children())
                    for row in rows:
                        self.sale_estimatetransictionTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def saleestimatetransclear(self):
        self.sale_estimate_pur_search.set("Select"),
        self.Var_sale_estimate_searchtxt.set(""),
        self.saleestimatetrans()
    def getsaleestimatetotalamount(self):
        self.estimatee_sale_paidamount_list.clear()
        self.estimatee_sale_totalamount_list.clear()
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select total from estimategstsale ", )
            rowms = cur.fetchall()
            for rosw in rowms:
                self.estimatee_sale_totalamount_list.append(rosw)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def calgetsaleestimatetotalamount(self):
        self.estimate_sale_paidamount_mlist = []
        self.estimate_sale_unpaidamount_mlist = []
        self.estimate_sale_totalamount_mlist = []
        self.getsaleestimatetotalamount()
        for m in self.estimatee_sale_totalamount_list:
            for k in m:
             if k == "":
                 pass
             else:
               b=float(k)
               self.sale_totalamount_mlist.append(b)
        sumtotal = sum(self.sale_totalamount_mlist)
        self.estimatee_sale_totalamount=f"₹{sumtotal}"
        self.estimatee_sale_detail_total_amount_lable.configure(text=self.estimatee_sale_totalamount)

    # sale payment
    def salepaymentintrans(self):
            con = sqlite3.connect(database=r'DataBase/ims.db')
            cur = con.cursor()
            try:
                cur.execute("select  partyname,phonenumber,emailid,recivebalence,billaddress,gstin from salepaymentin")
                rows = cur.fetchall()
                self.sale_paymenttransictionTable.delete(*self.sale_paymenttransictionTable.get_children())
                for row in rows:
                    self.sale_paymenttransictionTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def salepaymentintranssearch(self):
        select = self.sale_payment_search.get()
        ssk = select.replace("Name", "partyname")
        ssm = ssk.replace("GSTIN", "gstin")
        ssl = ssm.replace("Invoice", "add2")
        ssjh = ssl.replace("Date.", "date")
        sss = ssjh.replace("Phone No.", "phonenumber")
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            if self.sale_payment_search.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self)
            elif self.Var_sale_payment_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self)
            else:
                cur.execute(
                    "select  partyname,phonenumber,emailid,recivebalence,billaddress,gstin from salepaymentin where " + sss + " LIKE '%" + self.Var_sale_payment_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.sale_paymenttransictionTable.delete(*self.sale_paymenttransictionTable.get_children())
                    for row in rows:
                        self.sale_paymenttransictionTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def salepaymentcler(self):
        self.sale_payment_search.set("Select"),
        self.Var_sale_payment_searchtxt.set(""),
        self.salepaymentintrans()

    # sale order

    # purches frame
    def purshow(self):
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select partyname,gstin,paybalence,recivebalence from partydata")
            rows = cur.fetchall()
            self.purchesTable.delete(*self.purchesTable.get_children())
            for row in rows:
                self.purchesTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def purchessearch(self):
        select=self.purches_search.get()
        ssk=select.replace("Name","partyname")
        ssm=ssk.replace("GSTIN","gstin")
        sss = ssm.replace("Phone No.", "phonenumber")
        con=sqlite3.connect(database=r'DataBase/ims.db')
        cur=con.cursor()
        try:
            if self.purches_search.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self)
            elif self.Vark_pur_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self)
            else :
              cur.execute("select partyname,gstin,paybalence,recivebalence from partydata where "+sss+" LIKE '%"+self.Vark_pur_searchtxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
                self.purchesTable.delete(*self.purchesTable.get_children())
                for row in rows:
                 self.purchesTable.insert('',END,values=row)
              else:
                  messagebox.showerror("Error","No record found!!!",parent=self)
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self)
    def purclear(self):
        self.purches_search.set("Select"),
        self.Vark_pur_searchtxt.set(""),
        self.purshow()
    def get_purchese_data(self):
        gst = self.purchesgstin.get()
        rgst = gst.replace("GSTIN : ", "")
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute("select invoiceno,invoicedate,paymentype,total,received,refreceno from gstpurchase where gstin=?",
                        (rgst,))
            rows = cur.fetchall()
            self.purchestransictionTable.delete(*self.purchestransictionTable.get_children())
            for row in rows:
                self.purchestransictionTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def get_purchase_data(self, ev):
        f = self.purchesTable.focus()
        content = (self.purchesTable.item(f))
        row = content['values']
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            cur.execute(
                "select partyname,phonenumber,emailid,recivebalence,billaddress,gstin from partydata where pid=?",
                (row[1],))
            rows = cur.fetchall()
            self.purchesTable.delete(*self.purchesTable.get_children())
            for row in rows:
                self.purchesname.set(row[0])
                self.purchesnumber.set(f"Phone No. : {row[1]}")
                self.purchesemail.set(f"Email : {row[2]}")
                self.purchescrlimit.set(f"Receiving Amount : ₹{row[3]}")
                self.purchesaddress.set(f"Address : {row[4]}")
                self.purchesgstin.set(f"GSTIN : {row[5]}")
                self.purshow()
                self.get_purchese_data()
                self.purclear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def purchasedataget(self,event):
        f = self.purchestransictionTable.focus()
        content = (self.purchestransictionTable.item(f))
        mow = content['values']
        invoice_zero=6-len(str(mow[0]))
        a = 1
        mm = "0"
        while a < invoice_zero:
            mm = mm + "0"
            a += 1
        final = f"{mm}{mow[0]}"
        strfinal = str(final)
        purlista = []
        purlista.clear()
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
          cur.execute("select partyname,phonenumber,gstin,cashorcr,invoiceno,invoicedate,steteofsuply,paymentype,refreceno,total,received,balance,item1name,qty1,unit1,unitprice1,dec1,desamount1,tax1,gstamount1,amount1,item2name,qty2,unit2,unitprice2,dec2,desamount2,tax2,gstamount2,amount2,item3name,qty3,unit3,unitprice3,dec3,desamount3,tax3,gstamount3,amount3,item4name,qty4,unit4,unitprice4,dec4,desamount4,tax4,gstamount4,amount4,item5name,qty5,unit5,unitprice5,dec5,desamount5,tax5,gstamount5,amount5,item6name,qty6,unit6,unitprice6,dec6,desamount6,tax6,gstamount6,amount6,item7name,qty7,unit7,unitprice7,dec7,desamount7,tax7,gstamount7,amount7,item8name,qty8,unit8,unitprice8,dec8,desamount8,tax8,gstamount8,amount8,item9name,qty9,unit9,unitprice9,dec9,desamount9,tax9,gstamount9,amount9,item10name,qty10,unit10,unitprice10,dec10,desamount10,tax10,gstamount10,amount10 from gstpurchase where invoiceno=?",
            (strfinal,))
          rows = cur.fetchall()
          for row in rows:
            for r in row:
                purlista.append(r)
          cur.execute("Update editgstpurchase set partyname=?,phonenumber=?,gstin=?,cashorcr=?,invoiceno=?,invoicedate=?,steteofsuply=?,paymentype=?,refreceno=?,total=?,received=?,balance=?,item1name=?,qty1=?,unit1=?,unitprice1=?,dec1=?,desamount1=?,tax1=?,gstamount1=?,amount1=?,item2name=?,qty2=?,unit2=?,unitprice2=?,dec2=?,desamount2=?,tax2=?,gstamount2=?,amount2=?,item3name=?,qty3=?,unit3=?,unitprice3=?,dec3=?,desamount3=?,tax3=?,gstamount3=?,amount3=?,item4name=?,qty4=?,unit4=?,unitprice4=?,dec4=?,desamount4=?,tax4=?,gstamount4=?,amount4=?,item5name=?,qty5=?,unit5=?,unitprice5=?,dec5=?,desamount5=?,tax5=?,gstamount5=?,amount5=?,item6name=?,qty6=?,unit6=?,unitprice6=?,dec6=?,desamount6=?,tax6=?,gstamount6=?,amount6=?,item7name=?,qty7=?,unit7=?,unitprice7=?,dec7=?,desamount7=?,tax7=?,gstamount7=?,amount7=?,item8name=?,qty8=?,unit8=?,unitprice8=?,dec8=?,desamount8=?,tax8=?,gstamount8=?,amount8=?,item9name=?,qty9=?,unit9=?,unitprice9=?,dec9=?,desamount9=?,tax9=?,gstamount9=?,amount9=?,item10name=?,qty10=?,unit10=?,unitprice10=?,dec10=?,desamount10=?,tax10=?,gstamount10=?,amount10=? where sid=1",
                (
                    purlista[0],
                    purlista[1],
                    purlista[2],
                    purlista[3],
                    purlista[4],
                    purlista[5],
                    purlista[6],
                    purlista[7],
                    purlista[8],
                    purlista[9],
                    purlista[10],
                    purlista[11],
                    purlista[12],
                    purlista[13],
                    purlista[14],
                    purlista[15],
                    purlista[16],
                    purlista[17],
                    purlista[18],
                    purlista[19],
                    purlista[20],
                    purlista[21],
                    purlista[22],
                    purlista[23],
                    purlista[24],
                    purlista[25],
                    purlista[26],
                    purlista[27],
                    purlista[28],
                    purlista[29],
                    purlista[30],
                    purlista[31],
                    purlista[32],
                    purlista[33],
                    purlista[34],
                    purlista[35],
                    purlista[36],
                    purlista[37],
                    purlista[38],
                    purlista[39],
                    purlista[40],
                    purlista[41],
                    purlista[42],
                    purlista[43],
                    purlista[44],
                    purlista[45],
                    purlista[46],
                    purlista[47],
                    purlista[48],
                    purlista[49],
                    purlista[50],
                    purlista[51],
                    purlista[52],
                    purlista[53],
                    purlista[54],
                    purlista[55],
                    purlista[56],
                    purlista[57],
                    purlista[58],
                    purlista[59],
                    purlista[60],
                    purlista[61],
                    purlista[62],
                    purlista[63],
                    purlista[64],
                    purlista[65],
                    purlista[66],
                    purlista[67],
                    purlista[68],
                    purlista[69],
                    purlista[70],
                    purlista[71],
                    purlista[72],
                    purlista[73],
                    purlista[74],
                    purlista[75],
                    purlista[76],
                    purlista[77],
                    purlista[78],
                    purlista[79],
                    purlista[80],
                    purlista[81],
                    purlista[82],
                    purlista[83],
                    purlista[84],
                    purlista[85],
                    purlista[86],
                    purlista[87],
                    purlista[88],
                    purlista[89],
                    purlista[90],
                    purlista[91],
                    purlista[92],
                    purlista[93],
                    purlista[94],
                    purlista[95],
                    purlista[96],
                    purlista[97],
                    purlista[98],
                    purlista[99],
                    purlista[100],
                    purlista[101],
                ))
          con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def purchestranssearch(self):
        select = self.purches_pur_search.get()
        ssk = select.replace("Invoice", "invoiceno")
        ssm = ssk.replace("Date", "invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        sss = ssmk.replace("Payment Type", "paymentype")
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:
            if self.purches_pur_search.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self)
            elif self.Var_pur_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self)
            else:
                cur.execute(
                    "select invoiceno,invoicedate,paymentype,total,received,refreceno from gstsale where " + sss + " LIKE '%" + self.Var_pur_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.purchestransictionTable.delete(*self.purchestransictionTable.get_children())
                    for row in rows:
                        self.purchestransictionTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)
    def purtransclear(self):
        self.purches_pur_search.set("Select"),
        self.Var_pur_searchtxt.set(""),
        self.get_purchese_data()


    # def calculate_growth_rate(initial_value, final_value):
    #     growth_rate = (final_value - initial_value) / initial_value * 100
    #     return growth_rate

if __name__ == "__main__":
    app = App()
    # app.attributes('-fullscreen',True)
    # app.state('withdrawn')
    app.mainloop()
