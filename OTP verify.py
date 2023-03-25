import random
import smtplib

# generate OTP
otp = random.randint(1000, 9999)

# email information
sender_email = 'rameshkurnool777@gmail.com'
sender_password = 'ypchhblcskypzgam'
receiver_email = 'rameshkurnool20@gmail.com'
message = f'Your OTP is {otp}'

# SMTP server information
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# connect to SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

# send email with OTP
server.sendmail(sender_email, receiver_email, message)
print('OTP sent successfully')

# prompt user to enter OTP
user_otp = input('Enter the OTP sent to your email: ')

# verify OTP
if int(user_otp) == otp:
    print('OTP verified successfully')
else:
    print('OTP verification failed')
