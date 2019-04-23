#!/usr/bin/env python3

#Created: 22Apr19
#Author: Yixin Ye

#Description: Admin panel that uses HTTP digest authentication
#admin will be able to delete non-admin user accounts here.

import cgi
import cgitb
import re, sys
import mysql.connector
from mysql.connector import errorcode
import config
import hashlib, time, os, shelve
from http import cookies
from helper import *

request = os.environ.get('REQUEST_METHOD')

cgitb.enable()
form = cgi.FieldStorage()

#connect to m207026 sql database
conn = mysql.connector.connect(user=config.USER, password = config.PASSWORD, host = config.HOST, database=config.DATABASE)
cursor = conn.cursor()

#checks for user deletion requests, only handles it if POST method is used
if request == "POST":
  delUser = Input(form.getvalue('delUser'))
  uid = Input(form.getvalue('uid'))

  if uid.content != "None": #This means that we have received a request to delete a user
    query = "delete from USERS where UserID = %s;"
    cursor.execute(query,(uid.content,))

Start("Admin Panel")

cursor.execute("select UserID, Username, Admin from USERS;")

print("<br><table style='border: 1px;'><tr> <th style='width: 70px;'>UserID</th> <th>User</th> <th style='width: 150px;'>Admin</th> <th style='width: 50px;'>Delete</th></tr>")

for row in cursor:
  print('<tr><td style="text-align: center;">{0}</td><td>{1}</td><td style="text-align: center;">{2}</td><td>'.format(row[0],row[1],row[2]))
  if row[2] != 1:
    print("""<form method="post" action="index.py">
    <input type="hidden" name="delUser" value="1">
    <input type="hidden" name="uid" value="{0}">
    """.format(row[0]))
    print('<input type="submit" value="[d]" style="display: block; margin: auto;"></form>')
  print('</td></tr>')

print("</table><br><a href='http://midn.cs.usna.edu/~m207026/project02/'>Home</a>")

End()
conn.commit()
conn.close()
