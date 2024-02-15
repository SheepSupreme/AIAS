import customtkinter
import serial

#Serial setup
# serial_port = 'COM3'
# baud_rate = 9600
# ser = serial.Serial(serial_port, baud_rate, timeout=2)

#Customtkinter setup
root = customtkinter.CTk()

class Button:
    def __init__(self,root,name,cmd,_row,_column):
        self.root = root
        self.name = name
        self.cmd = cmd
        self.button = customtkinter.CTkButton(master=self.root, text = self.name, command=self.send_text)
        self.button.grid(row = _row, column = _column, padx=10,pady=10)

    def send_text(self):
        print('sent')
        # message = self.name
        # print("message send:"+message)
        # message_bytes = message.encode('ascii')
        # ser.write(message_bytes)
        # while True:
        #     text_mod = ser.readline()
        #     text = text_mod.decode().strip()
        #     print("message received:",text);
        #     if text == 'cmd_end':
        #         break


class App:
    def __init__(self,root):
        self.root = root
        self.root.title('GUI')
        self.root.columnconfigure(0,weight=1)
        self.button_calibrate = Button(self.root,'calibrate','calibration 50',0,0)
        self.button_blink = Button(self.root,'blink','blink 0',1,0)
        self.button_pos1 = Button(self.root,'move to pos_1', "pos_1 0",2,0)
        self.button_pos2 = Button(self.root,'move to pos_2', "pos_2 0",3,0)
        self.button_pos3 = Button(self.root,'move to pos_3', "pos_3 0",4,0)
        self.button_pos3 = Button(self.root,'move to pos_4', "pos_4 0",5,0)

App(root)

root.mainloop()

# customtkinter.set_appearance_mode('dark')
