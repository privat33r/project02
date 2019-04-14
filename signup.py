#!/usr/bin/python3

#Created:29Mar19 Author: Yixin Ye
#Description: Handles signup actions from signup.html, perform input validation and updates database

import mysql.connector #library for database being used
from mysql.connector import errorcode #  allows you to check and handle errors
import config
import sys
import re
import cgi
import cgitb; cgitb.enable()
from helper import * # helper scripts
import hashlib

from inputClass import Input #this is to escape characters when dealing with user inputs

# Start() from helper scripts print
Start("Registration")

try:
  conn = mysql.connector.connect(user=config.USER, password=config.PASSWORD, host=config.HOST, database=config.DATABASE)
  cursor = conn.cursor() #declares cursor to iterate through database

#check for errors
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password<br>")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist<br>")
  else:
    print(err)
  print("Fix your code or contact the system admin.<br>")
  End()
  sys.exit(1)

form = cgi.FieldStorage()

user = Input(form.getvalue('user'))
password = Input(form.getvalue('pass'))
password2 = Input(form.getvalue('pass2'))

if len(user.content) < 4: #checks if passwords match
  print("""<h2 style="text-align: center;">Registration Failed</h2>""")
  print("Username needs to be at least 4 characters.<br><br>")
  print('<button onclick="window.history.back();">Go Back</button>')
  End()
  sys.exit(0)

# Checks if username is already taken
cursor.execute("SELECT * FROM USERS")

for row in cursor:
  # print("{0}".format(row[1]))
  if user.content == row[1]:
    print("""<h2 style="text-align: center;">Registration Failed</h2>""")
    print("Username already taken! Please try another username.<br><br>")
    print('<button onclick="window.history.back();">Go Back</button>')
    End()
    sys.exit(0)

# Checks if passwords match
if password.content != password2.content: #checks if passwords match
  print("""<h2 style="text-align: center;">Registration Failed</h2>""")
  print("Passwords do not match! Registration failed.<br><br>")
  print('<button onclick="window.history.back();">Go Back</button>')
  End()
  sys.exit(0)

# Checks if password has number and meets minimum length
pwTest = re.search(r"\d",password.content)
if pwTest == None:
  print("""<h2 style="text-align: center;">Registration Failed</h2>""")
  print("Password needs at least one number! Registration failed.<br><br>")
  print('<button onclick="window.history.back();">Go Back</button>')
  End()
  sys.exit(0)

if len(password.content) < 6:
  print("""<h2 style="text-align: center;">Registration Failed</h2>""")
  print("Password needs to be at least 6 characters long! Registration failed.<br><br>")
  print('<button onclick="window.history.back();">Go Back</button>')
  End()
  sys.exit(0)

# Passed all checks, preparing query
query = "INSERT INTO USERS (Username,Password,Admin) VALUES (%s,%s,0);"

# Calls getHash from helper.py
pwHash = getHash(user.content,password.content)

try:
  cursor.execute(query,(user.content,pwHash))
  cursor.close()
  conn.commit()
  conn.close()
except mysql.connector.Error as err:
  #for DEBUG only we'll print the error and statement- we should print some generic message instead of production site
  print ('<p style = "color:red">')
  print(err)
  print (" for statement" + cursor.statement )
  print ('</p>')

print("""<h2 style="text-align: center;">Registration Successful</h2>""")
print("Your account <i>{0}</i> has been successfully registered!<br><br>".format(user.html()))
print('<button onclick="window.location.href=\'index.py\';">Home</button>')


End()
