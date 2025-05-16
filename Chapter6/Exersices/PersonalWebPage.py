#  11. Personal Web Page Generator
#  Write a program that asks the user for his or her name, then asks the user to enter a sen
# tence that describes himself or herself. Here is an example of the program’s screen:
#  Enter your name: Julie Taylor Enter
#  Describe yourself: I am a computer science major, a member of the 
# Jazz club, and I hope to work as a mobile app developer after I 
# graduate. Enter
#  Once the user has entered the requested input, the program should create an HTML file, 
# containing the input, for a simple Web page. Here is an example of the HTML content, 
# using the sample input previously shown:
#  <html>
#  <head>
#  </head>
#  <body>
#    <center>
#       <h1>Julie Taylor</h1>
#    </center>
#    <hr />
#    I am a computer science major, a member of the Jazz club,
#    and I hope to work as a mobile app developer after I graduate.
#    <hr />
#  </body>
#  </html>





name = input("Enter your name: ")
about = input("Enter something about you: ")
with open("Chapter6/personal_page.html", "w", encoding="utf-8") as output_file:
        output_file.write(
            "<html>\n"
            "<head>\n"
            "</head>\n"
            "<body>\n"
            "  <center>\n"
            f"    <h1>{name}</h1>\n"
            "  </center>\n"
            "  <hr />\n"
            f"  {about}\n"
            "  <hr />\n"
            "</body>\n"
            "</html>\n"
        )






