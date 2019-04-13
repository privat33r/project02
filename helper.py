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
