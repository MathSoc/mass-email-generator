import csv

fileName = "aprilEmail.csv"
opening_title = "Congrats on finishing another (or your last!!) term!"
opening_line = "It's your last email from the MathSoc W22 team. This email contain a few volunteer opportunities (and some paid opportunities!) with deadlines coming up soon.  <hr>"
end_line = "That's it from us today. Hope you have a wonderful rest of your day.\n <h3 style=\"color:#COLOUR\"> The MathSoc Execs </h3>"
pink = "C60078"


with open(fileName) as f:
    email = """
    <center><table class="container600" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:calc(100%);max-width:calc(600px);margin: 0 auto;">
            <tr>
                <td width="100%" style="text-align: left;"> <h1 style=\"color:#COLOUR\">{} </h2> {}
    """.format(opening_title, opening_line)
    data = csv.reader(f, delimiter=",")
    next(data)
    for row in data:
        email_segment = """
        <h2 style=\"color:#COLOUR\">{} </h2>
        <p>{}</p>
        <table  border="0" cellpadding="0" cellspacing="0" style="margin-left:auto; margin-right:auto; background-color:#COLOUR; border:1px solid #COLOUR; border-radius:5px;">
  <tr>
    <td align="center" valign="middle" style="color:#FFFFFF; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; letter-spacing:-.5px; line-height:150%; padding-top:15px; padding-right:30px; padding-bottom:15px; padding-left:30px;">
      <a href="{}" target="_blank" style="color:#FFFFFF; text-decoration:none;">{}</a>
    </td>
  </tr>
</table>
<hr>
        """.format(row[2], row[3], row[5],  row[4])
        email = email + email_segment
    email = email + end_line
    email = email + " </tr></table></center"
    email = email.replace("COLOUR", pink)
    print(email)
        
