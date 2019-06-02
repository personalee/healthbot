from flask import Flask, render_template, request,jsonify
import sqlite3


status = False

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"


@app.route('/')
@app.route('/Login', methods=['POST', 'GET'])
def login():
    return render_template('index.html')


@app.route('/getcredentials', methods=['POST', 'GET'])
def auth():
    global status
    username = request.form['username']
    password = request.form['password']

    con = sqlite3.connect('chatbt.db')
    c = con.cursor()

    users = c.execute('select * from users')
    for u,p in users:
        # print(j, k)
        if (u == username and p == password):
            print('hi')
            status = True
            break
        else:
            status = False
            pass
    con.commit()

    print('\n\n', username, password, '\n\n')
    return render_template('index.html')


@app.route('/newuser', methods=['POST', 'GET'])
def createuser():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    dob = request.form['age']

    
    
    con = sqlite3.connect('chatbt.db')
    c = con.cursor()
    c.execute("INSERT INTO userdetails VALUES('%s','%s','%s','%s');" %(username,password,email,dob))
    c.execute("INSERT INTO users VALUES('%s','%s');" %(username,password))
    con.commit()

    print("\n\n\nlist", username, password, email, dob, '\n\n\n\n')
    return render_template('signup.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    global status
    status = False
    return render_template('signup.html')


@app.route('/application', methods=['POST', 'GET'])
def application():

    if status == True:
        con = sqlite3.connect('chatbt.db')
        c = con.cursor()

        doctors = list(c.execute('select * from doctors'))
        remainders = list(c.execute('select * from remainders'))
        con.commit()
        data = {
            'doctors':doctors,
            'remainders':remainders
        }
        return render_template('app.html', data = data)   # pass value to the app
    else:
        return '<h1>You are not logged in </h1> <br> <small>login to continue</small>'

@app.route('/remainders',methods = ['POST','GET'])
def remainders():
    dateselect = request.form['dateselect']
    timeselect = request.form['timeselect']

    con = sqlite3.connect('chatbt.db')
    c = con.cursor()
    c.execute("INSERT INTO remainders VALUES('%s','%s');" %(timeselect,dateselect))
    doctors = list(c.execute('select * from doctors'))
    remainders = list(c.execute('select * from remainders'))
    con.commit()
    data = {
        'doctors':doctors,
        'remainders':remainders
    }
    return render_template('app.html', data = data)   # pass value to the app

if __name__ == "__main__":
    app.run(debug=True)
