import tkinter as tk
import sqlite3 as sql

root = tk.Tk()
root.title("Contact Book Manager")
root.geometry("600x500")
root.config(bg="#1E1E1E")
root.resizable(False, False)

def create_database():
    conn = sql.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
    ''')
    conn.commit()
    conn.close()

def refresh_contacts():
    contacts_listbox.delete(0, tk.END)
    conn = sql.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, phone FROM contacts ORDER BY name')
    contacts = cursor.fetchall()
    for contact in contacts:
        contacts_listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")
    conn.close()
    status_label.config(text=f"Contacts: {len(contacts)}", fg="#4ECDC4")

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get("1.0", tk.END).strip()
    
    if not name or not phone:
        status_label.config(text="Name and Phone are required!", fg="#FF6B6B")
        root.after(2000, lambda: status_label.config(text="", fg="white"))
        return
    
    conn = sql.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)',
                  (name, phone, email, address))
    conn.commit()
    conn.close()
    
    clear_entries()
    refresh_contacts()
    status_label.config(text="Contact added successfully!", fg="#4ECDC4")
    root.after(2000, lambda: status_label.config(text="", fg="white"))

def search_contact():
    search_term = search_entry.get().strip()
    if not search_term:
        refresh_contacts()
        return
    
    contacts_listbox.delete(0, tk.END)
    conn = sql.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ? ORDER BY name',
                  (f'%{search_term}%', f'%{search_term}%'))
    contacts = cursor.fetchall()
    for contact in contacts:
        contacts_listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")
    conn.close()
    status_label.config(text=f"Found {len(contacts)} contacts", fg="#FFA500")

def view_contact_details(event):
    selection = contacts_listbox.curselection()
    if selection:
        contact_info = contacts_listbox.get(selection[0])
        name = contact_info.split(' - ')[0]
        
        conn = sql.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contacts WHERE name = ?', (name,))
        contact = cursor.fetchone()
        conn.close()
        
        if contact:
            details_window = tk.Toplevel(root)
            details_window.title("Contact Details")
            details_window.geometry("400x300")
            details_window.config(bg="#1E1E1E")
            
            tk.Label(details_window, text="Contact Details", bg="#1E1E1E", fg="#FFA500",
                    font=("Arial", 16, "bold")).pack(pady=10)
            
            details_frame = tk.Frame(details_window, bg="#1E1E1E")
            details_frame.pack(pady=10, padx=20, fill="both")
            
            tk.Label(details_frame, text=f"Name: {contact[1]}", fg="white", bg="#1E1E1E",
                    font=("Arial", 12), anchor="w").pack(fill="x", pady=5)
            tk.Label(details_frame, text=f"Phone: {contact[2]}", fg="white", bg="#1E1E1E",
                    font=("Arial", 12), anchor="w").pack(fill="x", pady=5)
            tk.Label(details_frame, text=f"Email: {contact[3] if contact[3] else 'N/A'}", fg="white", bg="#1E1E1E",
                    font=("Arial", 12), anchor="w").pack(fill="x", pady=5)
            tk.Label(details_frame, text=f"Address: {contact[4] if contact[4] else 'N/A'}", fg="white", bg="#1E1E1E",
                    font=("Arial", 12), anchor="w").pack(fill="x", pady=5)
            
            tk.Button(details_window, text="Close", bg="#FF6B6B", fg="black",
                     font=("Arial", 10, "bold"), command=details_window.destroy).pack(pady=10)

def delete_contact():
    selection = contacts_listbox.curselection()
    if selection:
        contact_info = contacts_listbox.get(selection[0])
        name = contact_info.split(' - ')[0]
        
        conn = sql.connect('contacts.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM contacts WHERE name = ?', (name,))
        conn.commit()
        conn.close()
        
        refresh_contacts()
        status_label.config(text="Contact deleted successfully!", fg="#FF6B6B")
        root.after(2000, lambda: status_label.config(text="", fg="white"))
    else:
        status_label.config(text="Please select a contact to delete!", fg="#FF6B6B")
        root.after(2000, lambda: status_label.config(text="", fg="white"))

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)

create_database()

heading = tk.Label(root, text="Contact Book Manager", bg="#1E1E1E", fg="#FFA500",
                  font=("Arial", 20, "bold"))
heading.pack(pady=10)

search_frame = tk.Frame(root, bg="#1E1E1E")
search_frame.pack(pady=10, padx=20, fill="x")

search_entry = tk.Entry(search_frame, bg="#2D2D2D", fg="white", font=("Arial", 12),
                       width=30)
search_entry.pack(side="left", padx=5)

search_btn = tk.Button(search_frame, text="Search", bg="#FFA500", fg="black",
                      font=("Arial", 10, "bold"), command=search_contact)
search_btn.pack(side="left", padx=5)

refresh_btn = tk.Button(search_frame, text="Refresh", bg="#4ECDC4", fg="black",
                       font=("Arial", 10, "bold"), command=refresh_contacts)
refresh_btn.pack(side="left", padx=5)

main_frame = tk.Frame(root, bg="#1E1E1E")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

contacts_frame = tk.Frame(main_frame, bg="#1E1E1E")
contacts_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

contacts_label = tk.Label(contacts_frame, text="Contacts List", fg="white", bg="#1E1E1E",
                         font=("Arial", 12, "bold"))
contacts_label.pack()

contacts_listbox = tk.Listbox(contacts_frame, bg="#2D2D2D", fg="white", font=("Arial", 11),
                             selectbackground="#FFA500", selectforeground="black")
contacts_listbox.pack(fill="both", expand=True)
contacts_listbox.bind('<Double-Button-1>', view_contact_details)

scrollbar = tk.Scrollbar(contacts_listbox, orient="vertical", command=contacts_listbox.yview)
scrollbar.pack(side="right", fill="y")
contacts_listbox.configure(yscrollcommand=scrollbar.set)

form_frame = tk.Frame(main_frame, bg="#1E1E1E")
form_frame.pack(side="right", fill="y", padx=(10, 0))

form_label = tk.Label(form_frame, text="Add New Contact", fg="white", bg="#1E1E1E",
                     font=("Arial", 12, "bold"))
form_label.pack(pady=(0, 10))

tk.Label(form_frame, text="Name *", fg="white", bg="#1E1E1E", font=("Arial", 10)).pack(anchor="w")
name_entry = tk.Entry(form_frame, bg="#2D2D2D", fg="white", font=("Arial", 11), width=25)
name_entry.pack(fill="x", pady=(0, 10))

tk.Label(form_frame, text="Phone *", fg="white", bg="#1E1E1E", font=("Arial", 10)).pack(anchor="w")
phone_entry = tk.Entry(form_frame, bg="#2D2D2D", fg="white", font=("Arial", 11), width=25)
phone_entry.pack(fill="x", pady=(0, 10))

tk.Label(form_frame, text="Email", fg="white", bg="#1E1E1E", font=("Arial", 10)).pack(anchor="w")
email_entry = tk.Entry(form_frame, bg="#2D2D2D", fg="white", font=("Arial", 11), width=25)
email_entry.pack(fill="x", pady=(0, 10))

tk.Label(form_frame, text="Address", fg="white", bg="#1E1E1E", font=("Arial", 10)).pack(anchor="w")
address_entry = tk.Text(form_frame, bg="#2D2D2D", fg="white", font=("Arial", 11), width=25, height=3)
address_entry.pack(fill="x", pady=(0, 15))

button_frame = tk.Frame(form_frame, bg="#1E1E1E")
button_frame.pack(fill="x")

add_btn = tk.Button(button_frame, text="Add Contact", bg="#4ECDC4", fg="black",
                   font=("Arial", 10, "bold"), command=add_contact)
add_btn.pack(side="left", padx=(0, 5))

clear_btn = tk.Button(button_frame, text="Clear", bg="#FFA500", fg="black",
                     font=("Arial", 10, "bold"), command=clear_entries)
clear_btn.pack(side="left", padx=5)

delete_btn = tk.Button(button_frame, text="Delete", bg="#FF6B6B", fg="black",
                      font=("Arial", 10, "bold"), command=delete_contact)
delete_btn.pack(side="left", padx=(5, 0))

status_label = tk.Label(root, text="", fg="white", bg="#1E1E1E", font=("Arial", 10))
status_label.pack(pady=5)

control_frame = tk.Frame(root, bg="#1E1E1E")
control_frame.pack(pady=10)

quit_btn = tk.Button(control_frame, text="Quit", bg="#FF6B6B", fg="black",
                    font=("Arial", 10, "bold"), command=root.quit)
quit_btn.pack()

refresh_contacts()

root.mainloop()