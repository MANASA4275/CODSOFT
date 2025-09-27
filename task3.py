import tkinter as tk
import random

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x350")
root.config(bg="#1E1E1E")

def update():
    length_msg.config(text="")
    complexity_msg.config(text="")

def weak_password(length):
    password = ""
    for i in range(length):
        ran = random.randrange(1, 3)
        if ran == 1:
            password += chr(random.randrange(65, 91))
        else:
            password += chr(random.randrange(97, 123))
    return password

def moderate_password(length):
    password = ""
    for i in range(length):
        ran = random.randrange(1, 4)
        if ran == 1:
            password += chr(random.randrange(65, 91))
        elif ran == 2:
            password += chr(random.randrange(97, 123))
        else:
            password += chr(random.randrange(48, 58))
    return password

def strong_password(length):
    password = ""
    for i in range(length):
        password += chr(random.randrange(33, 127))
    return password

def generate_password():
    if not length_entry.get():
        length_msg.config(text="Please enter a length")
        root.after(2000, update)
        return
        
    if length_entry.get().isdigit():
        length_val = int(length_entry.get())
        if 5 <= length_val <= 50:
            if complexity.get() != "None":
                password = ""
                
                if complexity.get() == "weak":
                    password = weak_password(length_val)
                elif complexity.get() == "moderate":
                    password = moderate_password(length_val)
                else:
                    password = strong_password(length_val)
                    
                result_window = tk.Toplevel(root)
                result_window.geometry("500x100")
                result_window.config(bg="#1E1E1E")
                result_window.title("Generated Password")
                
                password_label = tk.Label(result_window, text=password, bg="#1E1E1E", 
                                        fg="#FFA500", font=("Arial", 16, "bold"))
                password_label.pack(pady=30)
    
            else:
                complexity_msg.config(text="Please select complexity level")
                root.after(2000, update)
        else:
            length_msg.config(text="Length must be between 5-50")
            root.after(2000, update)
    else:
        length_msg.config(text="Length must be a number")
        root.after(2000, update)

heading = tk.Label(root, text="Password Generator", bg="#1E1E1E", fg="#FFA500",
                  font=("Arial", 20, "bold"))
heading.pack(pady=20)

main_frame = tk.Frame(root, bg="#1E1E1E")
main_frame.pack(pady=10)

length_frame = tk.Frame(main_frame, bg="#1E1E1E")
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Password Length:", fg="white", bg="#1E1E1E",
                       font=("Arial", 12, "bold"))
length_label.pack(side="left", padx=5)

length_entry = tk.Entry(length_frame, bg="#2D2D2D", fg="#FFA500", font=("Arial", 12),
                       justify="center", width=10)
length_entry.pack(side="left", padx=5)

length_msg = tk.Label(length_frame, text="", font=("Arial", 9), bg="#1E1E1E", fg="red")
length_msg.pack(pady=5)

complexity_frame = tk.Frame(main_frame, bg="#1E1E1E")
complexity_frame.pack(pady=15)

complexity_label = tk.Label(complexity_frame, text="Complexity Level:", fg="white", 
                           bg="#1E1E1E", font=("Arial", 12, "bold"))
complexity_label.pack()

radio_frame = tk.Frame(complexity_frame, bg="#1E1E1E")
radio_frame.pack(pady=10)

complexity = tk.StringVar()
complexity.set("None")

weak_radio = tk.Radiobutton(radio_frame, text="Weak", fg="#FF6B6B", bg="#1E1E1E",
                           font=("Arial", 10, "bold"), variable=complexity, value="weak")
weak_radio.grid(row=0, column=0, padx=15)

moderate_radio = tk.Radiobutton(radio_frame, text="Moderate", fg="#FFA500", bg="#1E1E1E",
                               font=("Arial", 10, "bold"), variable=complexity, value="moderate")
moderate_radio.grid(row=0, column=1, padx=15)

strong_radio = tk.Radiobutton(radio_frame, text="Strong", fg="#7CE1E1", bg="#1E1E1E",
                             font=("Arial", 10, "bold"), variable=complexity, value="strong")
strong_radio.grid(row=0, column=2, padx=15)

complexity_msg = tk.Label(complexity_frame, text="", font=("Arial", 9), bg="#1E1E1E", fg="red")
complexity_msg.pack(pady=5)

button_frame = tk.Frame(main_frame, bg="#1E1E1E")
button_frame.pack(pady=20)

generate_btn = tk.Button(button_frame, text="Generate Password", bg="#FFA500", fg="black",
                        font=("Arial", 12, "bold"), command=generate_password, width=15)
generate_btn.grid(row=0, column=0, padx=10)

quit_btn = tk.Button(button_frame, text="Quit", bg="#FF6B6B", fg="black",
                    font=("Arial", 12, "bold"), command=root.quit, width=10)
quit_btn.grid(row=0, column=1, padx=10)

root.mainloop()