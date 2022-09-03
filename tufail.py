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
print(f"Last Entered query: {records[-1][1]}, {records[-1][2]}, {records[-1][3]}")
SNo = Cursor.rowcount + 1

def check(Imei):
    for i in range (0, len(records)):
        if Imei == records[i][8]:
            print(records[i])
            i += 1
while True:
    var=['Sr No','Date','Name','Model','Contact','Address','RAM','ROM','IMEI1','IMEI2','Adhar','PAN','Driving Liscence','Amount']
    lis = []
    x = 0
    while x < len(var):
        g = int(input("1-> Enter Data\n2-> Search Data\n3-> Exit\nEnter your choice: "))
        if g == 2:
            Imei = input("Enter the data you want to search: ")
            check(Imei)
        elif g == 3:
            break
        else:
            if x == 0:
                print(f"Entry No: {SNo}")
                lis.append(SNo)
                x += 1
            print(f"Enter {var[x]}: ", end='')
            z = input()
            if z == "Exit" or z == "exit":
                break
            elif z == "Edit" or z == "edit":
                x -= 1
                lis.pop()
            else:
                lis.append(z)
                x += 1
    a = [y if y != "" else "-" for y in lis]
    records.append(tuple(a))
    try:
        query = "insert into Tufail_Mobile values ({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13])
    except:
        print("                                  !!! Entry Exited Midway Data Not Saved !!!")
    SNo = SNo + 1
    try:
        Cursor.execute(query)
    except:
        print("Entry Stopped.....!")
        break
    con.commit()
    print("Data Inserted....!")