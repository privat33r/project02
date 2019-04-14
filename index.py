#!/usr/bin/env python3
import cgi                #after succesful login, call Shield's function to redirect to message board
import cgitb
import re, sys
import mysql.connector
from mysql.connector import errorcode
import config
import hashlib, time, os, shelve
from http import cookies
from helper import *

#connect to m207026 sql database
conn = mysql.connector.connect(user=config.USER, password = config.PASSWORD, host = config.HOST, database=config.DATABASE)
cursor = conn.cursor()

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
          cookie['sid']['expires'] = 7 * 24 * 60 * 60
          isSession = True
          uid = row[0]
          if row[3] == "1":
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
          if row[3] == "1":
            isAdmin = True
    isSession = True

if isSession:

  cgitb.enable()
  form = cgi.FieldStorage()

  uidPost = Input(form.getvalue('uid'))
  message = Input(form.getvalue('msg'))

  if uidPost.content != "None":
    if message.content == "None":
      message.content = "<empty message>"
    query = "INSERT INTO MESSAGES (UserID,Message) VALUES (%s,%s);"
    cursor.execute(query,(uidPost.content,message.html()))

  print(cookie)

  Start("Message Board")

  session_file = '/tmp/sess_' + sid
  session = shelve.open(session_file, writeback=True)

  print("<table style='border: 1px;'><tr><th>User</th><th>Message</th></tr>")
  cursor.execute("SELECT * FROM MESSAGES LEFT JOIN USERS ON MESSAGES.UserID=USERS.UserID;") # stores result from the query
  for row in cursor:
    print('<tr><td>{0}</td><td>{1}</td></tr>'.format(row[4],row[2]))
  print("</table>")

  print("""<br>
  <form method="post" action="index.py">
    <textarea rows="3" cols="40" name="msg" placeholder="Write your message here"></textarea><br>
    <input type="hidden" name="uid" value=\"""",end="")
  print(uid,end="") #This will identify the user when posting messages
  print("""\">
    <input type="submit" value="Submit">
  </form>
  """,end="")

  End()
  conn.commit()
  conn.close()

else:
  page = open("login.html")
  print("Content-Type: text/html")
  print()
  pageParts = page.read().split("<span id='error'></span>")
  print(pageParts[0])
  print("Invalid Username and Password combination/Cookie<br><br>")
  print(pageParts[1])
