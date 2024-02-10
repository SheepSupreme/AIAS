import tkinter as tk
import time

class Timer:
    def __init__(self, end_time, root, index):
        self.index = index
        self.root = root
        self.start_time = time.time()
        self.current_time = time.time()
        self.end_time = self.start_time + end_time
        self.container = tk.Frame(self.root)
        self.container.pack()
        self.ident = tk.Label(self.container, font=('Arial',24),text=str(index)+':')
        self.ident.pack(side='left')
        self.count = tk.Label(self.container, font=('Arial', 24))
        self.count.pack()
        self.update_time()
    def update_time(self):
        self.current_time = time.time()
        self.current_time = self.end_time - self.current_time
        self.count.config(text = int(self.current_time))
        self.root.after(1000, self.update_time)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Current Time Display")

        self.button = tk.Button(text='press')
        self.button.pack()

        self.timer_1 = Timer(60,root,1)
        self.timer_2 = Timer(100,root,2)

# Create the main window
root = tk.Tk()

# Create an instance of the App class
app = App(root)

# Run the Tkinter event loop
root.mainloop()
