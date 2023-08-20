import subprocess
from string import capwords
from docxtpl import DocxTemplate
import sqlite3
from tkinter import ttk, messagebox, StringVar
from num2words import num2words
import datetime
import os
from docx2pdf import convert
doc = DocxTemplate("DataBase/Invoice/saleinvo1.docx")

item_list = []
party_list = []
partydata_list=[]
item_list1 = []
item_list2 = []
item_list3 = []
item_list4 = []
item_list5 = []
item_list6 = []
item_list7 = []
item_list8 = []
item_list9 = []
item_list10 = []
itmlist = []
hsn_no_list=[]
allitem_list=[]

cgsttotal=[]
partyam=[]

def gatpartyam():
    con = sqlite3.connect(database=r'DataBase/ims.db')
    cur = con.cursor()
    try:

        cur.execute("select partyam, partyamtotal from saleinvopartyam where no=1")
        rows = cur.fetchall()
        for row in rows:
            for i in row:
              partyam.append(i)
    except Exception as ex:
        print(ex)


def get_party_data():
        con=sqlite3.connect(database=r'DataBase/ims.db')
        cur=con.cursor()
        try:

            cur.execute("select pid,name,price,qty,status from invosale ")
            rows=cur.fetchall()
            for row in rows:
                item_list.insert(row)


        except Exception as ex:
            print(ex)
            # messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=s)

def get_item_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select partyname,phonenumber,gstin,cashorcr,invoiceno,invoicedate,steteofsuply,paymentype,refreceno,total,received,balance,item1name,qty1,unit1,unitprice1,dec1,desamount1,amount1,item2name,qty2,unit2,unitprice2,dec2,desamount2,amount2,item3name,qty3,unit3,unitprice3,dec3,desamount3,amount3,item4name,qty4,unit4,unitprice4,dec4,desamount4,amount4,item5name,qty5,unit5,unitprice5,dec5,desamount5,amount5,item6name,qty6,unit6,unitprice6,dec6,desamount6,amount6,item7name,qty7,unit7,unitprice7,dec7,desamount7,amount7,item8name,qty8,unit8,unitprice8,dec8,desamount8,amount8,item9name,qty9,unit9,unitprice9,dec9,desamount9,amount9,item10name,qty10,unit10,unitprice10,dec10,desamount10,amount10 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                allitem_list.append(r)


    except Exception as ex:
        print(ex)


def get_partybi_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select partyname,phonenumber,gstin,cashorcr,invoiceno,invoicedate,steteofsuply,paymentype,refreceno,total,received,balance,totaltac,totaldec,totalqty from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                partydata_list.append(r)


    except Exception as ex:
        print(ex)


def get_item1_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item1name,qty1,unit1,unitprice1,dec1,desamount1,amount1 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                item_list1.append(r)


    except Exception as ex:
        print(ex)
def get_item2_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item2name,qty2,unit2,unitprice2,dec2,desamount2,amount2 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                item_list2.append(r)


    except Exception as ex:
        print(ex)

def get_item3_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item3name,qty3,unit3,unitprice3,dec3,desamount3,amount3 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                item_list3.append(r)


    except Exception as ex:
        print(ex)

def get_item4_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item4name,qty4,unit4,unitprice4,dec4,desamount4,amount4 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                item_list4.append(r)


    except Exception as ex:
        print(ex)

def get_item5_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item5name,qty5,unit5,unitprice5,dec5,desamount5,amount5 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                item_list5.append(r)


    except Exception as ex:
        print(ex)

def get_item6_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item6name,qty6,unit6,unitprice6,dec6,desamount6,amount6 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                item_list6.append(r)

    except Exception as ex:
        print(ex)

def get_item7_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item7name,qty7,unit7,unitprice7,dec7,desamount7,amount7 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                item_list7.append(r)

    except Exception as ex:
        print(ex)

def get_item8_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item8name,qty8,unit8,unitprice8,dec8,desamount8,amount8 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                item_list8.append(r)

    except Exception as ex:
        print(ex)

def get_item9_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item9name,qty9,unit9,unitprice9,dec9,desamount9,amount9 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:
                item_list9.append(r)


    except Exception as ex:
        print(ex)

def get_item10_data():
    con=sqlite3.connect(database=r'DataBase/ims.db')
    cur=con.cursor()
    try:

        cur.execute("select item10name,qty10,unit10,unitprice10,dec10,desamount10,amount10 from invosale where sid=1")
        rows=cur.fetchall()

        for row in rows:
            for r in row:

                item_list10.append(r)

    except Exception as ex:
        print(ex)
def hsn_list():
    if item_list1[0] == "":
        itmlist.append("")
    elif item_list2[0] == "":
        itmlist.append(item_list1[0])
    elif item_list3[0] == "":
        itmlist.append(item_list1[0])
        itmlist.append(item_list2[0])

    elif item_list4[0] == "":
        itmlist.append(item_list1[0])
        itmlist.append(item_list2[0])
        itmlist.append(item_list3[0])

    elif item_list5[0] == "":
        itmlist.append(item_list1[0])
        itmlist.append(item_list2[0])
        itmlist.append(item_list3[0])
        itmlist.append(item_list4[0])

    elif item_list6[0] == "":
        itmlist.append(item_list1[0])
        itmlist.append(item_list2[0])
        itmlist.append(item_list3[0])
        itmlist.append(item_list4[0])
        itmlist.append(item_list5[0])

    elif item_list7[0] == "":
        itmlist.append(item_list1[0])
        itmlist.append(item_list2[0])
        itmlist.append(item_list3[0])
        itmlist.append(item_list4[0])
        itmlist.append(item_list5[0])
        itmlist.append(item_list6[0])

    elif item_list8[0] == "":
        itmlist.append(item_list1[0])
        itmlist.append(item_list2[0])
        itmlist.append(item_list3[0])
        itmlist.append(item_list4[0])
        itmlist.append(item_list5[0])
        itmlist.append(item_list6[0])
        itmlist.append(item_list7[0])

    elif item_list9[0] == "":
        itmlist.append(item_list1[0])
        itmlist.append(item_list2[0])
        itmlist.append(item_list3[0])
        itmlist.append(item_list4[0])
        itmlist.append(item_list5[0])
        itmlist.append(item_list6[0])
        itmlist.append(item_list7[0])
        itmlist.append(item_list8[0])

    elif item_list10[0] == "":
        itmlist.append(item_list1[0])
        itmlist.append(item_list2[0])
        itmlist.append(item_list3[0])
        itmlist.append(item_list4[0])
        itmlist.append(item_list5[0])
        itmlist.append(item_list6[0])
        itmlist.append(item_list7[0])
        itmlist.append(item_list8[0])
        itmlist.append(item_list9[0])

    elif item_list10[0] != "":
        itmlist.append(item_list1[0])
        itmlist.append(item_list2[0])
        itmlist.append(item_list3[0])
        itmlist.append(item_list4[0])
        itmlist.append(item_list5[0])
        itmlist.append(item_list6[0])
        itmlist.append(item_list7[0])
        itmlist.append(item_list8[0])
        itmlist.append(item_list9[0])
        itmlist.append(item_list10[0])

def get_hsn():
    hsn_list()

    for i in itmlist:

      con=sqlite3.connect(database=r'DataBase/ims.db')
      cur=con.cursor()
      try:

        cur.execute(f"select hsn from itemdata where itemname LIKE '%{i}%'")
        rows=cur.fetchall()
        for row in rows:
            for r in row:
               hsn_no_list.append(r)

      except Exception as ex:
        print(ex)


def addlist():
    if item_list1[0] == "":
        item_list.append("")
    elif item_list2[0] == "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])

    elif item_list3[0] == "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])
        item_list2.insert(0, 2)
        item_list.append(item_list2)
        item_list2.insert(2, hsn_no_list[1])

    elif item_list4[0] == "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])

        item_list2.insert(0, 2)
        item_list.append(item_list2)
        item_list2.insert(2, hsn_no_list[1])
       
        item_list3.insert(0, 3)
        item_list.append(item_list3)
        item_list3.insert(2, hsn_no_list[2])


    elif item_list5[0] == "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])
        
        item_list2.insert(0, 2)
        item_list.append(item_list2)
        item_list2.insert(2, hsn_no_list[1])
       
        item_list3.insert(0, 3)
        item_list.append(item_list3)
        item_list3.insert(2, hsn_no_list[2])
       
        item_list4.insert(0, 4)
        item_list.append(item_list4)
        item_list4.insert(2, hsn_no_list[3])

    elif item_list6[0] == "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])
       
        item_list2.insert(0, 2)
        item_list.append(item_list2)
        item_list2.insert(2, hsn_no_list[1])
     
        item_list3.insert(0, 3)
        item_list.append(item_list3)
        item_list3.insert(2, hsn_no_list[2])
       
        item_list4.insert(0, 4)
        item_list.append(item_list4)
        item_list4.insert(2, hsn_no_list[3])
      
        item_list5.insert(0, 5)
        item_list.append(item_list5)
        item_list5.insert(2, hsn_no_list[4])

    elif item_list7[0] == "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])
       
        item_list2.insert(0, 2)
        item_list.append(item_list2)
        item_list2.insert(2, hsn_no_list[1])
   
        item_list3.insert(0, 3)
        item_list.append(item_list3)
        item_list3.insert(2, hsn_no_list[2])
    
        item_list4.insert(0, 4)
        item_list.append(item_list4)
        item_list4.insert(2, hsn_no_list[3])
      
        item_list5.insert(0, 5)
        item_list.append(item_list5)
        item_list5.insert(2, hsn_no_list[4])
    
        item_list6.insert(0, 6)
        item_list.append(item_list6)
        item_list6.insert(2, hsn_no_list[5])

    elif item_list8[0] == "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])
     
        item_list2.insert(0, 2)
        item_list.append(item_list2)
        item_list2.insert(2, hsn_no_list[1])
      
        item_list3.insert(0, 3)
        item_list.append(item_list3)
        item_list3.insert(2, hsn_no_list[2])
      
        item_list4.insert(0, 4)
        item_list.append(item_list4)
        item_list4.insert(2, hsn_no_list[3])
       
        item_list5.insert(0, 5)
        item_list.append(item_list5)
        item_list5.insert(2, hsn_no_list[4])
      
        item_list6.insert(0, 6)
        item_list.append(item_list6)
        item_list6.insert(2, hsn_no_list[5])
      
        item_list7.insert(0, 7)
        item_list.append(item_list7)
        item_list7.insert(2, hsn_no_list[6])

    elif item_list9[0] == "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])
      
        item_list2.insert(0, 2)
        item_list.append(item_list2)
        item_list2.insert(2, hsn_no_list[1])
     
        item_list3.insert(0, 3)
        item_list.append(item_list3)
        item_list3.insert(2, hsn_no_list[2])
      
        item_list4.insert(0, 4)
        item_list.append(item_list4)
        item_list4.insert(2, hsn_no_list[3])
    
        item_list5.insert(0, 5)
        item_list.append(item_list5)
        item_list5.insert(2, hsn_no_list[4])
     
        item_list6.insert(0, 6)
        item_list.append(item_list6)
        item_list6.insert(2, hsn_no_list[5])
     
        item_list7.insert(0, 7)
        item_list.append(item_list7)
        item_list7.insert(2, hsn_no_list[6])
     
        item_list8.insert(0, 8)
        item_list.append(item_list8)
        item_list8.insert(2, hsn_no_list[7])


    elif item_list10[0] == "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])
      
        item_list2.insert(0, 2)
        item_list.append(item_list2)
        item_list2.insert(2, hsn_no_list[1])
      
        item_list3.insert(0, 3)
        item_list.append(item_list3)
        item_list3.insert(2, hsn_no_list[2])
     
        item_list4.insert(0, 4)
        item_list.append(item_list4)
        item_list4.insert(2, hsn_no_list[3])
      
        item_list5.insert(0, 5)
        item_list.append(item_list5)
        item_list5.insert(2, hsn_no_list[4])
    
        item_list6.insert(0, 6)
        item_list.append(item_list6)
        item_list6.insert(2, hsn_no_list[5])
      
        item_list7.insert(0, 7)
        item_list.append(item_list7)
        item_list7.insert(2, hsn_no_list[6])
      
        item_list8.insert(0, 8)
        item_list.append(item_list8)
        item_list8.insert(2, hsn_no_list[7])
      
        item_list9.insert(0, 9)
        item_list.append(item_list9)
        item_list9.insert(2, hsn_no_list[8])

    elif item_list10[0] != "":
        item_list1.insert(0, 1)
        item_list.append(item_list1)
        item_list1.insert(2, hsn_no_list[0])
      
        item_list2.insert(0, 2)
        item_list.append(item_list2)
        item_list2.insert(2, hsn_no_list[1])
     
        item_list3.insert(0, 3)
        item_list.append(item_list3)
        item_list3.insert(2, hsn_no_list[2])
     
        item_list4.insert(0, 4)
        item_list.append(item_list4)
        item_list4.insert(2, hsn_no_list[3])
      
        item_list5.insert(0, 5)
        item_list.append(item_list5)
        item_list5.insert(2, hsn_no_list[4])
      
        item_list6.insert(0, 6)
        item_list.append(item_list6)
        item_list6.insert(2, hsn_no_list[5])
     
        item_list7.insert(0, 7)
        item_list.append(item_list7)
        item_list7.insert(2, hsn_no_list[6])
      
        item_list8.insert(0, 8)
        item_list.append(item_list8)
        item_list8.insert(2, hsn_no_list[7])
      
        item_list9.insert(0, 9)
        item_list.append(item_list9)
        item_list9.insert(2, hsn_no_list[8])
      
        item_list10.insert(0, 10)
        item_list.append(item_list10)
        item_list10.insert(2, hsn_no_list[9])
     


get_partybi_data()
get_item1_data()
get_item2_data()
get_item3_data()
get_item4_data()
get_item5_data()
get_item6_data()
get_item7_data()
get_item8_data()
get_item9_data()
get_item10_data()

gatpartyam()

get_hsn()
addlist()

totalinword = num2words(partydata_list[9])
tta = capwords(totalinword)

get_item_data()
print(partyam)
# doc.render({"company" : "VEDIKA MEDICAL", "phone" : "9049054282", "nam" : partydata_list[0],"partynumber" : partydata_list[1],"invoice":partydata_list[4],"date":partydata_list[5],"tota":partydata_list[9],"total":partyam[0],"disc":partydata_list[10],"final":partyam[1],"totalqty":partydata_list[14],"item_list":item_list,"amtinword":tta})
# doc.save("DataBase/Invoice/new_sale_sampleinvoice.docx")
# filename = f"SaleInvoice/{partydata_list[0]}_{partydata_list[4]}.pdf"
# path = f"SaleInvoice/{partydata_list[0]}_{partydata_list[4]}.pdf"
# convert("DataBase/Invoice/new_sale_sampleinvoice.docx", filename)
# subprocess.Popen([path], shell=True)
#
