from pyexpat import model
from sqlite3 import Cursor
import mysql.connector as c

con = c.connect(host="localhost",
                user= "root",
                passwd= "P@$$ward1",
                database= "tufail")
sql_select_Query = "select * from Tufail_Mobile"
Cursor = con.cursor()
Cursor.execute(sql_select_Query)
records = Cursor.fetchall()
print("Last Entered query: ", records[-1][2], records[-1][3])
SNo = Cursor.rowcount + 1
while True:
    list1 = []
    list1.append(SNo)
    Dates = input("Enter the Date: ")
    list1.append(Dates)
    Fname = input("Enter your name: ")
    list1.append(Fname)
    Model = input("Enter your model: ")
    list1.append(Model)
    Contact = input("Enter your contact: ")
    list1.append(Contact)
    Address = input("Enter the Address: ")
    list1.append(Address)
    ram = input("Enter the RAM: ")
    list1.append(ram)
    rom = input("Enter the ROM: ")
    list1.append(rom)
    imei1 = input("Enter the IMEI1: ")
    list1.append(imei1)
    imei2 = input("Enter the IMEI2: ")
    list1.append(imei2)
    Adhar = input("Enter the Adhar No: ")
    list1.append(Adhar)
    Pan = input("Enter the PAN No: ")
    list1.append(Pan)
    Driving_Liscence = input("Enter the Driving Liscence: ")
    list1.append(Driving_Liscence)
    Amount = input("Enter the Amount: ")
    list1.append(Amount)
    a = [x if x != "" else "-" for x in list1]
    query = "insert into Tufail_Mobile values ({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13])
    SNo = SNo + 1
    Cursor.execute(query)
    con.commit()
    print("Data Inserted....!")
    x = int(input("1-> Enter More\n2-> Exit\nEnter your choice: "))
    if x == 2:
        break