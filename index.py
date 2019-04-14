#!/usr/bin/env python3

#Created: 12Apr19
#Author: Ben Valdes, Brandon Shield, Yixin Ye

#Description: Backbone of the entire website, serves as the landing page for returning and new users.
#New users will be directed to login/signup page.
#Returning users will be checked for existing cookies and if they are legitimate.
#Handles login POST from login page.
#Dynamically pulls messages from the MySQL database to generate message board, showing the most recent message first.
#Allows admins to delete any message and allows users to delete own messages.

import cgi                #after succesful login, call Shield's function to redirect to message board
import cgitb
import re, sys
import mysql.connector
from mysql.connector import errorcode
import config
import hashlib, time, os, shelve
from http import cookies
from helper import *

#Author: Ben valdes
#connect to m207026 sql database
conn = mysql.connector.connect(user=config.USER, password = config.PASSWORD, host = config.HOST, database=config.DATABASE)
cursor = conn.cursor()

#Author: Yixin Ye
# Checks for cookie
cookie = cookies.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')

isSession = False
isAdmin = False
sid = 0

if not string_cookie:
  cgitb.enable()
  form = cgi.FieldStorage()

  #get values from index.py
  user = Input(form.getvalue('user'))
  password = Input(form.getvalue('pass'))
  submit = Input(form.getvalue('src')) # Hidden field that weakly associates request with a browser input

  # uses getHash from helper.py to obtain hash
  pwHash = getHash(user.content,password.content)

  #once user presses log in button
  if submit.content=="browser":
    query = "SELECT * FROM USERS;" #get rows from USERS
    cursor.execute(query)

    for row in cursor:
      if row[1] == user.content:
        if pwHash == row[2]:
          # Hashing the password hash with some predetermined value so we don't store the actual hash in the cookie
          sid = getHash(row[2],str(7 * 24 * 60 * 60)) + user.content
          cookie['sid'] = sid
          cookie['sid']['expires'] = 7 * 24 * 60 * 60 #set cookie to expire in 10 days
          isSession = True
          uid = row[0]
          if row[3] == 1: #checks to see if user is admin, sets isAdmin to true if yes
            isAdmin = True

else:
  cookie.load(string_cookie)

  if 'sid' in cookie:
    user = cookie['sid'].value[64:]
    sneakyHash = cookie['sid'].value[:64]

    query = "SELECT * FROM USERS;" #get rows from USERS
    cursor.execute(query)

    for row in cursor:
      if row[1] == user:
        #Checks if the cookie is valid
        sid = getHash(row[2],str(7 * 24 * 60 * 60))
        if sneakyHash == sid:
          isSession = True
          uid = row[0]
          cookie['sid']['expires'] = 7 * 24 * 60 * 60 #Renews the cookie
          if row[3] == 1:
            isAdmin = True

if isSession:

  #Start collecting inputs
  cgitb.enable()
  form = cgi.FieldStorage()

  uidPost = Input(form.getvalue('uidPost'))
  message = Input(form.getvalue('msg'))

  if uidPost.content != "None": #This means that we have received a request to post a message
    if message.content == "None":
      message.content = "<empty message>"
    query = "INSERT INTO MESSAGES (UserID,Message,Timestamp) VALUES (%s,%s,FROM_UNIXTIME(%s));"
    cursor.execute(query,(uidPost.content,message.html(),time.time()))


  delPost = Input(form.getvalue('del'))
  delMsgID = Input(form.getvalue('msgID'))
  uidDel = Input(form.getvalue('uidDel'))

  if delPost.content != "None": #This means that we have received a request to delete a message
    if (int(uidDel.content) == uid) or isAdmin:
      query = "delete from MESSAGES where MessageID = %s;"
      cursor.execute(query,(delMsgID.content,))

  #Sets cookies
  print(cookie)

  #prints out the first part of the website using helper function Start()
  Start("Message Board")

  #Allows persistence of cookie
  session_file = '/tmp/sess_' + sid
  session = shelve.open(session_file, writeback=True)

  if not isAdmin:

    #Author: Brandon Shields
    #Pull messages from MESSAGES table
    #Editor: Yixin Ye
    #Included functionality that tracks if message correspond to user ID.
    print("<br><table style='border: 1px;'><tr> <th style='width: 70px;'>User</th> <th>Message</th> <th style='width: 150px;'>Timestamp</th> <th style='width: 50px;'>Delete</th></tr>")
    cursor.execute("SELECT * FROM MESSAGES LEFT JOIN USERS ON MESSAGES.UserID=USERS.UserID ORDER BY Timestamp DESC;") # stores result from the query
    for row in cursor:
      print('<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>'.format(row[5],row[2],row[3]))
      if row[1] == uid: #Checks if UID between current user and message matches, gives option to delete if they match.
        print("""<form method="post" action="index.py">
        <input type="hidden" name="del" value="1">
        <input type="hidden" name="msgID" value=\"""",end="")
        print(row[0],end="")

        print("""\">

        <input type="hidden" name="uidDel" value=\"""",end="")
        print(uid,end="") #This will identify the user when deleting the message
        print("""\">

        <input type="submit" value="[d]" style="display: block; margin: auto;"></form>
        """)
      print("""</td></tr>""")
    print("</table>")

  else:

    print("<br><table style='border: 1px;'><tr> <th style='width: 70px;'>User</th> <th>Message</th> <th style='width: 150px;'>Timestamp</th> <th style='width: 50px;'>Delete</th></tr>")
    cursor.execute("SELECT * FROM MESSAGES LEFT JOIN USERS ON MESSAGES.UserID=USERS.UserID ORDER BY Timestamp DESC;") # stores result from the query
    for row in cursor:
      print("""<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>
      <form method="post" action="index.py">
      <input type="hidden" name="del" value="1">
      <input type="hidden" name="msgID" value=\"""".format(row[5],row[2],row[3]),end="")
      print(row[0],end="")
      print("""\">

      <input type="hidden" name="uidDel" value=\"""",end="")
      print(uid,end="") #This will identify the user when posting messages
      print("""\">

      <input type="submit" value="[d]" style="display: block; margin: auto;"></form>
      </td></tr>
      """)
    print("</table>")

  print("""<br>
  <form method="post" action="index.py">
    <textarea rows="3" cols="80" name="msg" placeholder="Write your message here"></textarea><br>
    <input type="hidden" name="uidPost" value=\"""",end="")
  print(uid,end="") #This will identify the user when posting messages
  print("""\">
    <input type="submit" value="Submit">
  </form><br><br>
  <a href="logout.py"><button>Log Out</button></a>
  """,end="")

  End()
  conn.commit()
  conn.close()

#if not in session/failed login attempt
else:
  page = open("login.html")
  print("Content-Type: text/html")
  print()
  pageParts = page.read().split("<span id='error'></span>")
  print(pageParts[0])
  if submit.content=="browser":
    print("Invalid Username and Password combination.<br><br>")
  print(pageParts[1])
