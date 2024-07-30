import tkinter as tk

# the code must be understandable
# organization and pattern in the declarations of functions and methods
# variables names#


class login():
    def __init__(self, master):
        self.master = master
        self.master.title("Janelinha")
        self.master.geometry("350x200")
        self.master.resizable(0, 0)
        
        self.title = tk.Label(self.master, text='Login', fg='blue', font='arial')
        self.title.grid(row=0, column=1)
        
        self.textUser = tk.Label(self.master, text='Username', font='arial')
        self.textUser.grid(row=1, column=0)
        
     # functions for buttons
     
    def exit_app():
        root.destroy()
        exit_app = tk.Button(root, text= "Exit", command= exit_app)
        exit_app.grid(column= 0, row= 4)

if __name__ == '__main__':
    root = tk.Tk()
    login(root)
    root.mainloop()
