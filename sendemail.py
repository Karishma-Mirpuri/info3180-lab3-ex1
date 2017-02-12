import smtplib

from_name = 'Karishma Gmail'
from_addr = 'username@gmail.com'
to_name = 'Karishma Yahoo'
to_addr = 'username@yahoo.com'
subject = 'INFO3180 Lab 3 Ex1'
msg = 'This exercise demonstrates an email sending script.'
message =  """From: Karishma Gmail <username@gmail.com>
To: Karishma Yahoo <username@yahoo.com> 
Subject: INFO3180 Lab 3 Ex1

This exercise demonstrates an email sending script.
"""
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)

# Credentials
username = 'yourusername@gmail.com'
password = 'youremailappassword'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()
