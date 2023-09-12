import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,name text,price text,qty text,status text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS remaing(uid INTEGER PRIMARY KEY AUTOINCREMENT,contact text,name text,ramount text,status text)")
    con.commit()


    # Item
    cur.execute("CREATE TABLE IF NOT EXISTS itemdata(pid INTEGER PRIMARY KEY AUTOINCREMENT,itemname text,hsn text,category text,itemcode text,saleprice text,tax1 text,discount text,dicst text,wholesaleprice text,tax2 text,minqty text,purchesprice text,gsttax text,openqty text,atprice text,exdate text,minstockmanten text,unit text,batch text,batch1 text,batch2 text,batch3 text,batch4 text,batch5 text,location text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS edititemdata(pid INTEGER PRIMARY KEY AUTOINCREMENT,itemname text,hsn text,category text,itemcode text,saleprice text,tax1 text,discount text,dicst text,wholesaleprice text,tax2 text,minqty text,purchesprice text,gsttax text,openqty text,atprice text,exdate text,minstockmanten text,unit text,batch text,batch1 text,batch2 text,batch3 text,batch4 text,batch5 text,location text)")
    con.commit()


    # Party
    cur.execute("CREATE TABLE IF NOT EXISTS partydata(pid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,gstin text,phonenumber text,gsttype text,amount text,state text,emailid text,billaddress text,shipaddress text,paybalence text,recivebalence text,date text,creditlim text,add1 text,add2 text,add3 text,add4 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS editpartydata(pid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,gstin text,phonenumber text,gsttype text,amount text,state text,emailid text,billaddress text,shipaddress text,paybalence text,recivebalence text,date text,creditlim text,add1 text,add2 text,add3 text,add4 text)")
    con.commit()


    # GST Sale
    cur.execute("CREATE TABLE IF NOT EXISTS gstsale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,item1name text,qty1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS editgstsale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,item1name text,qty1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS invogstsale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,totaltac text,totaldec text,totalqty text,item1name text,qty1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS editinvogstsale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,totaltac text,totaldec text,totalqty text,item1name text,qty1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS invo(no INTEGER PRIMARY KEY AUTOINCREMENT,invoice text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS estimateinvogstsale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,totaltac text,totaldec text,totalqty text,item1name text,qty1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS edittransction(no INTEGER PRIMARY KEY AUTOINCREMENT,invoice text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS estimateinvo(no INTEGER PRIMARY KEY AUTOINCREMENT,invoice text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS estimategstsale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,item1name text,qty1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS gstinvopartyam(no INTEGER PRIMARY KEY AUTOINCREMENT,partyam text,partyamtotal text)")
    con.commit()


    # Sale
    cur.execute("CREATE TABLE IF NOT EXISTS sale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,drname text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,totaldic text,netam text,received text,balance text,item1name text,qty1 text,free1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,amount1 text,item2name text,qty2 text,free2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,amount2 text,item3name text,qty3 text,free3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,amount3 text,item4name text,qty4 text,free4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,amount4 text,item5name text,qty5 text,free5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,amount5 text,item6name text,qty6 text,free6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,amount6 text,item7name text,qty7 text,free7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,amount7 text,item8name text,qty8 text,free8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,amount8 text,item9name text,qty9 text,free9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,amount9 text,item10name text,qty10 text,free10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS editsale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,drname text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,totaldic text,netam text,received text,balance text,item1name text,qty1 text,free1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,amount1 text,item2name text,qty2 text,free2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,amount2 text,item3name text,qty3 text,free3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,amount3 text,item4name text,qty4 text,free4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,amount4 text,item5name text,qty5 text,free5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,amount5 text,item6name text,qty6 text,free6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,amount6 text,item7name text,qty7 text,free7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,amount7 text,item8name text,qty8 text,free8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,amount8 text,item9name text,qty9 text,free9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,amount9 text,item10name text,qty10 text,free10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS salepaymentin(pid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,gstin text,phonenumber text,gsttype text,amount text,state text,emailid text,billaddress text,shipaddress text,paybalence text,recivebalence text,date text,creditlim text,paymenttype text,add2 text,add3 text,add4 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS invosale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,drname text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,totaldic text,netam text,received text,balance text,totaltac text,totaldec text,totalqty text,item1name text,qty1 text,free1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,amount1 text,item2name text,qty2 text,free2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,amount2 text,item3name text,qty3 text,free3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,amount3 text,item4name text,qty4 text,free4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,amount4 text,item5name text,qty5 text,free5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,amount5 text,item6name text,qty6 text,free6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,amount6 text,item7name text,qty7 text,free7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,amount7 text,item8name text,qty8 text,free8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,amount8 text,item9name text,qty9 text,free9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,amount9 text,item10name text,qty10 text,free10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS invosalenon(no INTEGER PRIMARY KEY AUTOINCREMENT,invoice text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS saleinvopartyam(no INTEGER PRIMARY KEY AUTOINCREMENT,partyam text,partyamtotal text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS saleinvopartyam(no INTEGER PRIMARY KEY AUTOINCREMENT,partyam text,partyamtotal text)")
    con.commit()


    # Puechase
    cur.execute("CREATE TABLE IF NOT EXISTS gstpurchase(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,item1name text,qty1 text,unit1 text,batch1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,batch2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,batch3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,batch4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,batch5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,batch6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,batch7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,batch8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,batch9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,batch10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS editgstpurchase(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,item1name text,qty1 text,unit1 text,batch1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,batch2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,batch3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,batch4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,batch5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,batch6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,batch7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,batch8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,batch9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,batch10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS invopurchasesale(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,totaltac text,totaldec text,totalqty text,item1name text,qty1 text,unit1 text,batch1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,batch2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,batch3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,batch4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,batch5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,batch6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,batch7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,batch8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,batch9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,batch10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS purinvo(no INTEGER PRIMARY KEY AUTOINCREMENT,invoice text)")
    con.commit()


    # Settings
    cur.execute("CREATE TABLE IF NOT EXISTS appearance(no INTEGER PRIMARY KEY AUTOINCREMENT,theme text,scelling text)")
    con.commit()


    cur.execute("CREATE TABLE IF NOT EXISTS estimate(sid INTEGER PRIMARY KEY AUTOINCREMENT,partyname text,phonenumber text,gstin text,cashorcr text,invoiceno text,invoicedate text,steteofsuply text,paymentype text,refreceno text,total text,received text,balance text,item1name text,qty1 text,unit1 text,unitprice1 text,dec1 text,desamount1 text,tax1 text,gstamount1 text,amount1 text,item2name text,qty2 text,unit2 text,unitprice2 text,dec2 text,desamount2 text,tax2 text,gstamount2 text,amount2 text,item3name text,qty3 text,unit3 text,unitprice3 text,dec3 text,desamount3 text,tax3 text,gstamount3 text,amount3 text,item4name text,qty4 text,unit4 text,unitprice4 text,dec4 text,desamount4 text,tax4 text,gstamount4 text,amount4 text,item5name text,qty5 text,unit5 text,unitprice5 text,dec5 text,desamount5 text,tax5 text,gstamount5 text,amount5 text,item6name text,qty6 text,unit6 text,unitprice6 text,dec6 text,desamount6 text,tax6 text,gstamount6 text,amount6 text,item7name text,qty7 text,unit7 text,unitprice7 text,dec7 text,desamount7 text,tax7 text,gstamount7 text,amount7 text,item8name text,qty8 text,unit8 text,unitprice8 text,dec8 text,desamount8 text,tax8 text,gstamount8 text,amount8 text,item9name text,qty9 text,unit9 text,unitprice9 text,dec9 text,desamount9 text,tax9 text,gstamount9 text,amount9 text,item10name text,qty10 text,unit10 text,unitprice10 text,dec10 text,desamount10 text,tax10 text,gstamount10 text,amount10 text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS estimatetoinvo(no INTEGER PRIMARY KEY AUTOINCREMENT,invoice text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS invsetting(no INTEGER PRIMARY KEY AUTOINCREMENT,gstivo text,saleinvo text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS qtysetting(no INTEGER PRIMARY KEY AUTOINCREMENT,gstqty text,saleqty text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS stocksetting(no INTEGER PRIMARY KEY AUTOINCREMENT,lowstock text)")
    con.commit()

create_db()