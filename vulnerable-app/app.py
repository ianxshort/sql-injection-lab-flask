from flask import Flask, render_template, request,g 
import sqlite3

app = Flask(__name__)
DATABASE='users.db'

def get_db():
    if "db" not in g :
        g.db=sqlite3.connect(DATABASE) #open a connection so I can run queries 
    return g.db

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    #Get credentials for log in form 
    #build a SQL query that shows entries that match the user's credentials 
    db=get_db()  #fetching the database connection
    c=db.cursor() #assigning a cursor to the database connection 

    query=f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    c.execute(query) #execute query 

    result=c.fetchone()

    if result:
        return render_template('success.html')

    else: 
        return render_template('login.html', error="Invalid username or password")









if __name__ == '__main__':
    app.run(debug=True)