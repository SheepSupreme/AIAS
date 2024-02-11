import customtkinter
import serial

#Serial setup
serial_port = 'COM3'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)

#Customtkinter setup
root = customtkinter.CTk()

class App:
    def __init__(self,root):
        self.root = root
        self.root.title('GUI')
        self.root.geometry('400x150')
        self.root.columnconfigure(0,weight=1)

        self.button = customtkinter.CTkButton(self.root, text='blink',command = self.blink)
        self.button.grid(row=0,column=0,padx=10,pady=10)
    
    def blink(self):
        message = 'blink'
        message_bytes = message.encode('utf-8')
        ser.write(message_bytes)

App(root)

root.mainloop()

# customtkinter.set_appearance_mode('dark')
