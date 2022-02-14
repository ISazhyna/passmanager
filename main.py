from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def test():
    text=went.get()
    print(text)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canv=Canvas(width=200, height=200)

logo_img=PhotoImage(file="logo.png")
canv.create_image(100, 100, image = logo_img)
canv.grid(row=0, column=1)

wlab=Label(text="Website: ")
wlab.grid(row=1,column=0)
went=Entry(width=35)
went.grid(row=1, column=1,columnspan=2)

eulab=Label(text="Email/Username: ")
eulab.grid(row=2,column=0)
euent=Entry(width=35)
euent.grid(row=2, column=1,columnspan=2)

plab=Label(text="Password:")
plab.grid(row=3,column=0)
pent=Entry(width=21)
pent.grid(row=3, column=1,columnspan=1)

genbutt=Button(window, text="Generate Password", command=test)
genbutt.grid(row=3, column=2,columnspan=1)

addbutt=Button(text="Add", command=test)

addbutt.grid(row=4, column=1, sticky=N)

window.mainloop()