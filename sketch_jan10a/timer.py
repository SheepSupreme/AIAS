import tkinter as tk
import time

class Timer:
    def __init__(self, end_time, root):
        self.root = root
        self.delay = False
        self.start_time = time.time()
        self.end_time = self.start_time + end_time
        self.current_time = self.end_time - time.time()
        self.container = tk.Frame(master=self.root)
        self.container.grid(row=0, column=0, sticky='nswe')
        self.label = tk.Label(self.container, font=('Arial', 24), bg='lightgreen',fg='black')
        self.label.pack(fill=tk.BOTH)

class App:
    def __init__(self, root):
        self.timer_list = []
        self.root = root
        self.root.title("Current Time Display")

        self.Queue = tk.Frame(master=self.root, background='grey')
        self.Queue.grid(padx=10,pady=10,ipadx=10,ipady=10)

        self.entry = tk.Entry(master=self.Queue, font=('Arial', 20))
        self.entry.grid(row=0, column=0,padx=10,pady=10)

        self.button_1 = tk.Button(master=self.Queue, text='add timer', command=self.add_timer,font=('Arial', 22))
        self.button_1.grid(row=1, column=0)

        self.update()
    def add_timer(self):
        try:
            self.timer_list.append(Timer(int(self.entry.get()),root))
            self.update_queue()
        except ValueError:
            print('Eingabe nicht zulässig')
    
    def timer_sort(self):
        sorted_list = sorted(self.timer_list, key=lambda x: x.current_time, reverse = True)
        self.timer_list = sorted_list

    def update_queue(self):
        self.timer_sort()
        for timer in self.timer_list:
            timer.current_time = timer.end_time - time.time()
            timer.label.config(text = int(timer.current_time)) 
            timer.container.grid(row=self.timer_list.index(timer)+2,column=0)
            if timer.current_time < 0:
                timer.label.config(bg='red',fg='white')

    def update(self):
        self.update_queue()      

        self.root.after(1000, self.update)
    

# Create the main window
root = tk.Tk()

# Create an instance of the App class
App(root)

# Run the Tkinter event loop
root.mainloop()
