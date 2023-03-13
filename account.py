import configparser
import smtplib
import random
import sys
from email.message import EmailMessage
import ssl

config = configparser.ConfigParser()

class Accounts():

    def signup(self):
        while True:
            username = input("Please choose a username for your account")
            password = input("Please choose a password for your account")
            self.email = input("Please choose a email for your account")
            if config.has_section(username) == True:
                print("This username already in use please try another one.")
            else:
                with open("deneme2.ini","r") as f:
                    if self.email in f.read():
                        print("This email already in use please try another one.")
                    else:
                        print("We send a code to your email. Check it out.")
                        self.code = random.randint(1,99999)
                        self.sendemail()
                        usercode = int(input("Please input code that we sent you."))
                        if usercode == self.code:
                            print("You successfully signed up.")
                            config.read("deneme2.ini")
                            config.add_section(username)
                            config[username] = {"password":password,"email":self.email}
                            with open("deneme2.ini","w",encoding="utf-8") as f:
                                config.write(f)
                                sys.exit()
                        else:
                            print("The code is wrong")
    def login(self):
        while True:
            self.username = input("Please input your username.")
            password = input("Please input your password.")
            config.read("deneme2.ini")
            if config.has_section(self.username) == True:
                if config.get(self.username,"password") == password:
                    print("You successfully logged in.")
                    print("""
*************************************
Please choose what do you want to do.
1-Change Password
2-Delete Account
*************************************
                    """)
                    while True:

                        choice_1 = input("Your choice: ")
                        if int(choice_1) == 1:
                            ac.changepassword()
                        elif int(choice_1) == 2:
                            ac.delaccount()
                        else:
                            print("Please select a valid transaction.")

                else:
                    print("The password is wrong.")
            else:
                print("This username is not exist.")
    def sendemail(self):
        email_sender = "swarthy330@gmail.com"
        email_password = mypassword
        email_receiver = self.email
        subject = "PYTHON ACCOUNT PROJECT"
        body = """The code is: {}""".format(self.code)
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())

    def changepassword(self):
        config.read("deneme2.ini")
        newpassword = input("Please input your new password")
        config.set(self.username,"password",newpassword)
        with open("deneme2.ini","w",encoding="utf-8") as f:
            config.write(f)
            sys.exit()

    def delaccount(self):
        config.read("deneme2.ini")
        config.remove_section(self.username)
        print("You successfully deleted your account.")
        with open("deneme2.ini","w",encoding="utf-8") as f:
            config.write(f)
            sys.exit()
ac = Accounts()
print("""
**************************
Please choose what do you want to do.
1-Login
2-Signup
**************************
""")
while True:

    choice = input("Your choice: ")
    if int(choice) == 1:
        ac.login()
    elif int(choice) == 2:
        ac.signup()
    else:
        print("Please select a valid transaction.")
