import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from dbhelper import DBhelper

class FlipkartGUI:
    def __init__(self, root):
        self.db = DBhelper()
        self.root = root
        self.root.title("Flipkart Registration and Login")
        self.root.geometry("800x600")
        
        # Load background image
        self.background_image = Image.open("register.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create canvas to display background image
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="lightgray", bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.label_title = tk.Label(self.frame, text="Flipkart", font=("Arial", 24, "bold"), bg="lightgray")
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

        self.label_name = tk.Label(self.frame, text="Name:", font=("Arial", 14), bg="lightgray")
        self.label_name.grid(row=1, column=0, pady=5, padx=10, sticky="e")

        self.entry_name = ttk.Entry(self.frame, font=("Arial", 14))
        self.entry_name.grid(row=1, column=1, pady=5, padx=10)

        self.label_email = tk.Label(self.frame, text="Email:", font=("Arial", 14), bg="lightgray")
        self.label_email.grid(row=2, column=0, pady=5, padx=10, sticky="e")

        self.entry_email = ttk.Entry(self.frame, font=("Arial", 14))
        self.entry_email.grid(row=2, column=1, pady=5, padx=10)

        self.label_password = tk.Label(self.frame, text="Password:", font=("Arial", 14), bg="lightgray")
        self.label_password.grid(row=3, column=0, pady=5, padx=10, sticky="e")

        self.entry_password = ttk.Entry(self.frame, show='*', font=("Arial", 14))
        self.entry_password.grid(row=3, column=1, pady=5, padx=10)

        self.button_register = tk.Button(self.frame, text="Register", font=("Arial", 14), command=self.register)
        self.button_register.grid(row=4, column=0, pady=10, padx=10, sticky="e")

        self.button_login = tk.Button(self.frame, text="Login", font=("Arial", 14), command=self.login)
        self.button_login.grid(row=4, column=1, pady=10, padx=10, sticky="w")

    def register(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        if name and email and password:
            response = self.db.register(name, email, password)
            if response == 1:
                messagebox.showinfo("Success", "Registration successful")
            else:
                messagebox.showerror("Error", "Registration failed")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        if email and password:
            data = self.db.search(email, password)
            if len(data) == 0:
                messagebox.showerror("Error", "Access denied")
            else:
                messagebox.showinfo("Success", f"Hello {data[0][1]}")
                self.show_login_menu()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def show_login_menu(self):
        self.login_menu_window = tk.Toplevel(self.root)
        self.login_menu_window.title("Login Menu")
        self.login_menu_window.geometry("400x300")

        self.label_menu = tk.Label(self.login_menu_window, text="Login Menu", font=("Arial", 20))
        self.label_menu.pack(pady=10)

        self.button_profile = tk.Button(self.login_menu_window, text="See Profile")
        self.button_profile.pack(pady=5)

        self.button_edit_profile = tk.Button(self.login_menu_window, text="Edit Profile")
        self.button_edit_profile.pack(pady=5)

        self.button_delete_profile = tk.Button(self.login_menu_window, text="Delete Profile")
        self.button_delete_profile.pack(pady=5)

        self.button_logout = tk.Button(self.login_menu_window, text="Logout", command=self.login_menu_window.destroy)
        self.button_logout.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlipkartGUI(root)
    root.mainloop()
