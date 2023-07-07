import sqlite3
from subprocess import call

partyname_entry=""
phonenumber_entry=""
gstin_entry=""
crstete=""
invoice_entry=""
date_entry=""
state_menu=""
Payment_type_entry=""
Cheque_entry=""
Total_entry=""
Received_entry=""
balence=""

no1_item_entry=""
no1_qty_entry=""
no1_unit_entry=""
no1_unitprice_entry=""
no1_dec_percentagee_entry=""
no1_dec_amount_entry=""
no1_tax_percentagee_entry=""
no1_tax_amount_entry=""
no1_amount_entry=""

no2_item_entry=""
no2_qty_entry=""
no2_unit_entry=""
no2_unitprice_entry=""
no2_dec_percentagee_entry=""
no2_dec_amount_entry=""
no2_tax_percentagee_entry=""
no2_tax_amount_entry=""
no2_amount_entry=""

no3_item_entry=""
no3_qty_entry=""
no3_unit_entry=""
no3_unitprice_entry=""
no3_dec_percentagee_entry=""
no3_dec_amount_entry=""
no3_tax_percentagee_entry=""
no3_tax_amount_entry=""
no3_amount_entry=""

no4_item_entry=""
no4_qty_entry=""
no4_unit_entry=""
no4_unitprice_entry=""
no4_dec_percentagee_entry=""
no4_dec_amount_entry=""
no4_tax_percentagee_entry=""
no4_tax_amount_entry=""
no4_amount_entry=""

no5_item_entry=""
no5_qty_entry=""
no5_unit_entry=""
no5_unitprice_entry=""
no5_dec_percentagee_entry=""
no5_dec_amount_entry=""
no5_tax_percentagee_entry=""
no5_tax_amount_entry=""
no5_amount_entry=""

no6_item_entry=""
no6_qty_entry=""
no6_unit_entry=""
no6_unitprice_entry=""
no6_dec_percentagee_entry=""
no6_dec_amount_entry=""
no6_tax_percentagee_entry=""
no6_tax_amount_entry=""
no6_amount_entry=""

no7_item_entry=""
no7_qty_entry=""
no7_unit_entry=""
no7_unitprice_entry=""
no7_dec_percentagee_entry=""
no7_dec_amount_entry=""
no7_tax_percentagee_entry=""
no7_tax_amount_entry=""
no7_amount_entry=""

no8_item_entry=""
no8_qty_entry=""
no8_unit_entry=""
no8_unitprice_entry=""
no8_dec_percentagee_entry=""
no8_dec_amount_entry=""
no8_tax_percentagee_entry=""
no8_tax_amount_entry=""
no8_amount_entry=""

no9_item_entry=""
no9_qty_entry=""
no9_unit_entry=""
no9_unitprice_entry=""
no9_dec_percentagee_entry=""
no9_dec_amount_entry=""
no9_tax_percentagee_entry=""
no9_tax_amount_entry=""
no9_amount_entry=""

no10_item_entry=""
no10_qty_entry=""
no10_unit_entry=""
no10_unitprice_entry=""
no10_dec_percentagee_entry=""
no10_dec_amount_entry=""
no10_tax_percentagee_entry=""
no10_tax_amount_entry=""
no10_amount_entry=""

estimate_invoice=""
estimate_invoice_list=[]
estimate_total_invoice_list=[]

def start():
  getdata()

def getinvoice():
        con = sqlite3.connect(database=r'DataBase/ims.db')
        cur = con.cursor()
        try:

            cur.execute("select invoice from estimatetoinvo where no=1")
            rows=cur.fetchall()
            for row in rows:
              for r in row:
                return r

        except Exception as ex:
            print(ex)


def getdata():
  con = sqlite3.connect(database=r'DataBase/ims.db')
  cur = con.cursor()
  try:

    cur.execute(f"select partyname,phonenumber,gstin,cashorcr,invoiceno,invoicedate,steteofsuply,paymentype,refreceno,total,received,balance,item1name,qty1,unit1,unitprice1,dec1,desamount1,tax1,gstamount1,amount1,item2name,qty2,unit2,unitprice2,dec2,desamount2,tax2,gstamount2,amount2,item3name,qty3,unit3,unitprice3,dec3,desamount3,tax3,gstamount3,amount3,item4name,qty4,unit4,unitprice4,dec4,desamount4,tax4,gstamount4,amount4,item5name,qty5,unit5,unitprice5,dec5,desamount5,tax5,gstamount5,amount5,item6name,qty6,unit6,unitprice6,dec6,desamount6,tax6,gstamount6,amount6,item7name,qty7,unit7,unitprice7,dec7,desamount7,tax7,gstamount7,amount7,item8name,qty8,unit8,unitprice8,dec8,desamount8,tax8,gstamount8,amount8,item9name,qty9,unit9,unitprice9,dec9,desamount9,tax9,gstamount9,amount9,item10name,qty10,unit10,unitprice10,dec10,desamount10,tax10,gstamount10,amount10 from estimateinvogstsale where sid=1")
    rows = cur.fetchall()
    for row in rows:
      for r in row:
          estimate_invoice_list.append(r)

    cur.execute(f"select totaltac,totaldec,totalqty from estimateinvogstsale where sid=1")
    rows = cur.fetchall()
    for row in rows:
      for r in row:
        estimate_total_invoice_list.append(r)


    datastore()
    print("Success", "supplier Addedd Successfully")
  except Exception as ex:
    print("Error", f"Error due to : {str(ex)}")

def datastore():
  partyname_entry=estimate_invoice_list[0]
  phonenumber_entry=estimate_invoice_list[1]
  gstin_entry=estimate_invoice_list[2]
  crstete=estimate_invoice_list[3]
  invoice_entry=getinvoice()
  date_entry=estimate_invoice_list[5]
  state_menu=estimate_invoice_list[6]
  Payment_type_entry=estimate_invoice_list[7]
  Cheque_entry=estimate_invoice_list[8]
  Total_entry=estimate_invoice_list[9]
  Received_entry=estimate_invoice_list[10]
  balence=estimate_invoice_list[11]

  no1_item_entry=estimate_invoice_list[12]
  no1_qty_entry=estimate_invoice_list[13]
  no1_unit_entry=estimate_invoice_list[14]
  no1_unitprice_entry=estimate_invoice_list[15]
  no1_dec_percentagee_entry=estimate_invoice_list[16]
  no1_dec_amount_entry=estimate_invoice_list[17]
  no1_tax_percentagee_entry=estimate_invoice_list[18]
  no1_tax_amount_entry=estimate_invoice_list[19]
  no1_amount_entry=estimate_invoice_list[20]

  no2_item_entry=estimate_invoice_list[21]
  no2_qty_entry=estimate_invoice_list[22]
  no2_unit_entry=estimate_invoice_list[23]
  no2_unitprice_entry=estimate_invoice_list[24]
  no2_dec_percentagee_entry=estimate_invoice_list[25]
  no2_dec_amount_entry=estimate_invoice_list[26]
  no2_tax_percentagee_entry=estimate_invoice_list[27]
  no2_tax_amount_entry=estimate_invoice_list[28]
  no2_amount_entry=estimate_invoice_list[29]

  no3_item_entry=estimate_invoice_list[30]
  no3_qty_entry=estimate_invoice_list[31]
  no3_unit_entry=estimate_invoice_list[32]
  no3_unitprice_entry=estimate_invoice_list[33]
  no3_dec_percentagee_entry=estimate_invoice_list[34]
  no3_dec_amount_entry=estimate_invoice_list[35]
  no3_tax_percentagee_entry=estimate_invoice_list[36]
  no3_tax_amount_entry=estimate_invoice_list[37]
  no3_amount_entry=estimate_invoice_list[38]

  no4_item_entry=estimate_invoice_list[39]
  no4_qty_entry=estimate_invoice_list[40]
  no4_unit_entry=estimate_invoice_list[41]
  no4_unitprice_entry=estimate_invoice_list[42]
  no4_dec_percentagee_entry=estimate_invoice_list[43]
  no4_dec_amount_entry=estimate_invoice_list[44]
  no4_tax_percentagee_entry=estimate_invoice_list[45]
  no4_tax_amount_entry=estimate_invoice_list[46]
  no4_amount_entry=estimate_invoice_list[47]

  no5_item_entry=estimate_invoice_list[48]
  no5_qty_entry=estimate_invoice_list[49]
  no5_unit_entry=estimate_invoice_list[50]
  no5_unitprice_entry=estimate_invoice_list[51]
  no5_dec_percentagee_entry=estimate_invoice_list[52]
  no5_dec_amount_entry=estimate_invoice_list[53]
  no5_tax_percentagee_entry=estimate_invoice_list[54]
  no5_tax_amount_entry=estimate_invoice_list[55]
  no5_amount_entry=estimate_invoice_list[56]

  no6_item_entry=estimate_invoice_list[57]
  no6_qty_entry=estimate_invoice_list[58]
  no6_unit_entry=estimate_invoice_list[59]
  no6_unitprice_entry=estimate_invoice_list[60]
  no6_dec_percentagee_entry=estimate_invoice_list[61]
  no6_dec_amount_entry=estimate_invoice_list[62]
  no6_tax_percentagee_entry=estimate_invoice_list[63]
  no6_tax_amount_entry=estimate_invoice_list[64]
  no6_amount_entry=estimate_invoice_list[65]

  no7_item_entry=estimate_invoice_list[66]
  no7_qty_entry=estimate_invoice_list[67]
  no7_unit_entry=estimate_invoice_list[68]
  no7_unitprice_entry=estimate_invoice_list[69]
  no7_dec_percentagee_entry=estimate_invoice_list[70]
  no7_dec_amount_entry=estimate_invoice_list[71]
  no7_tax_percentagee_entry=estimate_invoice_list[72]
  no7_tax_amount_entry=estimate_invoice_list[73]
  no7_amount_entry=estimate_invoice_list[74]

  no8_item_entry=estimate_invoice_list[75]
  no8_qty_entry=estimate_invoice_list[76]
  no8_unit_entry=estimate_invoice_list[77]
  no8_unitprice_entry=estimate_invoice_list[78]
  no8_dec_percentagee_entry=estimate_invoice_list[79]
  no8_dec_amount_entry=estimate_invoice_list[80]
  no8_tax_percentagee_entry=estimate_invoice_list[81]
  no8_tax_amount_entry=estimate_invoice_list[82]
  no8_amount_entry=estimate_invoice_list[83]

  no9_item_entry=estimate_invoice_list[84]
  no9_qty_entry=estimate_invoice_list[85]
  no9_unit_entry=estimate_invoice_list[86]
  no9_unitprice_entry=estimate_invoice_list[87]
  no9_dec_percentagee_entry=estimate_invoice_list[88]
  no9_dec_amount_entry=estimate_invoice_list[89]
  no9_tax_percentagee_entry=estimate_invoice_list[90]
  no9_tax_amount_entry=estimate_invoice_list[91]
  no9_amount_entry=estimate_invoice_list[92]

  no10_item_entry=estimate_invoice_list[93]
  no10_qty_entry=estimate_invoice_list[94]
  no10_unit_entry=estimate_invoice_list[95]
  no10_unitprice_entry=estimate_invoice_list[96]
  no10_dec_percentagee_entry=estimate_invoice_list[97]
  no10_dec_amount_entry=estimate_invoice_list[98]
  no10_tax_percentagee_entry=estimate_invoice_list[99]
  no10_tax_amount_entry=estimate_invoice_list[100]
  no10_amount_entry=estimate_invoice_list[101]

  diccc=estimate_total_invoice_list[0]
  kk=estimate_total_invoice_list[1]
  allqty=estimate_total_invoice_list[2]


  recive=get_party_payamount(partyname_entry)
  get_amount(recive,Received_entry,Total_entry,gstin_entry)

  inv0= invoice_genrator()
  for i in inv0:
    print(i)
    invoice_entry=i

  invoice_updator(invoice_entry)

  con = sqlite3.connect(database=r'DataBase/ims.db')
  cur = con.cursor()
  try:
      cur.execute(
        "Insert into gstsale (partyname,phonenumber,gstin,cashorcr,invoiceno,invoicedate,steteofsuply,paymentype,refreceno,total,received,balance,item1name,qty1,unit1,unitprice1,dec1,desamount1,tax1,gstamount1,amount1,item2name,qty2,unit2,unitprice2,dec2,desamount2,tax2,gstamount2,amount2,item3name,qty3,unit3,unitprice3,dec3,desamount3,tax3,gstamount3,amount3,item4name,qty4,unit4,unitprice4,dec4,desamount4,tax4,gstamount4,amount4,item5name,qty5,unit5,unitprice5,dec5,desamount5,tax5,gstamount5,amount5,item6name,qty6,unit6,unitprice6,dec6,desamount6,tax6,gstamount6,amount6,item7name,qty7,unit7,unitprice7,dec7,desamount7,tax7,gstamount7,amount7,item8name,qty8,unit8,unitprice8,dec8,desamount8,tax8,gstamount8,amount8,item9name,qty9,unit9,unitprice9,dec9,desamount9,tax9,gstamount9,amount9,item10name,qty10,unit10,unitprice10,dec10,desamount10,tax10,gstamount10,amount10) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (

          partyname_entry,
          phonenumber_entry,
          gstin_entry,
          crstete,
          invoice_entry,
          date_entry,
          state_menu,
          Payment_type_entry,
          Cheque_entry,
          Total_entry,
          Received_entry,
          balence,

          no1_item_entry,
          no1_qty_entry,
          no1_unit_entry,
          no1_unitprice_entry,
          no1_dec_percentagee_entry,
          no1_dec_amount_entry,
          no1_tax_percentagee_entry,
          no1_tax_amount_entry,
          no1_amount_entry,

          no2_item_entry,
          no2_qty_entry,
          no2_unit_entry,
          no2_unitprice_entry,
          no2_dec_percentagee_entry,
          no2_dec_amount_entry,
          no2_tax_percentagee_entry,
          no2_tax_amount_entry,
          no2_amount_entry,

          no3_item_entry,
          no3_qty_entry,
          no3_unit_entry,
          no3_unitprice_entry,
          no3_dec_percentagee_entry,
          no3_dec_amount_entry,
          no3_tax_percentagee_entry,
          no3_tax_amount_entry,
          no3_amount_entry,

          no4_item_entry,
          no4_qty_entry,
          no4_unit_entry,
          no4_unitprice_entry,
          no4_dec_percentagee_entry,
          no4_dec_amount_entry,
          no4_tax_percentagee_entry,
          no4_tax_amount_entry,
          no4_amount_entry,

          no5_item_entry,
          no5_qty_entry,
          no5_unit_entry,
          no5_unitprice_entry,
          no5_dec_percentagee_entry,
          no5_dec_amount_entry,
          no5_tax_percentagee_entry,
          no5_tax_amount_entry,
          no5_amount_entry,

          no6_item_entry,
          no6_qty_entry,
          no6_unit_entry,
          no6_unitprice_entry,
          no6_dec_percentagee_entry,
          no6_dec_amount_entry,
          no6_tax_percentagee_entry,
          no6_tax_amount_entry,
          no6_amount_entry,

          no7_item_entry,
          no7_qty_entry,
          no7_unit_entry,
          no7_unitprice_entry,
          no7_dec_percentagee_entry,
          no7_dec_amount_entry,
          no7_tax_percentagee_entry,
          no7_tax_amount_entry,
          no7_amount_entry,

          no8_item_entry,
          no8_qty_entry,
          no8_unit_entry,
          no8_unitprice_entry,
          no8_dec_percentagee_entry,
          no8_dec_amount_entry,
          no8_tax_percentagee_entry,
          no8_tax_amount_entry,
          no8_amount_entry,

          no9_item_entry,
          no9_qty_entry,
          no9_unit_entry,
          no9_unitprice_entry,
          no9_dec_percentagee_entry,
          no9_dec_amount_entry,
          no9_tax_percentagee_entry,
          no9_tax_amount_entry,
          no9_amount_entry,

          no10_item_entry,
          no10_qty_entry,
          no10_unit_entry,
          no10_unitprice_entry,
          no10_dec_percentagee_entry,
          no10_dec_amount_entry,
          no10_tax_percentagee_entry,
          no10_tax_amount_entry,
          no10_amount_entry,

        ))
      con.commit()

  except Exception as ex:
      print("Error", f"Error due to : {str(ex)}")

  con = sqlite3.connect(database=r'DataBase/ims.db')
  cur = con.cursor()
  try:
   cur.execute("Select * from invogstsale where sid=1")

   cur.execute(
    "Update invogstsale set partyname=?,phonenumber=?,gstin=?,cashorcr=?,invoiceno=?,invoicedate=?,steteofsuply=?,paymentype=?,refreceno=?,total=?,received=?,balance=?,totaltac=?,totaldec=?,totalqty=?,item1name=?,qty1=?,unit1=?,unitprice1=?,dec1=?,desamount1=?,tax1=?,gstamount1=?,amount1=?,item2name=?,qty2=?,unit2=?,unitprice2=?,dec2=?,desamount2=?,tax2=?,gstamount2=?,amount2=?,item3name=?,qty3=?,unit3=?,unitprice3=?,dec3=?,desamount3=?,tax3=?,gstamount3=?,amount3=?,item4name=?,qty4=?,unit4=?,unitprice4=?,dec4=?,desamount4=?,tax4=?,gstamount4=?,amount4=?,item5name=?,qty5=?,unit5=?,unitprice5=?,dec5=?,desamount5=?,tax5=?,gstamount5=?,amount5=?,item6name=?,qty6=?,unit6=?,unitprice6=?,dec6=?,desamount6=?,tax6=?,gstamount6=?,amount6=?,item7name=?,qty7=?,unit7=?,unitprice7=?,dec7=?,desamount7=?,tax7=?,gstamount7=?,amount7=?,item8name=?,qty8=?,unit8=?,unitprice8=?,dec8=?,desamount8=?,tax8=?,gstamount8=?,amount8=?,item9name=?,qty9=?,unit9=?,unitprice9=?,dec9=?,desamount9=?,tax9=?,gstamount9=?,amount9=?,item10name=?,qty10=?,unit10=?,unitprice10=?,dec10=?,desamount10=?,tax10=?,gstamount10=?,amount10=?",
    (

      partyname_entry,
      phonenumber_entry,
      gstin_entry,
      crstete,
      invoice_entry,
      date_entry,
      state_menu,
      Payment_type_entry,
      Cheque_entry,
      Total_entry,
      Received_entry,
      balence,
      diccc,
      kk,
      allqty,

      no1_item_entry,
      no1_qty_entry,
      no1_unit_entry,
      no1_unitprice_entry,
      no1_dec_percentagee_entry,
      no1_dec_amount_entry,
      no1_tax_percentagee_entry,
      no1_tax_amount_entry,
      no1_amount_entry,

      no2_item_entry,
      no2_qty_entry,
      no2_unit_entry,
      no2_unitprice_entry,
      no2_dec_percentagee_entry,
      no2_dec_amount_entry,
      no2_tax_percentagee_entry,
      no2_tax_amount_entry,
      no2_amount_entry,

      no3_item_entry,
      no3_qty_entry,
      no3_unit_entry,
      no3_unitprice_entry,
      no3_dec_percentagee_entry,
      no3_dec_amount_entry,
      no3_tax_percentagee_entry,
      no3_tax_amount_entry,
      no3_amount_entry,

      no4_item_entry,
      no4_qty_entry,
      no4_unit_entry,
      no4_unitprice_entry,
      no4_dec_percentagee_entry,
      no4_dec_amount_entry,
      no4_tax_percentagee_entry,
      no4_tax_amount_entry,
      no4_amount_entry,

      no5_item_entry,
      no5_qty_entry,
      no5_unit_entry,
      no5_unitprice_entry,
      no5_dec_percentagee_entry,
      no5_dec_amount_entry,
      no5_tax_percentagee_entry,
      no5_tax_amount_entry,
      no5_amount_entry,

      no6_item_entry,
      no6_qty_entry,
      no6_unit_entry,
      no6_unitprice_entry,
      no6_dec_percentagee_entry,
      no6_dec_amount_entry,
      no6_tax_percentagee_entry,
      no6_tax_amount_entry,
      no6_amount_entry,

      no7_item_entry,
      no7_qty_entry,
      no7_unit_entry,
      no7_unitprice_entry,
      no7_dec_percentagee_entry,
      no7_dec_amount_entry,
      no7_tax_percentagee_entry,
      no7_tax_amount_entry,
      no7_amount_entry,

      no8_item_entry,
      no8_qty_entry,
      no8_unit_entry,
      no8_unitprice_entry,
      no8_dec_percentagee_entry,
      no8_dec_amount_entry,
      no8_tax_percentagee_entry,
      no8_tax_amount_entry,
      no8_amount_entry,

      no9_item_entry,
      no9_qty_entry,
      no9_unit_entry,
      no9_unitprice_entry,
      no9_dec_percentagee_entry,
      no9_dec_amount_entry,
      no9_tax_percentagee_entry,
      no9_tax_amount_entry,
      no9_amount_entry,

      no10_item_entry,
      no10_qty_entry,
      no10_unit_entry,
      no10_unitprice_entry,
      no10_dec_percentagee_entry,
      no10_dec_amount_entry,
      no10_tax_percentagee_entry,
      no10_tax_amount_entry,
      no10_amount_entry,

      ))
   con.commit()

  except Exception as ex:
     print(ex)

  update_item_qty(no1_item_entry, no1_qty_entry)
  update_item_qty(no2_item_entry,no2_qty_entry)
  update_item_qty(no3_item_entry, no3_qty_entry)
  update_item_qty(no4_item_entry, no4_qty_entry)
  update_item_qty(no5_item_entry, no5_qty_entry)
  update_item_qty(no6_item_entry, no6_qty_entry)
  update_item_qty(no7_item_entry, no7_qty_entry)
  update_item_qty(no8_item_entry, no8_qty_entry)
  update_item_qty(no9_item_entry, no9_qty_entry)
  update_item_qty(no10_item_entry, no10_qty_entry)

  invoice_event()
def invoice_event():
  call(["python", "GST_Invoice.py"])

def invoice_genrator():
  con = sqlite3.connect(database=r'DataBase/ims.db')
  cur = con.cursor()
  try:

    cur.execute("select invoice from invo where no=1", )
    rows = cur.fetchall()

    for row in rows:
      for i in row:
        invoice_zero = 6 - len(i)
        incre = int(i) + 1
        a = 1
        mm = "0"
        while a < invoice_zero:
          mm = mm + "0"
          a += 1
        final = f"{mm}{incre}"
        strfinal = str(final)
        invo=strfinal
        return  invo,

  except Exception as ex:
    print("Error", f"Error due to : {str(ex)}")


def invoice_updator(data):
  p = 1
  incre=data.replace("0","")
  print(incre)
  con = sqlite3.connect(database=r'DataBase/ims.db')
  cur = con.cursor()
  try:

    cur.execute("Select no from invo where no=?", (p,))
    row = cur.fetchone()
    cur.execute("Update invo set invoice=? where no=?", (
      incre,
      p,
    ))
    con.commit()
  except Exception as ex:
    print("Error", f"Error due to : {str(ex)}")

def update_item_qty(name, seto):
        if name == "":
            pass
        else:

          con = sqlite3.connect(database=r'DataBase/ims.db')
          cur = con.cursor()
          try:
              if seto=="":
                  pass
              else:
                  cur.execute("select openqty from itemdata where itemname=?", (name,))
                  rows = cur.fetchall()
                  b=seto
                  for row in rows:
                     for i in row:
                       resualt=int(i)-int(b)
                       cur.execute("select pid from itemdata where itemname=?", (name,))
                       pids = cur.fetchall()
                       for pid in pids:
                           for p in pid:

                              cur.execute("Select pid from itemdata where pid=?", (p,))
                              row = cur.fetchone()
                              cur.execute("Update itemdata set openqty=? where pid=?", (
                               resualt,
                                p,
                                ))
                              con.commit()

          except Exception as ex:
            print("Error", f"Error due to : {str(ex)}")



def get_party_payamount(partyname):

    con = sqlite3.connect(database=r'DataBase/ims.db')
    cur = con.cursor()
    try:

      cur.execute("select recivebalence from partydata where partyname=?", (partyname,))
      rows = cur.fetchall()

      for row in rows:
        for i in row:
          return i



    except Exception as ex:
      print("Error", f"Error due to : {str(ex)}")
def get_amount(recivee,payedd,totall,gstin):
        recive = float(recivee)
        payed = float(payedd)
        total = float(totall)

        esult = recive + (total - payed)
        result =str(esult)

        try:
          con = sqlite3.connect(database=r'DataBase/ims.db')
          cur = con.cursor()

          cur.execute(f"Select recivebalence from partydata where gstin={gstin}")
          cur.execute(f"Update partydata set recivebalence=? where gstin={gstin}", (
            result,
          ))
          con.commit()


        except Exception as ex:
          print(ex)

start()