from email.policy import default
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# import flask_whooshalchemy3 as wa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mobile.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['WHOOSH_BASE'] = 'whoosh'
db = SQLAlchemy(app)

class Mobile(db.Model):
    __tablename__ = 'mobile'
    __searchable__ = ['Cust_Name','Model','Mob_No','Alt_No','RAM','ROM','Address','IMEI_1','IMEI_2','Adhar','PAN','Driv_Lisce','Amount']

    sno = db.Column(db.Integer, primary_key = True)
    Cust_Name = db.Column(db.String(30))
    Model = db.Column(db.String(20))
    Mob_No = db.Column(db.String(10))
    Alt_No = db.Column(db.String(10))
    RAM = db.Column(db.String(2))
    ROM = db.Column(db.String(3))
    Address = db.Column(db.String(200))
    IMEI_1 = db.Column(db.String(20))
    IMEI_2 = db.Column(db.String(20))
    Adhar = db.Column(db.String(12))
    PAN = db.Column(db.String(15))
    Driv_Lisce = db.Column(db.String(25))
    Amount = db.Column(db.String(10))

# wa.whoosh.index(app, Mobile)

@app.route("/", methods=['GET','POST'])
def main():
    if request.method=="POST":
        Cust_Name = request.form['Cust_Name'] 
        Model = request.form['Model'] 
        Mob_No = request.form['Mob_No']
        Alt_No = request.form['Alt_No'] 
        RAM = request.form['RAM']
        ROM = request.form['ROM'] 
        Address = request.form['Address']
        IMEI_1 = request.form['IMEI_1'] 
        IMEI_2 = request.form['IMEI_2']
        Adhar = request.form['Adhar'] 
        PAN = request.form['PAN']
        Driv_Lisce = request.form['Driv_Lisce'] 
        Amount = request.form['Amount']
        mobile = Mobile(Cust_Name=Cust_Name, Model=Model, Mob_No=Mob_No, Alt_No=Alt_No, RAM=RAM, ROM=ROM, Address=Address, IMEI_1=IMEI_1, IMEI_2=IMEI_2, Adhar=Adhar, PAN=PAN, Driv_Lisce=Driv_Lisce, Amount=Amount)
        db.session.add(mobile)
        db.session.commit()
    allMobile= Mobile.query.all()
    return render_template('index.html', allMobile = allMobile)

@app.route("/table")
def table():
    mobile= Mobile.query.all()
    return render_template('table.html', allMobile = mobile)
    
@app.route("/update/<int:sno>",methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        Cust_Name = request.form['Cust_Name'] 
        Model = request.form['Model'] 
        Mob_No = request.form['Mob_No']
        Alt_No = request.form['Alt_No'] 
        RAM = request.form['RAM']
        ROM = request.form['ROM'] 
        Address = request.form['Address']
        IMEI_1 = request.form['IMEI_1'] 
        IMEI_2 = request.form['IMEI_2']
        Adhar = request.form['Adhar'] 
        PAN = request.form['PAN']
        Driv_Lisce = request.form['Driv_Lisce'] 
        Amount = request.form['Amount']
        mobile= Mobile.query.filter_by(sno=sno).first()
        mobile.Cust_Name = Cust_Name
        mobile.Model = Model
        mobile.Mob_No = Mob_No
        mobile.Alt_No = Alt_No
        mobile.RAM = RAM
        mobile.ROM = ROM
        mobile.Address = Address
        mobile.IMEI_1 = IMEI_1
        mobile.IMEI_2 = IMEI_2
        mobile.Adhar = Adhar
        mobile.PAN = PAN
        mobile.Driv_Lisce = Driv_Lisce
        mobile.Amount = Amount
        db.session.add(mobile)
        db.session.commit()
        return redirect("/")
    mobile= Mobile.query.filter_by(sno=sno).first()
    return render_template('update.html', mobile=mobile)

@app.route("/delete/<int:sno>")
def delete(sno):
    mobile= Mobile.query.filter_by(sno=sno).first()
    db.session.delete(mobile)
    db.session.commit()
    return redirect("/")

@app.route("/about/")
def about():
    return render_template('about.html', title='about')

@app.route("/search",methods=['GET','POST'])
def search():
    allMobile= Mobile.query.whoosh_search(request.args.get('query')).all()

    return render_template('search.html', allMobile = allMobile)

if __name__ =="__main__":
    app.run(debug = True, port = 7500)

