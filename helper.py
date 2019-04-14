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
    <link rel="stylesheet" href="styles.css">
    <link rel="shortcut icon" href="bubble.ico"/>
  </head>
  <body>
    <h1 style="margin-top: 100px; text-align: center; color: #ffffff;" onclick="window.location.href='index.py';">All aBoard Message Board</h1>

    <div class="box">
    """)

#Automatically prints out the final part of the website.
def End():
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

#Takes two string inputs and concatenates them based on pre-determined manner.
def getHash(un,pw):
  hash256 = hashlib.sha256()
  prepared = str(pw) + str(un)
  hash256.update(prepared.encode())
  pwHash = hash256.hexdigest()
  return pwHash
