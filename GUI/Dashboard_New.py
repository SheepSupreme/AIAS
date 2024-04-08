from customtkinter import *
from Spinbox import *


class Dashboard_New(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=1, column=1, sticky="nsew", padx=5, pady=10)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=8, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.rowconfigure(2, weight=32, uniform='a')
        self.rowconfigure(3, weight=32, uniform='a')

        self.create_headline()
        self.kapazity()
        self.ausgabe()
        self.steuerung()
        self.timer()

    def create_headline(self):

        label_headline = CTkLabel(self, text="Dashboard", text_color = "#FF99FF", font=("Arial",24,"bold"))
        label_headline.grid(column=1, row=0, sticky="nsew", pady=5, padx=5)

        label_underline = CTkLabel(self, fg_color="#FF99FF", text="", )
        label_underline.grid(column=0, row=1, columnspan=3, sticky="nsew", padx=10)

    def kapazity(self):

        Kapazity_Box = CTkFrame(self, corner_radius=5 )
        Kapazity_Box.grid(column=0, row=2, sticky="nsew", pady=10, padx=10)

        Kapazity_Box.columnconfigure(0, weight=1, uniform='a')
        Kapazity_Box.columnconfigure(1, weight=1, uniform='a')
        Kapazity_Box.columnconfigure(2, weight=1, uniform='a')
        Kapazity_Box.rowconfigure(0, weight=1, uniform='a')
        Kapazity_Box.rowconfigure(1, weight=4, uniform='a')
        Kapazity_Box.rowconfigure(2, weight=1, uniform='a')

        headline = CTkLabel(Kapazity_Box, text="Auslastung", text_color= "#FF99FF", font=("Arial",24,"bold"))
        headline.grid(column= 0, row=0, columnspan=3, pady=2, padx=2, sticky="nsew")
        
        box1 = CTkFrame(Kapazity_Box, border_color="#FF99FF", border_width=1)
        box1.grid(column=0, row=1, pady=2, padx=2, sticky="nsew")

        box2 = CTkFrame(Kapazity_Box, border_color="#FF99FF", border_width=1)
        box2.grid(column=1, row=1, pady=2, padx=2, sticky="nsew")

        box3 = CTkFrame(Kapazity_Box, border_color="#FF99FF", border_width=1)
        box3.grid(column=2, row=1, pady=2, padx=2, sticky="nsew")

        box1text = CTkLabel(Kapazity_Box, text = "0%", text_color= "#FF99FF", font=("Arial",24,"bold"))
        box1text.grid(column=0, row=2, pady=2, padx=2, sticky="nsew")

        box2text = CTkLabel(Kapazity_Box, text = "0%", text_color= "#FF99FF", font=("Arial",24,"bold"))
        box2text.grid(column=1, row=2, pady=2, padx=2, sticky="nsew")

        box3text = CTkLabel(Kapazity_Box, text = "0%", text_color= "#FF99FF", font=("Arial",24,"bold"))
        box3text.grid(column=2, row=2, pady=2, padx=2, sticky="nsew")

    def ausgabe(self):

        Ausgabe_Box = CTkFrame(self, corner_radius=5 )
        Ausgabe_Box.grid(column=0, row=3, sticky="nsew", pady=10, padx=10)

        Ausgabe_Box.columnconfigure(0, weight=1, uniform='a')
        Ausgabe_Box.rowconfigure(0, weight=2, uniform='a')
        Ausgabe_Box.rowconfigure(1, weight=4, uniform='a')
        Ausgabe_Box.rowconfigure(2, weight=4, uniform='a')

        headline = CTkLabel(Ausgabe_Box, text="Ausgabe", text_color= "#FF99FF", font=("Arial",24,"bold"))
        headline.grid(column= 0, row=0, columnspan=2, pady=2, padx=2, sticky="nsew")

        Spinbox = FloatSpinbox(Ausgabe_Box)
        Spinbox.grid(column=0, row= 1, sticky="ew")

        Button = CTkButton(Ausgabe_Box,
                            text= "Ausgeben!",
                            font=("Arial",24,"bold"),
                            fg_color = "#FF99FF",
                            text_color = "#990099",
                            hover_color="#FFB7FF")
        Button.grid(column=0, row=2, pady=(0,50), padx=20, sticky = "nsew")
        
    def steuerung(self):

        Steuerung_Box = CTkFrame(self, corner_radius=5 )
        Steuerung_Box.grid(column=1, row=2, rowspan=2, sticky="nsew", pady=10, padx=10)

        Steuerung_Box.columnconfigure(0, weight=1, uniform='a')
        Steuerung_Box.rowconfigure(0, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(1, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(2, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(3, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(4, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(5, weight=1,uniform='a')
        Steuerung_Box.rowconfigure(6, weight=1,uniform='a')

        headline = CTkLabel(Steuerung_Box, text="Steuerung", text_color="#FF99FF", font=("Arial",24, "bold"))
        headline.grid(column=0, row=0, sticky="nsew")

        class Button:
            def __init__(self,root,name,cmd,_row,_column):
                self.root = root
                self.name = name
                self.cmd = cmd
                self.button = CTkButton(master=self.root,
                                        text = self.name,
                                        command=self.send_text,
                                        fg_color="#FF99FF",
                                        text_color = "#990099",
                                        hover_color="#FFB7FF",
                                        font=("Arial",16,"bold"))
                self.button.grid(row = _row, column = _column, padx=10,pady=10, sticky="nsew")
            
            def send_text(self):
                print('sent')
            #     message = self.name
            #     print("message send:"+message)
            #     message_bytes = message.encode('ascii')
            #     ser.write(message_bytes)
            #     while True:
            #         text_mod = ser.readline()
            #         text = text_mod.decode().strip()
            #         print("message received:",text);
            #         if text == 'cmd_end': 
            #             break

        button_calibrate = Button(Steuerung_Box,'calibrate','calibration 50',1,0)
        button_blink = Button(Steuerung_Box,'blink','blink 0',2,0)
        button_pos1 = Button(Steuerung_Box,'move to pos_1', "pos_1 0",3,0)
        button_pos2 = Button(Steuerung_Box,'move to pos_2', "pos_2 0",4,0)
        button_pos3 = Button(Steuerung_Box,'move to pos_3', "pos_3 0",5,0)
        button_pos4 = Button(Steuerung_Box,'move to pos_4', "pos_4 0",6,0)


    def timer(self):

        timer_box = CTkFrame(self, corner_radius=5 )
        timer_box.grid(column=2, row=2, rowspan=2, sticky="nsew", pady=10, padx=10)

        timer_box.columnconfigure(0, weight=1, uniform='a')
        timer_box.columnconfigure(1, weight=1, uniform='a')
        timer_box.rowconfigure(0, weight=1, uniform='a')
        timer_box.rowconfigure(1, weight=6, uniform='a')

        headline = CTkLabel(timer_box, text="Verfallszeit", text_color="#FF99FF", font=("Arial",24, "bold"))
        headline.grid(column=0, row=0, columnspan=2, sticky="nsew")

        

