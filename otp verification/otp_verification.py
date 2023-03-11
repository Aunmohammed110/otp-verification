from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox

class otp_verifier (Tk) :
    def __init__(self):
        super().__init__()
        self.geometry ( "600x550")
        self.resizable(False, False)
        self.n =random.randint(1000,9999)
        account_sid = 'AC6b4665b6abac1ca9a1f25ecc2e318bba'
        auth_token = '1231c62a6b72d94e70616e883745ba6f'
        self.client = Client(account_sid, auth_token)
        self.client.messages.create(to=["+917659817618"],from_ ="+15673646816",
                                 body=self.n)

    def Labels(self):
        self.c = Canvas(self, bg = "white", width=400, height=280)
        self.c.place (x=100,y=60)
        self.Login_Title = Label(self, text= "OTP Verification", font="bold, 20", bg="white")
        self.Login_Title.place(x=210,y=90)

    def Entry(self):
        self.User_Name =Text (self, borderwidth=2, wrap= "word", width=29, height=2)
        self.User_Name.place (x=190,y=168)

    def Buttons(self):
        self.submitButtonImage=PhotoImage(file="submit.png")
        self.submitButton =Button (self, image=self.submitButtonImage, command=self.checkOTP,border=0)
        self.submitButton.place(x=245,y=220)
        
        self.resendOTPImage=PhotoImage(file="resend.png")
        self.resendOTP=Button (self, image=self.resendOTPImage, command=self.resendOTP, border=0)
        self.resendOTP.place(x=245,y=280)

    def checkOTP(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo","Login success")
                self.n="done"
            elif self.n=="done":
                messagebox.showinfo("showinfo","Already Entered the otp")
            else:
                messagebox.showinfo("showinfo","Wrong OTP")
        except:
            messagebox.showinfo("showinfo","invalid OTP")            


    def resendOTP(self):
        self.n =random.randint(1000,9999)
        account_sid = 'AC6b4665b6abac1ca9a1f25ecc2e318bba'
        auth_token = '1231c62a6b72d94e70616e883745ba6f'
        self.client = Client(account_sid, auth_token)
        self.client.messages.create (to=["+917659817618"],from_ ="+15673646816",
                                 body=self.n)



if __name__ =="__main__":
    window=otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()
