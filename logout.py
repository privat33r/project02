#!/usr/bin/env python3

#Created: 12Apr19
#Author:

#Description: Makes cookie expire, clears session, and directs user to login page.

import cgi                #after succesful login, call Shield's function to redirect to message board
import cgitb
import sys
import mysql.connector
from mysql.connector import errorcode
import config
import hashlib, time, os, shelve
from http import cookies
from helper import *

cookie = cookies.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')

isSession = False

if string_cookie:
  cookie.load(string_cookie)
  if 'sid' in cookie:
    sid = cookie['sid'].value
    isSession = True

cookie['sid'] = ''
cookie['sid']['expires'] = -1

if isSession:
  sessionFile = '/tmp/sess_' + sid
  session = shelve.open(sessionFile, writeback=True)

  #clear session data
  session.clear()
  #remove session file
  session.close()
  os.remove(sessionFile)

print(cookie)
page = open("login.html")
print("Content-Type: text/html")
print()
pageParts = page.read().split("<span id='error'></span>")
print(pageParts[0])
print("Successfully Logged Out.<br><br>")
print(pageParts[1])
