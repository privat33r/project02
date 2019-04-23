import hashlib


#Defines input class to help escape problematic characters
class Input:
  def __init__(self,str_in):
    if str_in == None: #In case no input given
      str_in = "None"
    self.content = str_in
    return

  #In case the class was used as string
  def __str__(self):
    return self.content

  #Returns a string that is HTML-friendly
  def html(self):
    str_in = self.content
    if str_in != None:
      str_in = str_in.replace("&","&amp;")
      str_in = str_in.replace("<","&lt;")
      str_in = str_in.replace(">","&gt;")
      str_in = str_in.replace('"',"&quot;")
    return str_in

#Automatically prints out the first part of the website, taking a customizable title.
def Start(title):
  print("Content-Type: text/html")
  print()
  print("<!DOCTYPE html>")
  print("""
  <html lang="en">
  <head>
    <title>All aBoard Message Board - """+title+"""</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="http://midn.cs.usna.edu/~m207026/project02/styles.css">
    <link rel="shortcut icon" href="http://midn.cs.usna.edu/~m207026/project02/bubble.ico"/>
  </head>
  <body>
    <h1 style="margin-top: 100px; text-align: center; color: #ffffff;" onclick="window.location.href='http://midn.cs.usna.edu/~m207026/project02/index.py';">All aBoard Message Board</h1>

    <div class="box">
    """)

#Automatically prints out the final part of the website.
def End():
  print("""
    </div>

  </body>
  </html>
  """)

#Takes two string inputs and concatenates them based on pre-determined manner.
def getHash(un,pw):
  hash256 = hashlib.sha256()
  prepared = str(pw) + str(un)
  hash256.update(prepared.encode())
  pwHash = hash256.hexdigest()
  return pwHash

def failOut():
  page = open("login.html")
  print("Content-Type: text/html")
  print()
  pageParts = page.read().split("<span id='error'></span>")
  print(pageParts[0])
  try:
    if submit.content=="browser":
      print("Invalid Username and Password combination.<br><br>")
  except: # submit.content may not exist
    pass
  print(pageParts[1])
