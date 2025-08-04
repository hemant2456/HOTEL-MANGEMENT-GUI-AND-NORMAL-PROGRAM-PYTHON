import os
import sys
import pickle
from tkinter import *
import tkinter.ttk as ttk

# Global guest details list
details_list = []

# Class to store guest data
class Save:
    def __init__(self, name, address, mobile_no, room_no, price):
        self.name = name
        self.address = address
        self.mobile_no = mobile_no
        self.room_no = room_no
        self.price = price
        print(self.name, self.address, self.mobile_no, self.room_no, self.price)

# Function to save guest details to file
def file_save():
    if len(details_list) < 5:
        print("Details list incomplete.")
        return

    name, address, mobile, room, price = details_list[:5]
    guest = Save(name, address, mobile, room, price)
    
    with open("hotel.dat", "ab") as f:
        pickle.dump(guest, f, protocol=2)

    print("Guest saved successfully!")

# Class for checkout window
class HotelCheckoutWindow:
    def __init__(self):
        def check_room():
            room_input = self.data.get()
            self.Text1.insert(INSERT, f"Checking room: {room_input}\n")
            if room_input.isdigit():
                room_no = int(room_input)
                found = False

                try:
                    with open("hotel.dat", "rb") as f, open("temp.dat", "ab") as temp:
                        while True:
                            try:
                                guest = pickle.load(f)
                                if guest.room_no == room_no:
                                    found = True
                                    name1 = guest.name
                                else:
                                    pickle.dump(guest, temp)
                            except EOFError:
                                break
                except FileNotFoundError:
                    self.Text1.insert(INSERT, "No data file found.\n")
                    return

                if found:
                    self.Text1.insert(INSERT, f"THANK YOU {name1.upper()} FOR VISITING US\n")
                else:
                    self.Text1.insert(INSERT, "NO GUEST FOUND\n")

                os.remove("hotel.dat")
                os.rename("temp.dat", "hotel.dat")
            else:
                self.Text1.insert(INSERT, "Invalid input. Please enter a valid ROOM NO.\n")

        # Tkinter GUI
        root = Tk()
        root.title("HOTEL MANAGEMENT")
        root.geometry("1011x750")
        root.configure(bg="white")

        font11 = ("Segoe UI", 23, "bold")
        font12 = ("Segoe UI", 24, "bold")
        font9 = ("Segoe UI", 9)

        self.Frame1 = Frame(root, bg="white", relief=GROOVE, bd=2)
        self.Frame1.place(relx=0.04, rely=0.04, relwidth=0.91, relheight=0.91)

        self.Label1 = Label(self.Frame1, text="ENTER THE ROOM NO. :", font=font11, bg="white", fg="black")
        self.Label1.place(relx=0.14, rely=0.12, height=46, width=442)

        self.data = StringVar()
        self.Entry1 = Entry(self.Frame1, textvariable=self.data, font=("Courier New", 10))
        self.Entry1.place(relx=0.67, rely=0.12, height=44, relwidth=0.07)

        self.Button1 = Button(self.Frame1, text="CHECK OUT", font=font12, command=check_room)
        self.Button1.place(relx=0.34, rely=0.28, height=93, width=286)

        self.Text1 = Text(self.Frame1, font=font9, wrap=WORD, bg="white", fg="black")
        self.Text1.place(relx=0.05, rely=0.54, relwidth=0.89, relheight=0.4)

        root.mainloop()

# Example for adding guest details (normally comes from user input in full app)
details_list = ["Alice", "Mumbai", "9876543210", 101, 5000.0]
file_save()

# Launch the checkout window
if __name__ == '__main__':
    HotelCheckoutWindow()
