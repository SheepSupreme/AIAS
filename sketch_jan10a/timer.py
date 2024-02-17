import time
import customtkinter
import serial

#Serial setup
serial_port = 'COM4'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=10)

class Timer:
    def __init__(self, name, end_time, root):
        self.root = root
        self.name = name
        self.root.columnconfigure(0,weight=1)
        self.start_time = time.time()
        self.end_time = self.start_time + end_time
        self.current_time = self.end_time - time.time()
        self.container = customtkinter.CTkFrame(master=self.root)
        self.container.grid(row=0, column=0, sticky='nswe')
        self.label = customtkinter.CTkLabel(self.container, font=('Arial', 24))
        self.label.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.name = customtkinter.CTkLabel(self.container, font=('Arial', 24), text = self.name)
        self.name.grid(row = 0, column = 0, padx = 10, pady = 10)

class App:
    def __init__(self, root):
        self.timer_list = []
        self.root = root
        self.root.title("Current Time Display")
        self.root.columnconfigure(0,weight=1)

        self.Queue = customtkinter.CTkFrame(self.root)
        self.Queue.grid(padx=10,pady=10,ipadx=10,ipady=10)

        self.entry = customtkinter.CTkEntry(self.Queue, font=('Arial', 20))
        self.entry.grid(row=0, column=0,padx=10,pady=10)

        self.button_1 = customtkinter.CTkButton(master=self.Queue, text='add timer', command=self.add_e_timer,font=('Arial', 22))
        self.button_1.grid(row=1, column=0)

        self.update()

    def add_timer(self,time):
        self.timer_list.append(Timer('Timer_QR',time,self.root))
        self.update_queue()

    def add_e_timer(self):
        self.timer_list.append(Timer('Timer',int(self.entry.get()),self.root))
        self.update_queue()        
    
    def timer_sort(self):
        sorted_list = sorted(self.timer_list, key=lambda x: x.current_time, reverse = True)
        self.timer_list = sorted_list

    def update_queue(self):
        self.timer_sort()
        for timer in self.timer_list:
            timer.current_time = timer.end_time - time.time()
            timer.label.configure(text = int(timer.current_time)) 
            timer.container.grid(row=self.timer_list.index(timer)+2,column=0)
            if timer.current_time < 0:
                timer.label.configure(bg_color = 'red')

    def update(self):
        self.update_queue()      

        self.root.after(1000, self.update)
    

# Create the main window
root = customtkinter.CTk()

# Create an instance of the App class
game_instance = App(root)

# Run the Tkinter event loop
while True:
    if ser.in_waiting > 0:
        text_mod = ser.readline()
        message = text_mod.decode().strip()
        print("message received:",message);
        game_instance.add_timer(int(message))

    root.update_idletasks()
    root.update()
