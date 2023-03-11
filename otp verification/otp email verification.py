import random
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
#adding TLS security 
server.starttls()
#get your app password of gmail ----as directed in the video
password='edifvdkkisvuyucl'
server.login("aunmohammed110@gmail.com",password)
#generate OTP using random.randint() function
otp=''.join([str(random.randint(0,9)) for i in range(6)])
msg='Hello, Your OTP is '+str(otp)
sender='aunmohammed110@gmail.com'  #write email id of sender
receiver='sirtesla52@gmail.com' #write email of receiver
#sendi
server.sendmail(sender,receiver,msg)
server.quit()