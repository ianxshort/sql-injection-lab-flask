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

if __name__ == '__main__':
    app.run(debug=True)