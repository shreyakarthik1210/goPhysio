from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

con = pymysql.connect(host="34.170.18.228", user="root", password="karthik", database= "physioUsers");

try:
    cur= con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id int, firstName varchar(32), lastName varchar(32), "
               +"Gender varchar(10), DOB varchar(15), email varchar(32), password varchar(32))")
except Exception as e:
    print("Error")


@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
     msg=''
     username = request.form.get('username')
     password = request.form.get('password')
     cur.execute("select * from users where email<> 'admin@gmail.com' and email = %s and password= %s",(username,password))
     acc=cur.fetchone()
     if acc:
        msg='Logged in successfully'
        return render_template('patientPortal.html',msg= msg)
     elif username=='admin@gmail.com':
         return render_template('doctor.html')
     else:
         msg="Invalid login"
     return render_template('login.html',msg=msg)
 
""" 

def index():
    return render_template('registration.html') """

@app.route('/register', methods=['GET','POST'])
def register():
 msg=''
 if(request.method=='POST' and 'username' in request.form):
    firstName = request.form.get("firstName")
    lastName = request.form.get("lastName")
    gender = request.form.get("gender")
    birthday = request.form.get("birth")
    email = request.form.get("username")
    password = request.form.get("password")
    

    # Basic validation
    """ if not email or not password or not firstName or not lastName or not birthday:
        return 'Registration failed. Please fill out the form correctly. <a href="/">Go back to registration</a>' """

    # Store user data 
    sql="INSERT INTO users (id,firstName,lastName,Gender,DOB,email,password) values (%s,%s,%s,%s,%s,%s,%s)"
    val=("10",firstName, lastName, gender, str(birthday), email, password)
    cur.execute(sql,val)
    con.commit()
    msg='Registration successful'
 elif request.method=='POST':
     msg='Fill form'
    # return f'Registration successful, {email}! You can now <a href="/login">Login</a>.'
 return render_template('register.html',msg=msg)



if __name__ == '__main__':
    app.run(debug=True)
