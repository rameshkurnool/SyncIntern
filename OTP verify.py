import random

otp = random.randint(100000, 999999)
print("Your OTP is:", otp)

# Storing the OTP in a variable
otp_input = input("Enter the OTP you received: ")

if otp == int(otp_input):
    print("Verification successful!")
else:
    print("Verification failed.")

import random
import smtplib

fromaddr = "rameshkurnool777@gmail.com"
msg = "Your OTP is: "

otp = random.randint(100000, 999999)

# Send the OTP to the user's email
toaddr = input("rameshkurnool20@gmail.com")
msg += str(otp)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, 'sadhguru@777')
server.sendmail(fromaddr, toaddr, msg)
server.quit()

# Request user input for the OTP
otp_input = input("Enter the otp you recieved: ")

# Verify the OTP
if otp == int(otp_input):
    print("Verification successful!")
else:
    print("Verification failed.")
