import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get().strip()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        selection = task_listbox.curselection()
        if selection:
            the_value = task_listbox.get(selection[0])
            if the_value in tasks:
                tasks.remove(the_value)
                list_update()
                the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    if tasks:
        message_box = messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks?')
        if message_box:
            tasks.clear()
            the_cursor.execute('delete from tasks')
            list_update()
    else:
        messagebox.showinfo('Info', 'No tasks to delete.')

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    the_connection.commit()
    the_cursor.close()
    guiWindow.destroy()

def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("520x480+750+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg = "#2C3E50")
    
    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')
    
    tasks = []
    
    main_frame = tk.Frame(guiWindow, bg = "#34495E", padx=10, pady=10)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    header_label = ttk.Label(
        main_frame,
        text = "To-Do List Manager",
        font = ("Arial", "16", "bold"),
        background = "#34495E",
        foreground = "#ECF0F1"
    )
    header_label.pack(pady = (0, 15))
    
    input_frame = tk.Frame(main_frame, bg = "#34495E")
    input_frame.pack(fill="x", pady=(0, 10))
    
    task_label = ttk.Label(
        input_frame,
        text = "Enter Task:",
        font = ("Arial", "10", "bold"),
        background = "#34495E",
        foreground = "#ECF0F1"
    )
    task_label.pack(anchor="w")
    
    task_field = ttk.Entry(
        input_frame,
        font = ("Arial", "11"),
        width = 30
    )
    task_field.pack(fill="x", pady=(5, 10))
    task_field.focus()
    
    buttons_frame = tk.Frame(main_frame, bg = "#34495E")
    buttons_frame.pack(fill="x", pady=(0, 15))
    
    add_button = ttk.Button(
        buttons_frame,
        text = "Add Task",
        width = 15,
        command = add_task
    )
    del_button = ttk.Button(
        buttons_frame,
        text = "Delete Selected",
        width = 15,
        command = delete_task
    )
    del_all_button = ttk.Button(
        buttons_frame,
        text = "Delete All",
        width = 15,
        command = delete_all_tasks
    )
    
    add_button.pack(side="left", padx=(0, 5))
    del_button.pack(side="left", padx=5)
    del_all_button.pack(side="left", padx=(5, 0))
    
    list_frame = tk.Frame(main_frame, bg = "#34495E")
    list_frame.pack(fill="both", expand=True)
    
    list_label = ttk.Label(
        list_frame,
        text = "Your Tasks:",
        font = ("Arial", "10", "bold"),
        background = "#34495E",
        foreground = "#ECF0F1"
    )
    list_label.pack(anchor="w")
    
    task_listbox = tk.Listbox(
        list_frame,
        width = 40,
        height = 12,
        selectmode = 'SINGLE',
        background = "#ECF0F1",
        foreground = "#2C3E50",
        selectbackground = "#3498DB",
        selectforeground = "#FFFFFF",
        font = ("Arial", "10"),
        relief = "flat",
        highlightthickness = 0
    )
    task_listbox.pack(fill="both", expand=True, pady=(5, 0))
    
    scrollbar = ttk.Scrollbar(task_listbox, orient="vertical", command=task_listbox.yview)
    scrollbar.pack(side="right", fill="y")
    task_listbox.configure(yscrollcommand=scrollbar.set)
    
    exit_frame = tk.Frame(main_frame, bg = "#34495E")
    exit_frame.pack(fill="x", pady=(10, 0))
    
    exit_button = ttk.Button(
        exit_frame,
        text = "Exit Application",
        width = 20,
        command = close
    )
    exit_button.pack()
    
    retrieve_database()
    list_update()
    
    guiWindow.mainloop()