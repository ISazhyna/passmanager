from tkinter import *
import string
import secrets

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():
    password=''.join(secrets.choice(string.ascii_letters+ string.digits) for _ in range(10))
    passent.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def savedata():
    website=webent.get()
    email=emailent.get()
    password = passent.get()
    f = open("data.txt", "a")
    f.write(f"{website} | {email} | {password}\n")
    f.close()
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canv=Canvas(width=200, height=200)

logo_img=PhotoImage(file="logo.png")
canv.create_image(100, 100, image = logo_img)
canv.grid(row=0, column=1)

weblab=Label(text="Website: ")
weblab.grid(row=1, column=0)
webent=Entry(width=35)
webent.grid(row=1, column=1, columnspan=2)

emailab=Label(text="Email/Username: ")
emailab.grid(row=2, column=0)
emailent=Entry(width=35)
emailent.insert(0, "email@gmail.com")
emailent.grid(row=2, column=1, columnspan=2)

passlab=Label(text="Password:")
passlab.grid(row=3, column=0)
passent=Entry(width=21)
passent.grid(row=3, column=1, columnspan=1)

genbtn=Button(window, text="Generate Password", command=generatepassword)
genbtn.grid(row=3, column=2, columnspan=1)

addbtn=Button(text="Add", command=savedata)

addbtn.grid(row=4, column=1, sticky=N)

window.mainloop()