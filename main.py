from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS
import json
mysql = MySQL()
app = Flask(__name__)
CORS(app)
# My SQL Instance configurations
# Change these details to match your instance configurations
# Needs this to run
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'HelloWorld'
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_HOST'] = '35.197.236.234'
mysql.init_app(app)

cur = mysql.connection.cursor() #create a connection to the SQL instance

def insert(name,email):
  s = f"INSERT INTO student(studentName, email) VALUES('{name}','{email}'"
  try:
    cur.execute(s)
    mysql.connection.commit()
    return '{"Result":"Success"}' # Really? maybe we should check!
  except:
    return ('{"Result":"Failure"}')

def read():
  cur.execute('''SELECT * FROM students''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['Name']=row[0].replace('\n',' ')
    Result['Email']=row[1]
    Result['ID']=row[2]
    Results.append(Result)
  return Results

@app.route("/add") #Add Student
def add():
  name = request.args.get('name')
  email = request.args.get('email')
  
  insert(name,email)
  

  

@app.route("/hello") #Add Student
def hello():
  return '{"Server":"Running"}'
  
@app.route("/") #Default - Show Data
def read_all(): # Name of the method
  
  Results = read()
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format
if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080

