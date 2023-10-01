import tkinter as tk
from tkinter import messagebox

class AddressBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Address Book")
        self.contacts = []

        self.add_contact_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_contacts_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.add_contact_button.pack()
        self.view_contacts_button.pack()

    def add_contact(self):
        # Implement the code to add a new contact
        pass

    def view_contacts(self):
        # Implement the code to view contacts
        pass

def main():
    root = tk.Tk()
    address_book = AddressBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()
