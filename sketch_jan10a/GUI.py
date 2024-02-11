import customtkinter
import serial

#Serial setup
serial_port = 'COM4'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)

#Customtkinter setup
root = customtkinter.CTk()

class Button:
    def __init__(self,root,name,_row,_column):
        self.root = root
        self.name = name
        self.button = customtkinter.CTkButton(master=self.root, text = self.name, command=self.send_text)
        self.button.grid(row = _row, column = _column, padx=10,pady=10)

    def send_text(self):
        message = self.name
        print(message)
        message_bytes = message.encode('utf-8')
        ser.write(message_bytes)

class App:
    def __init__(self,root):
        self.root = root
        self.root.title('GUI')
        self.root.geometry('400x150')
        self.root.columnconfigure(0,weight=1)
        self.button_calibrate = Button(self.root,'calibrate',0,0)
        self.button_blink = Button(self.root,'blink',1,0)

App(root)

root.mainloop()

# customtkinter.set_appearance_mode('dark')
