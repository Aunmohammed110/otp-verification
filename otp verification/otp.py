import random
from twilio.rest import Client
otp=random.randint(1000,9999)
account_sid = 'AC6b4665b6abac1ca9a1f25ecc2e318bba'
auth_token = '1231c62a6b72d94e70616e883745ba6f'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = f'Your OTP is {otp}',
    from_='+15673646816',
    to='+917659817618'

  
)

