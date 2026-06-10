from tkinter import *
from tkinter import messagebox
import random 
import string
import json 

# (*) to import everything from tkinter
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits

    all_characters = letters + numbers

    password = ""

    for i in range(10):
        password += random.choice(all_characters)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Saved!")
    
def search_password():
    website = website_entry.get()

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(
            title="Error",
            message="No data file found."
        )
        return

    if website in data:
        username = data[website]["username"]
        password = data[website]["password"]
        messagebox.showinfo(
            title=website,
            message=f"Username: {username}\nPassword: {password}"
        )
    else:
        messagebox.showinfo(
            title="Not Found",
            message=f"No details for {website}"
        )    
window = Tk()
window.title("Password Manager")
window.geometry("500x350")

#website
Label(text="website").pack()
website_entry = Entry()
website_entry.pack()

#username
Label(text="Username").pack()
username_entry = Entry()
username_entry.pack()

#password
Label(text='password').pack()
password_entry = Entry()
password_entry.pack()

#create generate password button
generate_button = Button(
        text= 'Generate password ',
        command=generate_password
    )
generate_button.pack()

#create save password button
save_button = Button(
    text ='save',
    command = save_password
)
save_button.pack()

#create search password button
search_button = Button(
    text='search',
    command=search_password

)
search_button.pack()

window.mainloop()