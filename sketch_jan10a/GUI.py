import tkinter as tk
import time

class Timer:
    def __init__(self, end_time, root):
        self.root = root
        self.start_time = time.time()
        self.current_time = time.time()
        self.end_time = self.start_time + end_time
        self.label = tk.Label(root, font=('Arial', 24))
        self.label.pack(padx=20, pady=20)
        self.update_time()
    def update_time(self):
        self.current_time = time.time()
        self.current_time = self.end_time - self.current_time
        self.label.config(text = int(self.current_time))
        self.root.after(1000, self.update_time)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Current Time Display")

        self.timer_1 = Timer(60,root)
        self.timer_2 = Timer(100,root)

# Create the main window
root = tk.Tk()

# Create an instance of the App class
app = App(root)

# Run the Tkinter event loop
root.mainloop()
