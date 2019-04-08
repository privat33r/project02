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

from inputClass import Input #

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
  <h1 style="margin-top: 100px; text-align: center; color: #ffffff;">All aBoard Message Board</h1>

  <div class="box">
  <h2 style="text-align: center;">Registration Successful!</h2>
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
  print("Fix your code or Contact the system admin<br></div></body></html>")
  sys.exit(1)

form = cgi.FieldStorage()

user = Input(form.getvalue('user'))
password = Input(form.getvalue('pass'))
password2 = Input(form.getvalue('pass2'))

print("Your account <i>{0}</i> has been successfully registered!".format(user))

print("""
  </div>

  <!-- ***************************************************************
     Below this point is text you should include on every SY306 page
     *************************************************************** -->
  <!-- Below are scripts which create a button you can click on to validate your page.
       The background will load green or red if the HTML is valid or not.
       The time at which the page was last modified will also be displayed below the button -->
<link href="http://courses.cyber.usna.edu/SY306/docs/check.css" rel="stylesheet">

  <script>
    document.write('<div id="response"><a href="http://csmidn.academy.usna.edu:8888/?showsource=yes&doc=' + document.location + '">' +
               '<img src="http://courses.cyber.usna.edu/SY306/docs/check.py"' + 'alt="HTML Check" height="60" />' +
               '</a><div id="time"></div></div>');
  </script>
  <script src="http://courses.cyber.usna.edu/SY306/docs/time.js" ></script>

</body>
</html>
""")
