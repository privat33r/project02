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
