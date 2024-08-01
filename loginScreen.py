import tkinter as tk

# the code must be understandable
# organization and pattern in the declarations of functions and methods like: interface in the high part of the code and the functions on the down part.
# variables names like the example: example_example or Example.
# constants like the example EXAMPLE
##


class login():
    def __init__(self, master, sign_up_instance):
        self.master = master
        self.master.title("Janelinha")
        self.master.geometry("350x200")
        self.master.resizable(0, 0)

        self.sign_up_instance = sign_up_instance
        
        self.title = tk.Label(self.master, text='Login', fg='blue', font='arial')
        self.title.grid(row=0, column=1)
        
        self.text_user = tk.Label(self.master, text='Username', font='arial')    # 'Username' text in interface
        self.text_user.grid(row=1, column=0, pady=5)    # placing 'Username' in window, row 1, column 0

        self.text_password = tk.Label(self.master, text='Password', font='arial')   # 'Password' text in interface
        self.text_password.grid(row=2, column=0, pady=5)    # placing 'Password' in window, row 2, column 0
        
        self.entry_user = tk.Entry(self.master)    # 'Username' entry text
        self.entry_user.grid(row=1, column=1)    # Placing 'Username' entry in window

        self.entry_password = tk.Entry(self.master)    # 'Password' entry text
        self.entry_password.grid(row=2, column=1)    # Placing 'Password' entry in window

        self.exit_button = tk.Button(self.master, text='Fechar', command=self.exit_app)    # Button with 'exit_app' function, to close the window
        self.exit_button.grid(column= 0, row= 4)    # Placing button in window


        
     # functions for buttons
     
    def exit_app(self):
        self.master.destroy()

class sign_up():
    def __init__(self, master):
        self.master = master
        self.master.title("Sign up")
        self.master.geometry("350x200")    
        self.master.resizable(0, 0)
        self.security = {}

        self.text_user = tk.Label(self.master, text='Username', font='arial')    # 'Username' text in interface
        self.text_user.grid(row=1, column=0, pady=5)    # placing 'Username' in window, row 1, column 0

        self.text_password = tk.Label(self.master, text='Password', font='arial')   # 'Password' text in interface
        self.text_password.grid(row=2, column=0, pady=5)    # placing 'Password' in window, row 2, column 0
        
        self.entry_user = tk.Entry(self.master)    # 'Username' entry text
        self.entry_user.grid(row=1, column=1)    # Placing 'Username' entry in window

        self.entry_password = tk.Entry(self.master)    # 'Password' entry text
        self.entry_password.grid(row=2, column=1)    # Placing 'Password' entry in window

        self.button_sign = tk.Button(self.master, text='Sign')
        self.button_sign.grid(row=3, column=1)

        self.h1 = tk.Label(self.master, text='Sign up', font='arial')
        self.h1.grid(row=0, column=1)

    def sign_up(self):
        self
        
        
        


if __name__ == '__main__':
    root_sign_up = tk.Tk()
    root_login = tk.Tk()
    
    sign_up_instance = sign_up(root_sign_up)
    login_instance = login(root_login, sign_up_instance)
    
    root_login.mainloop()
    root_sign_up.mainloop()
