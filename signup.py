#!/usr/bin/python3

#Created:29Mar19 Author:
#Description: Handles signup actions from signup.html, perform input validation and updates database

import mysql.connector #library for database being used
from mysql.connector import errorcode #  allows you to check and handle errors
import config
import sys
import re
import cgi
import cgitb; cgitb.enable()
from helper import End # neat way of ending the page
import hashlib

from inputClass import Input #this is to escape characters when dealing with user inputs

print("Content-Type: text/html")
print()
print("<!DOCTYPE html>")
print("""
<html lang="en">
<head>
  <title>All aBoard Message Board</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1 style="margin-top: 100px; text-align: center; color: #ffffff;" onclick="window.location.href='index.html';">All aBoard Message Board</h1>

  <div class="box">
  """)

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
hash256 = hashlib.sha256()
prepared = password.content + user.content
hash256.update(prepared.encode())
pwHash = hash256.hexdigest()

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

print("Your account <i>{0}</i> has been successfully registered!".format(user.html()))


End()
