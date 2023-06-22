import customtkinter
from customtkinter import *
import os
from PIL import Image
from subprocess import call
import sqlite3
from tkinter import messagebox, END, ttk
from AppOpener import open as op, close

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

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=15, column=0, padx=20, pady=20, sticky="s")

        self.scaling_label = customtkinter.CTkLabel(self.navigation_frame,image=self.scale_image,compound="left", text="   UI Scaling", anchor="w", font=customtkinter.CTkFont(size=15))
        self.scaling_label.grid(row=16, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                               values=["100%","80%", "90%","100%","110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=17, column=0, padx=20, pady=(10, 20))

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

        # todo: main side bar

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

        self.stock_amount_lable = customtkinter.CTkLabel(self.in_home_stock_frame, text=self.stockam,
                                                        font=customtkinter.CTkFont(size=20))
        self.stock_amount_lable.place(x=10, y=50)

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
        self.saleam="₹ 00.00"
        self.saletotalamlist=[]
        self.totalsaleam=[]

        self.sale_amount_lable = customtkinter.CTkLabel(self.in_home_sale_top_frame, text=self.saleam,
                                                        font=customtkinter.CTkFont(size=30, weight="bold"))
        self.sale_amount_lable.place(x=10, y=80)
        self.sale_amount_lable2 = customtkinter.CTkLabel(self.in_home_sale_top_frame, text="Total Sale",
                                                        font=customtkinter.CTkFont(size=15))
        self.sale_amount_lable2.place(x=10, y=120)

        self.salegroth = StringVar()
        self.salegroth = "0%"

        self.sale_growt_lable = customtkinter.CTkLabel(self.in_home_sale_top_frame, text=self.salegroth,
                                                        font=customtkinter.CTkFont(size=30),text_color="green",image=self.uparrow_image,compound="left",anchor="w")
        self.sale_growt_lable.place(x=10, y=180)
        self.sale_growt_lable2 = customtkinter.CTkLabel(self.in_home_sale_top_frame, text="This Month Growth",
                                                         font=customtkinter.CTkFont(size=15))
        self.sale_growt_lable2.place(x=10, y=220)

        self.sale_optionemenu = customtkinter.CTkOptionMenu(self.in_home_sale_top_frame,width=40,
                                                               values=["This Month","Last Month", "This Quarter", "This Year"])
        self.sale_optionemenu.place(x=790,y=10)

        self.totalsael()
        self.caluclattotalsale(self.saletotalamlist,self.totalsaleam,self.sale_amount_lable)

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

        self.party_name_lable = customtkinter.CTkLabel(self.party_detail_frame, textvariable=self.partyname,
                                          font=customtkinter.CTkFont(size=18), text_color="black")
        self.party_name_lable.place(x=15, y=10)

        self.party_number_lable = customtkinter.CTkLabel(self.party_detail_frame, textvariable=self.partynumber,
                                                         font=customtkinter.CTkFont(size=12), text_color="black")
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
        self.itemtransictionTable.bind("<ButtonRelease-1>", self.add_amount)

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

        self.gstsale_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

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
        self.saletransictionTable.bind("<ButtonRelease-1>", self.saletrans)

        self.saletrans()

        self.Var_sale_searchtxt = StringVar()

        self.sale_pur_lable = customtkinter.CTkLabel(self.sale_transiction_frame,font=customtkinter.CTkFont(size=25),text="Transition")
        self.sale_pur_lable.place(x=20, y=20)

        self.sale_add_sale_button = customtkinter.CTkButton(self.sale_transiction_frame, width=70, height=30,
                                                             text="Add Sale", command=self.addsale_event)
        self.sale_add_sale_button.place(x=1600, y=10)

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



        # todo : GST sale frame
        self.gstsale_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")




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

        self.saleestimatetrans()

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
        self.sale_ordertransictionTable.bind("<ButtonRelease-1>", self.saletrans)

        self.saletrans()

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
        self.purchestransictionTable.bind("<ButtonRelease-1>", self.add_amount)

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


    def addparty_event(self):
        call(["python", "comands/AddParty.py"])
    def additem_event(self):
        call(["python", "comands/AddItem.py"])
    def addsale_event(self):
        call(["python", "comands/AddSale.py"])
    def addestimate_event(self):
        call(["python", "comands/Estimate.py"])
    def addpurchase_event(self):
        call(["python", "comands/Purchase.py"])
    def editparty_event(self):
        call(["python", "comands/EditParty.py"])

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.parties_button.configure(fg_color=("gray75", "gray25") if name == "parties" else "transparent")
        self.Items_button.configure(fg_color=("gray75", "gray25") if name == "items" else "transparent")
        self.gst_sale_button.configure(fg_color=("gray75", "gray25") if name == "gstsale" else "transparent")
        self.sale_button.configure(fg_color=("gray75", "gray25") if name == "sale" else "transparent")
        self.Purches_button.configure(fg_color=("gray75", "gray25") if name == "purches" else "transparent")
        self.Expenses_button.configure(fg_color=("gray75", "gray25") if name == "expenses" else "transparent")
        self.Cashhandel_button.configure(fg_color=("gray75", "gray25") if name == "cashhandel" else "transparent")
        self.Reports_button.configure(fg_color=("gray75", "gray25") if name == "reports" else "transparent")
        self.Sync_button.configure(fg_color=("gray75", "gray25") if name == "sync" else "transparent")
        self.Backup_button.configure(fg_color=("gray75", "gray25") if name == "backup" else "transparent")
        self.Utilities_button.configure(fg_color=("gray75", "gray25") if name == "utilities" else "transparent")
        self.Setting_button.configure(fg_color=("gray75", "gray25") if name == "setting" else "transparent")
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
        if name == "sale":
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
    def home_button_event(self):
        self.select_frame_by_name("home")

    def parties_button_event(self):
        self.select_frame_by_name("parties")

    def Items_button_event(self):
        self.select_frame_by_name("items")

    def gst_sale_button_event(self):
        self.select_frame_by_name("gstsale")

    def sale_button_event(self):
        self.select_frame_by_name("sale")

    def Purches_button_event(self):
        self.select_frame_by_name("purches")

    def Expenses_button_event(self):
        self.select_frame_by_name("expenses")

    def Cashhandel_button_event(self):
        self.select_frame_by_name("cashhandel")

    def Reports_button_event(self):
        self.select_frame_by_name("reports")

    def Sync_button_event(self):
        self.select_frame_by_name("sync")

    def Backup_button_event(self):
        self.select_frame_by_name("backup")

    def Utilities_button_event(self):
        self.select_frame_by_name("utilities")

    def Setting_button_event(self):
        self.select_frame_by_name("setting")
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

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        num = 1

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def totalrecive(self):
        con = sqlite3.connect(database=r'ims.db')
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
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select paybalence from partydata ",)
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                    self.paytotalamlist.append(r)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def totalsael(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select total from gstsale ", )
            rows = cur.fetchall()
            for row in rows:
                for r in row:
                    self.saletotalamlist.append(r)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)


    def opencalcu(self):
        op("Calculator")
    def caluclattotalsale(self,list1,list2,variable):
        for r in list1:
            a= float(r)
            list2.append(a)
        result=sum(list2)
        s=str(result)
        rresult="₹ "+s
        variable.configure(text=rresult)

    def get_data(self, ev):
        f = self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']
        con = sqlite3.connect(database=r'ims.db')
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
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_transiction_data(self):

        gst = self.partygstin.get()
        rgst = gst.replace("GSTIN : ", "")
        con = sqlite3.connect(database=r'ims.db')
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

    def patysearch(self):
        select=self.parties_search.get()
        ssk=select.replace("Name","partyname")
        ssm=ssk.replace("GSTIN","gstin")
        sss = ssm.replace("Phone No.", "phonenumber")
        con=sqlite3.connect(database=r'ims.db')
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

    def partytranssearch(self):
        select=self.party_trans_search.get()
        ssk=select.replace("Invoice","invoiceno")
        ssm=ssk.replace("Date","invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        sss = ssmk.replace("Payment Type", "paymentype")
        con=sqlite3.connect(database=r'ims.db')
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

    def add_amount(self, ev):

        f = self.transictionTable.focus()
        content = (self.transictionTable.item(f))
        row = content['values']
        invo = row[0]
        try:
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()

            cur.execute("Select invoice from edittransction where no=1")
            cur.execute("Update edittransction set invoice=?", (
                invo,
            ))
            con.commit()

            self.editparty_event()
        except Exception as ex:
            print(ex)

    def show(self):
      con = sqlite3.connect(database=r'ims.db')
      cur = con.cursor()
      try:
        cur.execute("select partyname,gstin,paybalence,recivebalence from partydata")
        rows = cur.fetchall()
        self.productTable.delete(*self.productTable.get_children())
        for row in rows:
            self.productTable.insert('', END, values=row)

      except Exception as ex:
        messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)


    def patyclear(self):

        self.parties_search.set("Select"),
        self.Var_searchtxt.set(""),
        self.show()

    def patytransclear(self):
        self.party_trans_search.set("Select"),
        self.Var_trans_searchtxt.set(""),
        self.get_transiction_data()




    def itemshow(self):
      con = sqlite3.connect(database=r'ims.db')
      cur = con.cursor()
      try:
        cur.execute("select itemname,hsn,itemcode,openqty from itemdata")
        rows = cur.fetchall()
        self.itemTable.delete(*self.itemTable.get_children())
        for row in rows:
            self.itemTable.insert('', END, values=row)

      except Exception as ex:
        messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def get_itemtrans_data(self, ev):
        f = self.itemTable.focus()
        content = (self.itemTable.item(f))
        row = content['values']
        con = sqlite3.connect(database=r'ims.db')
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
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def stoclprice(self,price,qtyy,var):
        stprice=int(price)
        qty=int(qtyy)
        stock=stprice*qty
        var.set(f"Stock Price : ₹{stock}")

    def itemsearch(self):
        select=self.item_search.get()
        ssk=select.replace("Name","itemname")
        ssm=ssk.replace("HSN","hsn")
        sss = ssm.replace("Item Code", "itemcode")
        con=sqlite3.connect(database=r'ims.db')
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

    def get_item_data(self):
        lis = ["item1name", "item2name", "item3name", "item4name", "item5name", "item6name", "item7name", "item8name",
               "item9name", "item10name"]

        select = self.itemname.get()
        con = sqlite3.connect(database=r'ims.db')
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

    def itemtranssearch(self):
        select = self.item_pur_search.get()
        ssk = select.replace("Invoice", "invoiceno")
        ssm = ssk.replace("Date", "invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        sss = ssmk.replace("Payment Type", "paymentype")
        select = self.itemname.get()
        lis = ["item1name", "item2name", "item3name", "item4name", "item5name", "item6name", "item7name", "item8name",
               "item9name", "item10name"]
        con = sqlite3.connect(database=r'ims.db')
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

    def itemclear(self):
        self.item_search.set("Select"),
        self.Vark_item_searchtxt.set(""),
        self.itemshow()
    def itemctranslear(self):
        self.item_pur_search.set("Select"),
        self.Var_pur_searchtxt.set(""),
        self.get_item_data()



    def purchessearch(self):
        select=self.purches_search.get()
        ssk=select.replace("Name","partyname")
        ssm=ssk.replace("GSTIN","gstin")
        sss = ssm.replace("Phone No.", "phonenumber")
        con=sqlite3.connect(database=r'ims.db')
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

    def purshow(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select partyname,gstin,paybalence,recivebalence from partydata")
            rows = cur.fetchall()
            self.purchesTable.delete(*self.purchesTable.get_children())
            for row in rows:
                self.purchesTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def purclear(self):
        self.purches_search.set("Select"),
        self.Vark_pur_searchtxt.set(""),
        self.purshow()

    def purtransclear(self):
        self.purches_pur_search.set("Select"),
        self.Var_pur_searchtxt.set(""),
        self.get_purchese_data()

    def get_purchase_data(self, ev):
        f = self.purchesTable.focus()
        content = (self.purchesTable.item(f))
        row = content['values']
        con = sqlite3.connect(database=r'ims.db')
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

    def purchestranssearch(self):
        select = self.purches_pur_search.get()
        ssk = select.replace("Invoice", "invoiceno")
        ssm = ssk.replace("Date", "invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        sss = ssmk.replace("Payment Type", "paymentype")
        con = sqlite3.connect(database=r'ims.db')
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

    def get_purchese_data(self):

        gst = self.purchesgstin.get()
        rgst = gst.replace("GSTIN : ", "")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select invoiceno,invoicedate,paymentype,total,received,refreceno from gstsale where gstin=?",
                        (rgst,))
            rows = cur.fetchall()

            self.purchestransictionTable.delete(*self.purchestransictionTable.get_children())
            for row in rows:
                self.purchestransictionTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def getsaletotalamount(self):

        con = sqlite3.connect(database=r'ims.db')
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
            a=int(k)
            self.sale_paidamount_mlist.append(a)
        for m in self.sale_totalamount_list:
            for k in m:
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
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            try:
                cur.execute("select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from gstsale")
                rows = cur.fetchall()
                self.saletransictionTable.delete(*self.saletransictionTable.get_children())
                for row in rows:
                    self.saletransictionTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self)

    def salestranssearch(self):
        select = self.sale_pur_search.get()
        ssk = select.replace("Invoice", "invoiceno")
        ssm = ssk.replace("Date", "invoicedate")
        ssmk = ssm.replace("Cheque No.", "refreceno")
        ssml = ssmk.replace("Name", "partyname")
        sss = ssml.replace("Payment Type", "paymentype")
        con = sqlite3.connect(database=r'ims.db')
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


    def saleestimatetrans(self):
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()
            try:
                cur.execute("select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from estimate")
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
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.sale_estimate_pur_search.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self)
            elif self.Var_sale_estimate_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self)
            else:
                cur.execute(
                    "select invoicedate,invoiceno,partyname,paymentype,total,received,refreceno from estimate where " + sss + " LIKE '%" + self.Var_sale_estimate_searchtxt.get() + "%'")
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


    def salepaymentintrans(self):
            con = sqlite3.connect(database=r'ims.db')
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
        con = sqlite3.connect(database=r'ims.db')
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
        self.saleestimatetrans()



if __name__ == "__main__":
    app = App()
    # app.attributes('-fullscreen',True)
    # app.state('withdrawn')
    app.mainloop()
