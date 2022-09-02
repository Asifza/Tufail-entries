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
    var=['Sr No','Date','Name','Model','Contact','Address','RAM','ROM','IMEI1','IMEI2','Adhar','PAN','Driving Liscence','Amount']
    lis = []
    x = 0
    while x < len(var):
        if x == 0:
            print(SNo)
            lis.append(SNo)
            x += 1
        print(f"Enter {var[x]}: ", end='')
        z = input()
        if z == "Exit" or z == "exit":
            break
        else:
            lis.append(z)
            x += 1
    a = [y if y != "" else "-" for y in lis]
    try:
        query = "insert into Tufail_Mobile values ({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13])
    except:
        print("Error")
    SNo = SNo + 1
    Cursor.execute(query)
    con.commit()
    print("Data Inserted....!")
    x = int(input("1-> Enter More\n2-> Exit\nEnter your choice: "))
    if x == 2:
        break
    