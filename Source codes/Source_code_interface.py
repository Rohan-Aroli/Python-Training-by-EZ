import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

history = []
configurations = {}

class User:
    def create_config(self):
        no_of_attributes = simpledialog.askinteger("Input", 'Enter the number of attributes you want')
        if no_of_attributes is not None:
            for _ in range(no_of_attributes):
                key = simpledialog.askstring("Input", 'Enter the key')
                value = simpledialog.askstring("Input", 'Enter the value')
                if key and value:
                    configurations[key] = value

            current_time = datetime.now()
            history.append(f'Attribute has been created! (Created at {current_time})')
            messagebox.showinfo("Current Configurations", str(configurations))

    def read_config(self):
        while True:
            user_key = simpledialog.askstring("Input", 'Enter the key you want to read (enter END to terminate)')
            if user_key == 'END':
                break
            attribute = configurations.get(user_key, 'The input key was not found')
            messagebox.showinfo("Attribute", str(attribute))

            current_time = datetime.now()
            history.append(f'Read operation has been performed! (Read at {current_time})')

class Admin(User):
    def update_config(self):
        while True:
            user_key = simpledialog.askstring("Input", 'Enter the key to be updated (Type END to stop)')
            if user_key == 'END':
                break
            if user_key in configurations:
                user_value = simpledialog.askstring("Input", 'Enter the new value')
                if user_value:
                    configurations[user_key] = user_value
                    messagebox.showinfo("Updated", f'Updated {user_key} to {user_value}')
            else:
                messagebox.showerror("Error", 'The entered key was not found!')

        current_time = datetime.now()
        history.append(f'The dictionary has been updated! (Updated at: {current_time})')

    def delete_config(self):
        while True:
            user_key = simpledialog.askstring("Input", 'Enter the key to be deleted (Enter END to stop)')
            if user_key == 'END':
                break
            if user_key in configurations:
                del configurations[user_key]
                messagebox.showinfo("Deleted", f'The given key {user_key} is successfully deleted.')
            else:
                messagebox.showerror("Error", 'The entered key was not found.')

        current_time = datetime.now()
        history.append(f'Delete operation has been performed. (Deleted at {current_time})')

    def show_history(self):
        messagebox.showinfo("History", "\n".join(history))

    def view_config(self):
        messagebox.showinfo("Configurations", str(configurations))
        current_time = datetime.now()
        history.append(f'The dictionary has been viewed. (Viewed at {current_time})')

def main():
    root = tk.Tk()
    root.title("Configuration Manager")

    user = User()
    admin = Admin()

    def user_menu():
        while True:
            choice = simpledialog.askinteger("Input", '''Enter your choice:
            1 for CREATE
            2 to READ
            0 to Terminate loop.''')
            if choice == 1:
                user.create_config()
            elif choice == 2:
                user.read_config()
            elif choice == 0:
                break
            else:
                messagebox.showerror("Error", 'Enter valid input')

    def admin_menu():
        password = simpledialog.askstring("Input", 'Enter the password:')
        if password == 'admin123':
            while True:
                choice = simpledialog.askinteger("Input", '''Enter your choice:
                1 for CREATE
                2 to READ
                3 to UPDATE
                4 to DELETE
                5 to view history
                6 to view the dictionary
                0 to terminate the loop.''')
                if choice == 1:
                    admin.create_config()
                elif choice == 2:
                    admin.read_config()
                elif choice == 3:
                    admin.update_config()
                elif choice == 4:
                    admin.delete_config()
                elif choice == 5:
                    admin.show_history()
                elif choice == 6:
                    admin.view_config()
                elif choice == 0:
                    break
                else:
                    messagebox.showerror("Error", 'Invalid choice! Please enter a valid input.')
        else:
            messagebox.showerror("Error", 'Incorrect password.')

    def role_selection():
        role = simpledialog.askstring("Input", 'Enter your role (user/admin):').lower()
        if role == 'user':
            user_menu()
        elif role == 'admin':
            admin_menu()
        else:
            messagebox.showerror("Error", 'Enter a valid role!')

    tk.Button(root, text='Select Role', command=role_selection).pack(pady=20)
    tk.Button(root, text='Exit', command=root.quit).pack(pady=20)

    root.mainloop()
    root.destroy()

if __name__ == "__main__":
    main()
