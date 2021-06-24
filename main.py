from flask import Flask, render_template, request, redirect
from datetime import *
from flask_mysqldb import MySQL
import mysql.connector

global count
app = Flask(__name__, template_folder="template", static_folder="static")

# configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1417'
app.config['MYSQL_DB'] = 'edx'

mysql = MySQL(app)

user_login = 0
@app.route('/')
def home():

    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    return render_template('index.html',catDetails=catDetails)


@app.route('/courses')
def courses():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    return render_template('courses.html',catDetails=catDetails)

@app.route('/status')
def status():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    
    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    # ('103')
    for i in name1:
        userid = i
        # 103
    instValue = cur.execute("SELECT user_id FROM pending where user_id = %s",[userid])
    if instValue > 0:
        return render_template('status.html',catDetails=catDetails,msg="Your Application is not accepted Yet!")

    if instValue == 0:
        searchValue = cur.execute("SELECT user_id FROM instructors where user_id = %s",[userid])
        if searchValue > 0:
            return render_template('status.html',catDetails=catDetails,msg="You are selected!")
        else:
            return render_template('status.html',catDetails=catDetails,msg="You Did Not Apply!")
    return render_template('status.html',catDetails=catDetails)

@app.route('/binstructor', methods = ['GET','POST'])
def binstructor():
    cur = mysql.connection.cursor()
    # cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    courseValue = cur.execute("SELECT * FROM courses")
    if courseValue > 0:
        courseDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # course name
        course_name = request.form.get("name",None)
        print(course_name)
        finale = cur.execute("SELECT course_id FROM courses where course_name = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
        cur.execute("INSERT into pending(user_id,course_id) VALUES(%s,%s)",(userid,pidd))
        mysql.connection.commit()
        return render_template('status.html', msg='Request Has Been Sent!',catDetails=catDetails)
        # return redirect("/")
    return render_template('b_instructor.html',courseDetails = courseDetails,catDetails=catDetails)
    
@app.route('/about')
def about():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    return render_template('about.html',catDetails=catDetails)

@app.route('/uview')
def uview():
    cur = mysql.connection.cursor()
    # cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    userValue = cur.execute("SELECT * FROM users")
    if userValue > 0:
        userDetails = cur.fetchall()
    return render_template('view.html',userDetails=userDetails,catDetails=catDetails,uid="User_id",uname="Name",email="Email",table_name="User_Table")

@app.route('/iview')
def iview():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM users where user_id in (select user_id from instructors)")
    if instValue > 0:
        userDetails = cur.fetchall()
    return render_template('view.html',userDetails = userDetails,catDetails=catDetails,uid="User_id",uname="Name",email="Email",table_name="Instructor_Table")

@app.route('/cview')
def cview():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    bookValue = cur.execute("SELECT * from bookings,users,courses where bookings.user_id = users.user_id and bookings.course_id = courses.course_id")
    if bookValue > 0:
        bookDetails = cur.fetchall()
    return render_template('view.html',bookDetails = bookDetails,catDetails=catDetails,bid="Reg_id",bname="User_id",bemail="Name",cost="Cost",Course="Course",table_name="Registrations_Table")


@app.route('/Programming', methods = ['GET','POST'])
def programing():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    courseValue = cur.execute("SELECT * FROM courses where cat_id = 1111")
    if courseValue > 0:
        courseDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # course name
        course_name = request.form.get("name",None)
        
        finale = cur.execute("SELECT course_id FROM courses where course_name = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
        cur.execute("INSERT into bookings(user_id,course_id) VALUES(%s,%s)",(userid,pidd))
        mysql.connection.commit()
        return redirect("/mybookings")
    return render_template('ctable.html',catDetails=catDetails,courseDetails = courseDetails,table_name="Programming")

@app.route('/Music', methods = ['GET','POST'])
def Music():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    courseValue = cur.execute("SELECT * FROM courses where cat_id = 1112")
    if courseValue > 0:
        courseDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # course name
        course_name = request.form.get("name",None)
        
        finale = cur.execute("SELECT course_id FROM courses where course_name = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
        cur.execute("INSERT into bookings(user_id,course_id) VALUES(%s,%s)",(userid,pidd))
        mysql.connection.commit()
        return redirect("/mybookings")
    return render_template('ctable.html',catDetails=catDetails,courseDetails = courseDetails,table_name="Music")

@app.route('/Design', methods = ['GET','POST'])
def Design():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    courseValue = cur.execute("SELECT * FROM courses where cat_id = 1113")
    if courseValue > 0:
        courseDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # course name
        course_name = request.form.get("name",None)
        
        finale = cur.execute("SELECT course_id FROM courses where course_name = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
        cur.execute("INSERT into bookings(user_id,course_id) VALUES(%s,%s)",(userid,pidd))
        mysql.connection.commit()
        return redirect("/mybookings")
    return render_template('ctable.html',catDetails=catDetails,courseDetails = courseDetails,table_name="Design")

@app.route('/Technology', methods = ['GET','POST'])
def Technology():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    courseValue = cur.execute("SELECT * FROM courses where cat_id = 1114")
    if courseValue > 0:
        courseDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # course name
        course_name = request.form.get("name",None)
        
        finale = cur.execute("SELECT course_id FROM courses where course_name = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
        cur.execute("INSERT into bookings(user_id,course_id) VALUES(%s,%s)",(userid,pidd))
        mysql.connection.commit()
        return redirect("/mybookings")
    return render_template('ctable.html',catDetails=catDetails,courseDetails = courseDetails,table_name="Technology")

@app.route('/Photography', methods = ['GET','POST'])
def Photography():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    courseValue = cur.execute("SELECT * FROM courses where cat_id = 1115")
    if courseValue > 0:
        courseDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # course name
        course_name = request.form.get("name",None)
        
        finale = cur.execute("SELECT course_id FROM courses where course_name = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
        cur.execute("INSERT into bookings(user_id,course_id) VALUES(%s,%s)",(userid,pidd))
        mysql.connection.commit()
        return redirect("/mybookings")
    return render_template('ctable.html',catDetails=catDetails,courseDetails = courseDetails,table_name="Photography")

@app.route('/Robotics', methods = ['GET','POST'])
def Robotics():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    courseValue = cur.execute("SELECT * FROM courses where cat_id = 1116")
    if courseValue > 0:
        courseDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # course name
        course_name = request.form.get("name",None)
        
        finale = cur.execute("SELECT course_id FROM courses where course_name = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
        cur.execute("INSERT into bookings(user_id,course_id) VALUES(%s,%s)",(userid,pidd))
        mysql.connection.commit()
        return redirect("/mybookings")
    return render_template('ctable.html',catDetails=catDetails,courseDetails = courseDetails,table_name="Robotics")

@app.route('/AppDevolpment', methods = ['GET','POST'])
def AppDevolpment():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    courseValue = cur.execute("SELECT * FROM courses where cat_id = 1117")
    if courseValue > 0:
        courseDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # course name
        course_name = request.form.get("name",None)
        
        finale = cur.execute("SELECT course_id FROM courses where course_name = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
        cur.execute("INSERT into bookings(user_id,course_id) VALUES(%s,%s)",(userid,pidd))
        mysql.connection.commit()
        return redirect("/mybookings")
    return render_template('ctable.html',catDetails=catDetails,courseDetails = courseDetails,table_name="AppDevolpment")

@app.route('/WebDevolopment', methods = ['GET','POST'])
def WebDevolopment():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    courseValue = cur.execute("SELECT * FROM courses where cat_id = 1118")
    if courseValue > 0:
        courseDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # course name
        course_name = request.form.get("name",None)
        
        finale = cur.execute("SELECT course_id FROM courses where course_name = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
        cur.execute("INSERT into bookings(user_id,course_id) VALUES(%s,%s)",(userid,pidd))
        mysql.connection.commit()
        return redirect("/mybookings")
    return render_template('ctable.html',catDetails=catDetails,courseDetails = courseDetails,table_name="WebDevolopment")


@app.route('/admin', methods = ['GET','POST'])
def tables():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    courseValue = cur.execute("SELECT name,email,course_name from users, pending, courses where courses.course_id=pending.course_id and users.user_id = pending.user_id;")
    if courseValue > 0:
        pendDetails = cur.fetchall()

    cur.execute("SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin)")
    name1=cur.fetchone()
    for i in name1:
        userid = i

    if request.method == 'POST':
        #add entry
        global course_name
        # pending user email
        course_name = request.form.get("name",None)
        print(course_name)
        finale = cur.execute("SELECT user_id FROM users where email = %s",[course_name])
        pid = cur.fetchone()
        for i in pid:
            pidd = i
            print(pidd)
        cur.execute("INSERT into instructors(user_id) VALUES(%s)",[pidd])
        cur.execute("DELETE FROM pending where user_id = %s",[pidd])
        mysql.connection.commit()
        return redirect("/admin")
    return render_template('tables.html',catDetails=catDetails,pendDetails=pendDetails)



@app.route('/signin', methods = ['GET','POST'])
def signin():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    if(request.method == 'POST'):
        userDetails = request.form
        email = userDetails['email']
        password = userDetails['password']
        # cur = mysql.connection.cursor()
        
        cur.execute("SELECT email from users")
        emails = cur.fetchall()
        size = len(emails)

        if len(email) == 0:
            return render_template('invalid.html',error_msg = 'No Email',error_msg2 = 'You cannot leave email blank!')
            # return "NO EMAIL"
        if len(password) == 0:
            return render_template('invalid.html',error_msg = 'No Password',error_msg2 = 'You did not enter your password!')
            # return "NO PASSWORD"

        email_flag = 0
        pass_flag = 0
        
        count = 0
        cur.execute("SELECT email,password,user_id from users")
        # {('1','2','3'),('1','2','3'),...('1','2','3')}
        sum = cur.fetchone()
        # ('1','2','3')
        # 0 to n range n 
        for i in range(size):
            for j in sum:
                temp = j
                if email == temp:
                    email_flag = 1
                if password == temp:
                    pass_flag = 1
                if pass_flag == 1 and email_flag == 1:
                    if count == 0 :
                        count=1
                        # print(count)
                        cur.execute("SELECT user_id FROM users where email = %s",[email])
                        busid = cur.fetchone()
                        for k in busid:
                            userid = k
                            # print(count)
                            # userid = temp
                        cur.execute("SELECT email,password,user_id from users")
                    users = temp    
                    # print(userid)
            sum = cur.fetchone()

        if email_flag == 1 and pass_flag == 1:
            cur.execute("SELECT user_id from admin")
            sum = cur.fetchone()
            # for i in range(size):
            for j in sum:
                temp = j
                # print(j)
            sum = cur.fetchone()
            # print(userid)
            if temp == userid:
                cur.execute("INSERT INTO signin(user_id,email) VALUES (%s,%s)",(userid,email))
                mysql.connection.commit()
                cur.execute("SELECT name FROM users WHERE email = (SELECT email FROM signin where time = (SELECT max(time) from signin))")
                name1=cur.fetchone()
                for i in name1:
                    disp_name = i
                cur.close()
                return render_template('tables.html',welcome = 'Welcome',user = disp_name,exc = '!')


            cur.execute("INSERT INTO signin(user_id,email) VALUES (%s,%s)",(userid,email))
            cur.execute("SELECT name FROM users WHERE email = (SELECT email FROM signin where time = (SELECT max(time) from signin))")
            name1=cur.fetchone()
            for i in name1:
                disp_name = i
            mysql.connection.commit()
            cur.close()
            return render_template('index.html',welcome = 'Welcome',catDetails=catDetails,user = disp_name,exc = '!')
        
        if email_flag == 0:
            return render_template('invalid.html',catDetails=catDetails,error_msg = 'Incorrect_Email',error_msg2 = 'Oops! Please check your Email!')
        
        if pass_flag == 0:
            return render_template('invalid.html',catDetails=catDetails,error_msg = 'Incorrect_Password',error_msg2 = 'Oops! Please check your Password!')
    return render_template('login.html',catDetails=catDetails)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    if(request.method == 'POST'):
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        password = userDetails['password']

        if len(name) == 0:
            return render_template('invalid.html',catDetails=catDetails,error_msg = 'No Name' ,error_msg2 = 'Name cannot be empty')
        if len(email) == 0:
            return render_template('invalid.html',error_msg = 'No Email',catDetails=catDetails,error_msg2 = 'Email cannot be empty')
            return "NO EMAIL"
        if len(password) == 0:
            return render_template('invalid.html',error_msg = 'No Password',catDetails=catDetails, error_msg2 = 'Password Cannot be empty')
            return "NO PASSWORD"

        cur = mysql.connection.cursor()
        cur.execute("SELECT MAX(user_id) from users")
        id = cur.fetchone()
        for i in id:
            user_id = i
        user_id = user_id + 1
        user_login = 1
        signup_login = user_login
        cur.execute("INSERT INTO users(user_id,name,email,password) VALUES(%s,%s,%s, %s)",(user_id,name,email,password))
        cur.execute("INSERT INTO signin(user_id,email)  VALUES(%s, %s)",(user_id,email))
        cur.execute("SELECT name FROM users WHERE email = (SELECT email FROM signin where time = (SELECT max(time) from signin))")
        name2=cur.fetchone()
        for i in name2:
            display_name = i
        mysql.connection.commit()
        cur.close()
        return render_template('index.html',catDetails=catDetails,welcome = 'Welcome',user = display_name,exc = '!')
    return render_template('signup.html',catDetails=catDetails)

@app.route('/mybookings')
def bookings():
    cur = mysql.connection.cursor()
    instValue = cur.execute("SELECT * FROM catagories")
    if instValue > 0:
        catDetails = cur.fetchall()
    # cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT course_name, fee from courses, bookings, users where users.user_id = bookings.user_id and courses.course_id = bookings.course_id and users.user_id in (SELECT user_id FROM signin WHERE time = (SELECT max(time) FROM signin));")
    if resultValue > 0:
        courseDetails = cur.fetchall()
        return render_template('bookings.html',catDetails=catDetails,courseDetails = courseDetails )
    return render_template('bookings.html',catDetails=catDetails)

if __name__ == "__main__":
    app.run(debug=True)
