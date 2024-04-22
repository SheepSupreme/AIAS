import time
import customtkinter
import serial

#Serial setup
<<<<<<< HEAD
serial_port = 'COM3'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=10)
=======
# serial_port = 'COM4'
# baud_rate = 9600
# ser = serial.Serial(serial_port, baud_rate, timeout=10)
>>>>>>> origin/main

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

class Filler:
    def __init__(self, root):
        self.end_time = time.time() - 999999
        self.current_time = self.end_time - time.time()
        self.root = root
        self.container = customtkinter.CTkFrame(master = self.root)
        self.container.grid(row = 0, column = 0, padx = 0, pady = 10, sticky = 'nsew')
        self.label = customtkinter.CTkLabel(self.container, font=('Arial', 24))
        self.label.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.name = customtkinter.CTkLabel(self.container, font=('Arial', 24), text = 'Filler')
        self.name.grid(row = 0, column = 0, padx = 10, pady = 10)

class App:
    def __init__(self, root):
        self.timer_list = []
        self.timer_list_count = 0

        self.root = root
        self.root.title("Current Time Display")
        self.root.columnconfigure(0,weight=1)
        self.root.geometry("600x1000")

        self.Queue = customtkinter.CTkFrame(self.root)
        self.Queue.grid(padx=10,pady=10,ipadx=10,ipady=10)

        self.entry = customtkinter.CTkEntry(self.Queue, font=('Arial', 20))
        self.entry.grid(row=0, column=0,padx=10,pady=10)

        self.button_1 = customtkinter.CTkButton(master=self.Queue, text='add timer', command=self.add_e_timer,font=('Arial', 22))
        self.button_1.grid(row=1, column=0)

        self.Ausgabe = customtkinter.CTkEntry(self.Queue, font=('Arial', 20))
        self.Ausgabe.grid(row=0, column=1,padx=10,pady=10)

        self.button_1 = customtkinter.CTkButton(master=self.Queue, text='Ausgeben', command=self.delete_timer,font=('Arial', 22))
        self.button_1.grid(row=1, column=1)

        self.update()

    def add_timer(self,time):
        try:
            self.timer_list.append(Timer('Timer_QR',time,self.root))
            self.timer_list_count += 1
            self.update_queue()
        except ValueError:
            print('ValueError')

    def add_e_timer(self):
        try:
            self.timer_list.append(Timer('Timer',int(self.entry.get()),self.root))
            self.timer_list_count += 1
            self.update_queue()     
        except ValueError:
            print('ValueError')   
    
    def delete_timer(self):
        for i in range(min(int(self.Ausgabe.get()),len(self.timer_list))):
            print('deleted', len(self.timer_list)-1)
            self.timer_list[len(self.timer_list)-1].label.destroy()
            self.timer_list[len(self.timer_list)-1].name.destroy()
            self.timer_list[len(self.timer_list)-1].container.destroy()
            del self.timer_list[len(self.timer_list)-1]
            self.timer_list_count -= 1
            if self.timer_list_count == -1:
                self.timer_list_count = 0
            self.update_queue() 

    def timer_sort(self):
        sorted_list = sorted(self.timer_list, key=lambda x: x.current_time, reverse = True)
        self.timer_list = sorted_list

    def update_queue(self):
        self.timer_sort()
        for timer in self.timer_list:
            timer.current_time = timer.end_time - time.time()
            timer.container.grid(row=self.timer_list.index(timer)+2,column=0)
            try:
                timer.label.configure(text = int(timer.current_time)) 
                if timer.current_time < 0:
                    timer.label.configure(bg_color = 'red')
            except AttributeError:
                return


    def update(self):
        self.update_queue()      
        print(self.timer_list_count)
        self.root.after(1000, self.update)


# Create the main window
root = customtkinter.CTk()

# Create an instance of the App class
game_instance = App(root)

# Run the Tkinter event loop
while True:
    # if ser.in_waiting > 0:
    #     text_mod = ser.readline()
    #     message = text_mod.decode().strip()
    #     print("message received:",message);
    #     game_instance.add_timer(int(message))

    root.update_idletasks()
    root.update()
